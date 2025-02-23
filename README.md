# 🔐 VeriScan - Password Strength Checker API  

This project implements a **Password Strength Checker** using **Python** and **AWS Lambda**. The API evaluates password strength based on multiple factors and provides feedback on whether they are **weak**, **strong**, or somewhere in between.  

---  

## 🚀 Features  

- ✅ **Presence of uppercase, lowercase, numbers, and special characters.**
- ✅ **Checks for personal information** (first/last name) in the password.  
- ✅ **Validates password length** to ensure security.  
- ✅ **Detects common passwords** using a predefined list.  
- ✅ **Provides a score & feedback** (🔴 Weak, 🟠 Fine, 🟡 Good, 🟢 Great). 
---  

## 🛠️ Setup Instructions  

### 🏗️ AWS Lambda Setup  

To deploy the function as an AWS Lambda service:  

1️⃣ **Create a Lambda Function:**  
   - Go to the **AWS Lambda Console**.  
   - Click **Create Function**.  
   - Choose **Author from scratch**.  
   - Set the function name to `password-strength-checker`.  
   - Select **Python 3.x** as the runtime.  
   - In the execution role, choose **Create a new role with basic Lambda permissions**.  
   - Click **Create Function**.  

2️⃣ **Deploy Code to Lambda:**  
   - In the **Lambda function code editor**, replace the default code using the **Upload** button.  
   - Click **Deploy** to save the function.  

3️⃣ **Set Environment Variables (Optional but Recommended):**  
   - Go to the **Configuration tab** in AWS Lambda.  
   - Add key-value pairs under **Environment Variables** for storing configurations. 

---  

### 🌐 API Gateway Setup  

To expose the Lambda function as a **REST API**:  

1️⃣ **Create an API:**  
   - Go to the **API Gateway Console**.  
   - Click **Create API** → Select **REST API**.  
   - Configure the API name, description, and endpoint type.  

2️⃣ **Integrate API with Lambda:**  
   - In the **Resources tab**, click **Actions → Create Method** and choose **POST**.  
   - Select **Lambda Function** as the **Integration Type**.  
   - Specify your Lambda function (`password-strength-checker`) and save.  

3️⃣ **Enable CORS (Optional):**  
   - Select your method (**POST**) → Click **Actions → Enable CORS**.  
   - This allows your API to be accessed from a web browser.  

4️⃣ **Deploy API:**  
   - Go to **Stages → Create Stage** (e.g., `prod`).  
   - Select **Deploy API**.  
   - Note the **Invoke URL**—this is your API endpoint for HTTP requests.  

---  

## 💻 Local Development  

If you want to run the password strength checker locally:  

1️⃣ **Clone the Repository:**  
   ```bash
   git clone https://github.com/priyanshukumar13/Veriscan.git  
   cd Veriscan  
   ```  

2️⃣ **Install Dependencies:**  
   ```bash
   pip install -r requirements.txt  
   ```  

3️⃣ **Run the Function:**  
   - Call the `check_password_strength()` function directly in Python.  
   - Integrate it with a local API testing framework like **Flask**.  

⚠️ **Security Tip:** Do not expose your actual API URL publicly! Use environment variables or placeholders in documentation to prevent unauthorized access.  

---  

🎯 **Enjoy using VeriScan to enhance password security! 🔒**
