# 𝗙𝗹𝗮𝘀𝗸 𝗣𝗮𝘁𝗵 𝗧𝗿𝗮𝘃𝗲𝗿𝘀𝗮𝗹 𝗩𝘂𝗹𝗻𝗲𝗿𝗮𝗯𝗹𝗲 𝗔𝗽𝗽𝗹𝗶𝗰𝗮𝘁𝗶𝗼𝗻

## 𝗢𝘃𝗲𝗿𝘃𝗶𝗲𝘄
This project is a demonstration of various vulnerabilities for educational purposes. It consists of five labs, each showcasing a different security issue related to path traversal, file handling, and unsafe file uploads. These labs are designed to help users learn about security flaws and understand how to mitigate them.

## 𝗙𝗲𝗮𝘁𝘂𝗿𝗲𝘀
1. 𝐋𝐚𝐛 𝟏: 𝐒𝐢𝐦𝐩𝐥𝐞 𝐏𝐚𝐭𝐡 𝐓𝐫𝐚𝐯𝐞𝐫𝐬𝐚𝐥
   - Explores the risk of allowing unchecked file path inputs.

2. 𝐋𝐚𝐛 𝟐: 𝐄𝐧𝐜𝐨𝐝𝐢𝐧𝐠 𝐓𝐫𝐢𝐜𝐤𝐬
   - Demonstrates how Base64 encoding can be exploited to bypass security mechanisms.

3. 𝐋𝐚𝐛 𝟑: 𝐅𝐢𝐥𝐞 𝐔𝐩𝐥𝐨𝐚𝐝
   - Highlights the dangers of improper handling of uploaded files.

4. 𝐋𝐚𝐛 𝟒: 𝐃𝐢𝐫𝐞𝐜𝐭𝐨𝐫𝐲 𝐁𝐲𝐩𝐚𝐬𝐬
   - Shows how zip file extraction can be exploited for path traversal attacks.

5. 𝐋𝐚𝐛 𝟓: 𝐀𝐝𝐯𝐚𝐧𝐜𝐞𝐝 𝐏𝐚𝐭𝐡 𝐌𝐚𝐧𝐢𝐩𝐮𝐥𝐚𝐭𝐢𝐨𝐧
   - Focuses on unsafe file operations when handling user uploads.

## 𝗥𝗲𝗾𝘂𝗶𝗿𝗲𝗺𝗲𝗻𝘁𝘀
- Python 3.8 or later
- Flask 2.0.0 or later
- Werkzeug (for secure file handling)
- Base64 and Zipfile modules (default in Python)

## 𝗦𝗲𝘁𝘂𝗽 𝗜𝗻𝘀𝘁𝗿𝘂𝗰𝘁𝗶𝗼𝗻𝘀
1. Clone or download the project to your local machine.
2. Navigate to the project directory:
	cd <project-folder>
3. Install dependencies:
	pip install -r requirements.txt
4. Run the Flask application:
	python app.py
5. Open your browser and navigate to:
	http://127.0.0.1:5000

## 𝗙𝗶𝗹𝗲 𝗦𝘁𝗿𝘂𝗰𝘁𝘂𝗿𝗲
- `app.py`: The main Flask application file.
- `labs/`: Directory containing lab-specific files and upload folders.
- `lab_Files/`: Stores files for the labs.
- `lab_files/`: Temporary folder for user uploads.
- `templates/`: Contains HTML templates for rendering the web pages.
- `static/`: Optional directory for CSS, JS, or other static assets.

## 𝗦𝗲𝗰𝘂𝗿𝗶𝘁𝘆 𝗩𝘂𝗹𝗻𝗲𝗿𝗮𝗯𝗶𝗹𝗶𝘁𝗶𝗲𝘀 𝗗𝗲𝗺𝗼𝗻𝘀𝘁𝗿𝗮𝘁𝗲𝗱
1. 𝐏𝐚𝐭𝐡 𝐓𝐫𝐚𝐯𝐞𝐫𝐬𝐚𝐥:
- Labs 1, 4, and 5 demonstrate risks related to improper file path handling.

2. 𝐁𝐚𝐬𝐞𝟔𝟒 𝐄𝐧𝐜𝐨𝐝𝐢𝐧𝐠 𝐓𝐫𝐢𝐜𝐤𝐬:
- Lab 2 shows how attackers can exploit improperly validated Base64-encoded inputs.

3. 𝐔𝐧𝐬𝐚𝐟𝐞 𝐅𝐢𝐥𝐞 𝐔𝐩𝐥𝐨𝐚𝐝𝐬:
- Labs 3 and 5 demonstrate the dangers of allowing unvalidated file uploads.

## 𝗠𝗶𝘁𝗶𝗴𝗮𝘁𝗶𝗼𝗻𝘀 𝗜𝗺𝗽𝗹𝗲𝗺𝗲𝗻𝘁𝗲𝗱
- 𝐋𝐚𝐛 𝟏: File path validation to prevent path traversal attacks.
- 𝐋𝐚𝐛 𝟐: Base64 decoding with validation and dangerous content detection.
- 𝐋𝐚𝐛 𝟑: Restricts uploaded files to specific names and ensures safe handling.
- 𝐋𝐚𝐛 𝟒: Checks extracted zip file paths to prevent directory traversal.
- 𝐋𝐚𝐛 𝟓: Deletes only files explicitly listed within the uploaded file to ensure controlled deletion.

## 𝗘𝗱𝘂𝗰𝗮𝘁𝗶𝗼𝗻𝗮𝗹 𝗚𝗼𝗮𝗹𝘀
This project is intended for ethical use in learning about vulnerabilities and secure coding practices. It should not be used for malicious purposes. Always follow ethical guidelines when working with security concepts.

## 𝗟𝗶𝗰𝗲𝗻𝘀𝗲
||||||||||||||||This project is released under the MIT License. See LICENSE for details.|||||||||||||||||||

## 𝗖𝗼𝗻𝘁𝗮𝗰𝘁
For further queries, feel free to reach out:
- Name: Cyber Saviours
- Group Members: 
	AKSHAY KUMAR D R
	CHARAN G
	DEEKSHA Y V
- Location: Bangalore

