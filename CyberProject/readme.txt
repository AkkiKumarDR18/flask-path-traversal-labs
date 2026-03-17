# 🛡️ Flask Path Traversal & Security Lab
### *An Educational Sandbox for Web Vulnerability Research & Secure Coding*

## 🌟 Overview
This project is a specialized security laboratory built with **Flask**. It is designed as a hands-on environment to demonstrate common web vulnerabilities, specifically focusing on **Path Traversal**, **Unsafe File Handling**, and **Malicious File Uploads**. 

Each lab module provides a functional demonstration of how attackers exploit weak code logic and, more importantly, how developers can implement robust mitigations to defend against these "OWASP Top 10" style vulnerabilities.

---

## 🧪 Detailed Lab Modules

The application is divided into five progressive security challenges:

1.  **Lab 1: Simple Path Traversal**
    * **Vulnerability:** Unchecked file path inputs via URL parameters.
    * **Objective:** Understand how the lack of input sanitization allows unauthorized access to sensitive system files.

2.  **Lab 2: Encoding Tricks (Base64 Bypass)**
    * **Vulnerability:** Trusting encoded inputs without validation.
    * **Attack Vector:** Using Base64 to hide malicious traversal strings (like `../`) from simple string-matching security filters.

3.  **Lab 3: Improper File Upload Handling**
    * **Vulnerability:** Lack of file extension validation and unsafe storage.
    * **Impact:** Potential for Remote Code Execution (RCE) or file overwriting.

4.  **Lab 4: Zip Slip (Directory Bypass)**
    * **Vulnerability:** Unsafe extraction of compressed archives using the `zipfile` module.
    * **Attack Vector:** Exploiting filenames inside a ZIP file to overwrite files outside the intended extraction directory.

5.  **Lab 5: Advanced Path Manipulation**
    * **Vulnerability:** Unsafe file deletion/operation logic based on user-provided metadata.
    * **Mitigation:** Implementing strict directory sandboxing and identity verification.

---

## 🛠️ Tech Stack
* **Backend:** Python 3.8+
* **Framework:** Flask 2.0.0+
* **Security Modules:** Werkzeug (Secure Filename), Base64, Zipfile
* **Frontend:** Jinja2 Templates, HTML5, CSS3

---

## ⚙️ Setup & Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Cyber-Saviours/Flask-Security-Labs.git](https://github.com/Cyber-Saviours/Flask-Security-Labs.git)
    cd Flask-Security-Labs
    ```

2.  **Install Dependencies:**
    Ensure you have Python installed, then run:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Launch the Application:**
    ```bash
    python app.py
    ```

4.  **Access the Labs:** Open your browser and navigate to `http://127.0.0.1:5000`.

---

## 📂 Project Architecture
```text
├── app.py              # Main Flask Entry Point & Route Definitions
├── labs/               # Core logic and vulnerable endpoints for Lab 1-5
├── lab_Files/          # Controlled storage for lab-specific assets
├── lab_files/          # Temporary directory for user upload testing
├── templates/          # Responsive UI components and Lab interfaces
├── requirements.txt    # Python library dependencies
└── README.md           # Documentation and educational guide

## 🔒 Implemented Mitigations
This project serves as a "Fix-It" guide by demonstrating these defensive techniques:
* **Input Sanitization:** Validating all user-provided paths against a "whitelist" of safe directories.
* **Safe Extraction:** Implementing path validation during ZIP extraction to prevent directory traversal.
* **Secure Filenames:** Utilizing `werkzeug.utils.secure_filename` to strip dangerous characters from uploads.
* **Metadata Validation:** Ensuring operations (like deletion) only occur on files explicitly authorized by the system.

## 👥 The Team: Cyber Saviours
Developed as an educational initiative by:
* **AKSHAY KUMAR D R**
* **CHARAN G**
* **DEEKSHA Y V**

*📍 Based in Bangalore, India.*

---
⚠️ **DISCLAIMER:** *This application is strictly for educational and ethical security research. It contains intentional vulnerabilities and should never be deployed on a public-facing server or used for malicious purposes.*
