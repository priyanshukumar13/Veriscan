# Veriscan 🚀

## 🔐 Password Strength Checker API

This project implements a **Password Strength Checker** using **Python** and **AWS Lambda**. The API evaluates password security based on:

- ✅ **Presence of uppercase, lowercase, numbers, and special characters.**
- ✅ **Checks for personal information** (first/last name) in the password.  
- ✅ **Validates password length** to ensure security.  
- ✅ **Detects common passwords** using a predefined list.  
- ✅ **Provides a score & feedback** (🔴 Weak, 🟠 Fine, 🟡 Good, 🟢 Great). 

## 📌 Features

- 🛡 **Checks for inclusion of personal information** (first/last name) in passwords.
- 🔍 **Validates password length** to ensure better security.
- 📋 **Uses a predefined list (`common.txt`)** to detect commonly used passwords.
- 📊 **Provides feedback based on a scoring system:**  
  - 🔴 **Very Weak:** Use a mix of uppercase, lowercase, numbers, and symbols.  
  - 🟠 **Weak:** Consider making your password longer and adding special characters.  
  - 🟡 **Fair:** Adding numbers or uncommon words can improve security.  
  - 🟢 **Strong:** Your password is quite strong, but avoid common words.  
  - ✅ **Very Strong:** Your password is highly secure!  

---

## 🛠 Setup Instructions

### 🚀 AWS Lambda Setup

To deploy the function as an AWS Lambda service:

1. **Create a Lambda Function:**
   - Go to the **AWS Lambda Console**.
   - Click **Create Function**.
   - Choose **Author from scratch**.
   - Set the function name to `password-strength-checker`.
   - Select **Python 3.x** as the runtime environment.
   - Choose **Create a new role with basic Lambda permissions**.
   - Click **Create Function**.

2. **Deploy Code to Lambda:**
   - In the **Lambda function code editor**, replace the default code.
   - Upload the `common.txt` file via the **Upload button** or include it in a deployment package.
   - Click **Deploy** to save the function.

3. **Set Environment Variables (Optional but Recommended):**
   - Store values like the `common.txt` path in environment variables.
   - Go to **Configuration > Environment Variables** and add key-value pairs.

### 🌐 API Gateway Setup (Expose as a REST API)

1. **Create an API:**
   - Go to **API Gateway Console**.
   - Click **Create API** and select **REST API**.
   - Configure **API name, description, and endpoint type**.

2. **Integrate API with Lambda:**
   - In the **Resources** tab, click **Actions > Create Method** and choose **POST**.
   - Select **Lambda Function** as the integration type.
   - Specify your Lambda function (`password-strength-checker`) and save.

3. **Enable CORS (Optional):**
   - Select **POST method** > **Actions > Enable CORS**.
   - This allows API access from a web browser.

4. **Deploy API:**
   - Go to **Stages > Create Stage** (e.g., `prod`).
   - Deploy the API by selecting **Deploy API**.
   - Note the **Invoke URL** (your API endpoint for requests).

---

## 🖥 Local Development

If you want to run the password strength checker **locally**:

1. Clone the repository:
   ```bash
   git clone https://github.com/priyanshukumar13/Veriscan.git
   cd PasswordChecker
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the function:
   - Call `check_password_strength()` directly in Python.
   - Or integrate it with a local API testing framework like **Flask**.

⚠ **Security Tip:** Avoid exposing your actual API URL publicly. Use **environment variables** or placeholders instead.

---

📌 **Now you're all set!** Enjoy using **Veriscan** for better password security! 🔐🚀
