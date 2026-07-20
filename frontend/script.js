const apiUrl =
  "https://r3k5esxp9a.execute-api.eu-north-1.amazonaws.com/prod/createpass";

document
  .getElementById("busPassForm")
  .addEventListener("submit", async function (e) {
    e.preventDefault();

    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "Processing...";

    const data = {
      name: document.getElementById("name").value.trim(),
      email: document.getElementById("email").value.trim(),
      phone: document.getElementById("phone").value.trim(),
      route: document.getElementById("route").value.trim(),
      passType: document.getElementById("passType").value,
    };

    try {
      const response = await fetch(apiUrl, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(data),
      });

      const text = await response.text();
      console.log("Response Status:", response.status);
      console.log("Response Body:", text);

      let result = {};

      try {
        result = JSON.parse(text);

        // Lambda responses usually return JSON inside "body"
        if (result.body) {
          result = JSON.parse(result.body);
        }
      } catch (e) {
        result = { message: text };
      }

      if (response.ok) {
        resultDiv.innerHTML = `
          <div style="color:green">
            <h3>✅ Bus Pass Created Successfully</h3>
            <p><strong>Pass ID:</strong> ${result.PassID}</p>
            <p><strong>Price:</strong> ₹${result.Price}</p>
            <p><strong>File:</strong> ${result.FileName}</p>
          </div>
        `;
      } else {
        resultDiv.innerHTML = `
          <div style="color:red">
            <strong>Error:</strong> ${
              result.error || result.message || "Something went wrong."
            }
          </div>
        `;
      }
    } catch (error) {
      console.error("Fetch Error:", error);

      resultDiv.innerHTML = `
        <div style="color:red">
          <strong>Unable to connect to server.</strong><br>
          ${error.message}
        </div>
      `;
    }
  });
