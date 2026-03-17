# 🛡️ Flask Path Traversal & Security Lab
### *An Educational Sandbox for Web Vulnerability Research*

## 🌟 Overview
This project is a specialized security laboratory built with **Flask**. It is designed to demonstrate common web vulnerabilities, specifically focusing on **Path Traversal**, **Unsafe File Handling**, and **Malicious File Uploads**. 

Each lab provides a hands-on environment to understand how attackers exploit weak code and, more importantly, how developers can implement robust mitigations using secure coding practices.

## 🧪 Detailed Lab Modules
The application is divided into five progressive security challenges:

1.  **Lab 1: Simple Path Traversal** * **Vulnerability:** Unchecked file path inputs via URL parameters.
    * **Impact:** Unauthorized access to sensitive system files (e.g., `/etc/passwd`).

2.  **Lab 2: Encoding Tricks (Base64 Bypass)** * **Vulnerability:** Trusting encoded inputs.
    * **Attack Vector:** Using Base64 to hide malicious traversal strings from simple security filters.

3.  **Lab 4: Zip Slip (Directory Bypass)** * **Vulnerability:** Unsafe extraction of compressed archives.
    * **Attack Vector:** Exploiting `zipfile` extraction to overwrite files outside the intended directory.

4.  **Lab 3 & 5: Unsafe File Operations** * **Vulnerability:** Improper handling of user-uploaded files and metadata.
    * **Mitigation:** Implementation of `werkzeug.utils.secure_filename` and strict directory sandboxing.



## 🛠️ Tech Stack & Requirements
* **Backend:** Python 3.8+ / Flask 2.0.0+
* **Security Utilities:** Werkzeug (Secure Filename), Base64, Zipfile
* **Frontend:** Jinja2 Templates, HTML5, CSS3

## ⚙️ Setup & Installation
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Cyber-Saviours/Flask-Security-Labs.git](https://github.com/Cyber-Saviours/Flask-Security-Labs.git)
    cd Flask-Security-Labs
    ```
2.  **Environment Setup:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Application:**
    ```bash
    python app.py
    ```
4.  **Access the Labs:** Navigate to `http://127.0.0.1:5000` in your browser.

## 📂 Project Architecture
```text
├── app.py              # Main Flask Entry Point
├── labs/               # Lab logic and vulnerable endpoints
├── lab_files/          # Controlled environment for file operations
├── templates/          # Responsive UI components
├── requirements.txt    # Python dependencies
└── README.md           # Documentation

## 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗩𝘂𝗹𝗻𝗲𝗿𝗮𝗯𝗶𝗹𝗶𝘁𝗶𝗲𝘀 𝗗𝗲𝗺𝗼𝗻𝘀𝘁𝗿𝗮𝘁𝗲𝗱
1. 𝐏𝐚𝐭𝐡 𝐓𝐫𝐚𝐯𝐞𝐫𝐬𝐚𝐥:
- Labs 1, 4, and 5 demonstrate risks related to improper file path handling.

2. 𝐁𝐚𝐬𝐞𝟔𝟒 𝐄𝐧𝐜𝐨𝐝𝐢𝐧𝐠 𝐓𝐫𝐢𝐜𝐤𝐬:
- Lab 2 shows how attackers can exploit improperly validated Base64-encoded inputs.

3. 𝐔𝐧𝐬𝐚𝐟𝐞 𝐅𝐢𝐥𝐞 𝐔𝐩𝐥𝐨𝐚𝐝𝐬:
- Labs 3 and 5 demonstrate the dangers of allowing unvalidated file uploads.

## 𝗠𝗶𝘁𝗶𝗴𝗮𝘁𝗶𝗼𝗻𝘀 𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁𝗲𝗱
* 𝐋𝐚𝐛 𝟏: File path validation to prevent path traversal attacks.
* 𝐋𝐚𝐛 𝟐: Base64 decoding with validation and dangerous content detection.
* 𝐋𝐚𝐛 𝟑: Restricts uploaded files to specific names and ensures safe handling.
* 𝐋𝐚𝐛 𝟒: Checks extracted zip file paths to prevent directory traversal.
* 𝐋𝐚𝐛 𝟓: Deletes only files explicitly listed within the uploaded file to ensure controlled deletion.

## 𝗘𝗱𝘂𝗰𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗚𝗼𝗮𝗹𝘀
This project is intended for ethical use in learning about vulnerabilities and secure coding practices. It should not be used for malicious purposes. Always follow ethical guidelines when working with security concepts.

## 𝗖𝗼𝗻𝘁𝗮𝗰𝘁
For further queries, feel free to reach out:
* Name: Cyber Saviours
* Group Members: 
	AKSHAY KUMAR D R
	CHARAN G
	DEEKSHA Y V
* Location: Bangalore

