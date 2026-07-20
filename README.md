# 🚌 Cloud-Based Bus Pass System

A cloud-based Bus Pass System built using AWS Cloud Services that allows users to apply for digital bus passes online. The application stores bus pass details securely, generates digital records, sends email notifications, and automatically scales during high traffic using AWS Auto Scaling.

---

# 📖 Project Overview

Traditional bus pass systems often rely on manual processes that can lead to ticket loss, duplicate entries, incorrect pricing, and poor scalability. This project addresses these challenges by leveraging AWS cloud services to build a scalable, secure, and highly available bus pass management system.

---

# 🚀 Features

- Online Bus Pass Registration
- Digital Bus Pass Generation
- Dynamic Price Calculation
- Secure Data Storage
- Email Notifications
- REST API Integration
- Serverless Backend
- Auto Scaling
- High Availability
- Cloud Monitoring

---

# ☁️ AWS Services Used

- IAM
- Amazon EC2
- AWS Lambda
- Amazon API Gateway
- Amazon DynamoDB
- Amazon S3
- Amazon SNS
- Amazon CloudWatch
- Auto Scaling Group
- Application Load Balancer

---

# 📂 Project Structure

```
Cloud bus pass system
│
├── README.md
├── frontend
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── lambda
│   └── lambda_function.py
│
├── sample-bus.txt
│
└── screenshots
```

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
      Frontend Website (EC2)
                  │
                  ▼
            API Gateway
                  │
                  ▼
           AWS Lambda
      ┌────────┼─────────┐
      ▼        ▼         ▼
 DynamoDB      S3       SNS
      │
      ▼
 CloudWatch Logs
```

---

# 📸 Project Screenshots

## IAM Configuration

### IAM User

![](screenshots/1-iam-user.PNG)

### IAM User Details

![](screenshots/2-iam%20user.PNG)

### AWS IAM Login

![](screenshots/3-aws-iam-login.PNG)

### IAM Permissions

![](screenshots/4-iam-permissions.PNG)

### IAM Role

![](screenshots/5-iam-role.PNG)

---

# DynamoDB

### DynamoDB Service

![](screenshots/6-dynamodb.PNG)

### DynamoDB Table

![](screenshots/7-dynamodb-table.PNG)

### Partition Key

![](screenshots/8-dynamodb-partitionkey.PNG)

### Stored Item

![](screenshots/49-dynamodb-table-item-stored.PNG)

---

# Amazon S3

### S3 Bucket

![](screenshots/9-s3-bucket.PNG)

### Uploaded Object

![](screenshots/10-s3-bucket-upload.PNG)

### Static Website Hosting

![](screenshots/11-s3-bucket-static-website.PNG)

### Bucket Policy

![](screenshots/12-s3-bucket-policy.PNG)

### Stored Objects

![](screenshots/48-s3-objects-stored.PNG)

---

# Amazon SNS

### SNS Topic

![](screenshots/13-sns.PNG)

### Email Subscription

![](screenshots/14-sns-email-subscription.PNG)

### Email Notification

![](screenshots/16-sns-notification-received.PNG)

### Mail Notification

![](screenshots/50-mail-msg.PNG)

![](screenshots/51-mail-msg.PNG)

![](screenshots/52-mail-msg.PNG)

---

# AWS Lambda

### Lambda Function

![](screenshots/15-lambda.PNG)

### Environment Variables

![](screenshots/17-lambda-environment-variables.PNG)

### Lambda Code

![](screenshots/18-lambda-code.PNG)

![](screenshots/19-lambda-code.PNG)

![](screenshots/20-lambda-code.PNG)

![](screenshots/21-lambda-code.PNG)

![](screenshots/22-lambda-code.PNG)

![](screenshots/23-lambda-code.PNG)

![](screenshots/24-lambda-code.PNG)

### Test Event

![](screenshots/25-lambda-test-event.PNG)

### Successful Test Result

![](screenshots/26-successful-lambda-test-result.PNG)

---

# API Gateway

### HTTP API Created

![](screenshots/27-http-api-created.PNG)

### API Route

![](screenshots/28-apo-route.PNG)

### API CORS Configuration

![](screenshots/29-api-cors-configuration.PNG)

### API Invoke URL

![](screenshots/29-api-invoke-url.PNG)

---

# Testing using Postman

### POST Request

![](screenshots/30-post-request.PNG)

### Successful Response

![](screenshots/31-postman-added-meassage.PNG)

---

# Frontend

### Bus Pass Application

![](screenshots/32-frontend-submission.PNG)

---

# EC2 Deployment

### EC2 Instance

![](screenshots/33-ec2-instance-created.PNG)

### Security Group

![](screenshots/34-security-group-rules.PNG)

### SSH Connection

![](screenshots/35-ssh-teminal-connected.PNG)

### Apache Running

![](screenshots/36-apache-running.PNG)

### Website Hosted on EC2

![](screenshots/37-website-opened-using-ec2-public-ip.PNG)

---

# Auto Scaling

### Launch Template

![](screenshots/38-launch-template.PNG)

### Auto Scaling Group

![](screenshots/39-auto-scaling-group.PNG)

### Scaling Policy

![](screenshots/40-scaling-policy.PNG)

### Load Balancer

![](screenshots/41-load-balancer.PNG)

### Application Load Balancer

![](screenshots/42-application-load-balancer.PNG)

### Target Group

![](screenshots/43-target-group.PNG)

### Health Check

![](screenshots/44-health-check.PNG)

---

# CloudWatch Monitoring

### CloudWatch Dashboard

![](screenshots/45-cloudwatch.PNG)

### CPU Utilization

![](screenshots/46-cloudwatch-cpu-graph.PNG)

---

# Auto Scaling Result

### Two EC2 Instances Running

![](screenshots/47-two-ec2-instances-running-after-autoscaling.PNG)

---

# Technologies Used

- HTML5
- CSS3
- JavaScript
- Python
- AWS Lambda
- Amazon EC2
- Amazon DynamoDB
- Amazon S3
- Amazon SNS
- Amazon API Gateway
- CloudWatch
- Auto Scaling
- Application Load Balancer

---

# Future Enhancements

- User Authentication
- QR Code Bus Pass
- Payment Gateway Integration
- PDF Bus Pass
- Admin Dashboard
- Mobile Application

---

# Author

**Ruchita Amey Deshmukh**

AWS Cloud | DevOps | Full Stack Development

---

⭐ If you found this project useful, don't forget to Star this repository.
