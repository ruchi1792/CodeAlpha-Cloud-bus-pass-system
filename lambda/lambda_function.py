import json
import os
import uuid
import boto3
from datetime import datetime, timedelta

# AWS Clients
dynamodb = boto3.resource('dynamodb')
s3 = boto3.client('s3')
sns = boto3.client('sns')

# Environment Variables
TABLE_NAME = os.environ['TABLE_NAME']
BUCKET_NAME = os.environ['BUCKET_NAME']
TOPIC_ARN = os.environ['TOPIC_ARN']

table = dynamodb.Table(TABLE_NAME)


# Price Calculation
def calculate_price(pass_type):
    prices = {
        "Daily": 50,
        "Weekly": 300,
        "Monthly": 800
    }
    return prices.get(pass_type, 0)


def lambda_handler(event, context):
    try:

        # Print event for debugging
        print("Received Event:")
        print(json.dumps(event))

        # Handle API Gateway request
        if "body" in event:
            body = event["body"]

            # If body is JSON string, convert to dictionary
            if isinstance(body, str):
                body = json.loads(body)
        else:
            # Lambda Test Event
            body = event

        # Read request data
        name = body.get("name")
        email = body.get("email")
        phone = body.get("phone")
        route = body.get("route")
        pass_type = body.get("passType")

        # Validate input
        if not all([name, email, phone, route, pass_type]):
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Missing required fields"
                })
            }

        # Generate Pass ID
        pass_id = "PASS-" + str(uuid.uuid4())[:8]

        issue_date = datetime.now()

        if pass_type == "Daily":
            expiry_date = issue_date + timedelta(days=1)
        elif pass_type == "Weekly":
            expiry_date = issue_date + timedelta(days=7)
        elif pass_type == "Monthly":
            expiry_date = issue_date + timedelta(days=30)
        else:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "message": "Invalid Pass Type"
                })
            }

        price = calculate_price(pass_type)

        # Save to DynamoDB
        table.put_item(
            Item={
                "PassID": pass_id,
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Route": route,
                "PassType": pass_type,
                "Price": price,
                "IssueDate": issue_date.strftime("%Y-%m-%d"),
                "ExpiryDate": expiry_date.strftime("%Y-%m-%d"),
                "Status": "Active"
            }
        )

        # Create pass file
        pass_text = f"""
Cloud-Based Bus Pass

Pass ID : {pass_id}

Name : {name}

Email : {email}

Phone : {phone}

Route : {route}

Pass Type : {pass_type}

Price : ₹{price}

Issue Date : {issue_date.strftime('%Y-%m-%d')}

Expiry Date : {expiry_date.strftime('%Y-%m-%d')}

Status : Active
"""

        file_name = f"{pass_id}.txt"

        # Upload to S3
        s3.put_object(
            Bucket=BUCKET_NAME,
            Key=file_name,
            Body=pass_text
        )

        # Send SNS Notification
        sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="Bus Pass Created Successfully",
            Message=f"""
Hello {name},

Your Bus Pass has been created successfully.

Pass ID : {pass_id}

Route : {route}

Pass Type : {pass_type}

Price : ₹{price}

Issue Date : {issue_date.strftime('%Y-%m-%d')}

Expiry Date : {expiry_date.strftime('%Y-%m-%d')}

Status : Active

Thank you for using our Cloud-Based Bus Pass System.
"""
        )

        # Success Response
        return {
            "statusCode": 200,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "message": "Bus Pass Created Successfully",
                "PassID": pass_id,
                "Price": price,
                "FileName": file_name
            })
        }

    except Exception as e:
        print("Error:", str(e))

        return {
            "statusCode": 500,
            "headers": {
                "Content-Type": "application/json"
            },
            "body": json.dumps({
                "error": str(e)
            })
        }