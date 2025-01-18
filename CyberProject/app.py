from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
import base64
import re
import logging
import zipfile

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Required for session handling

# Set the base directory for lab files
BASE_DIR = os.path.join(os.getcwd(), "labs", "lab_Files")
UPLOAD_DIR = os.path.join(os.getcwd(), "labs", "lab_files")

# Ensure the directories exist
if not os.path.exists(BASE_DIR):
    os.makedirs(BASE_DIR)  # Create the folder if it doesn't exist
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)  # Create the upload folder if it doesn't exist

# Lab challenges with expected solutions
labs = [
    {"id": 1, "name": "Lab 1: Simple Path Traversal", "points": 10, "unlocked": True, "solution": "../secret.txt"},
    {"id": 2, "name": "Lab 2: Encoding Tricks", "points": 15, "unlocked": True, "solution": "Li4vc2VjcmV0LnR4dA=="},
    {"id": 3, "name": "Lab 3: File Upload", "points": 20, "unlocked": True, "solution": "../secret2.txt"},
    {"id": 4, "name": "Lab 4: Directory Bypass", "points": 25, "unlocked": True, "solution": "restricted.zip"},
    {"id": 5, "name": "Lab 5: Advanced Path Manipulation", "points": 30, "unlocked": True, "solution": "instructions.txt"}
]

# Function to validate Base64 strings
def is_valid_base64(s):
    base64_regex = re.compile(r'^[A-Za-z0-9+/=]+$')
    return bool(base64_regex.match(s))

# Function to ensure zip file paths are safe
def is_safe_zip(zip_path, extract_path):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        for member in zip_ref.namelist():
            member_path = os.path.abspath(os.path.join(extract_path, member))
            if not os.path.commonpath([extract_path, member_path]).startswith(extract_path):
                return False
    return True

# Function to move extracted files to BASE_DIR
def move_extracted_files_to_base_dir(extract_path, base_dir):
    for root, _, files in os.walk(extract_path):
        for file in files:
            file_path = os.path.join(root, file)
            target_path = os.path.join(base_dir, file)
            os.rename(file_path, target_path)
            print(f"Moved: {file_path} -> {target_path}")

# Initialize session variables
def initialize_session():
    if "score" not in session:
        session["score"] = 0
    if "completed_labs" not in session:
        session["completed_labs"] = []
    for lab in labs:
        lab["unlocked"] = True

@app.route("/")
def index():
    initialize_session()
    return render_template("index.html", labs=labs, score=session["score"])

@app.route("/lab/<int:lab_id>", methods=["GET", "POST"])
def complete_lab(lab_id):
    initialize_session()
    lab = next((lab for lab in labs if lab["id"] == lab_id), None)

    if not lab:
        return "Lab not found", 404

    message = None
    file_content = None
    show_done_button = False

    if request.method == "POST":
        user_input = request.form.get("solution", "").strip()

        # Lab 1: Simple Path Traversal
        if lab_id == 1:
            file_path = os.path.abspath(os.path.join(BASE_DIR, user_input))
            if os.path.exists(file_path) or os.path.exists(user_input):
                target_path = file_path if os.path.exists(file_path) else user_input
                try:
                    with open(target_path, "r", encoding="utf-8") as file:
                        file_content = file.read()
                    if user_input == lab["solution"]:
                        show_done_button = True
                except Exception as e:
                    message = f"Error reading file: {str(e)}"
            else:
                message = "File not found."

        # Lab 2: Encoding Tricks
        elif lab_id == 2:
            if user_input == lab["solution"]:
                file_path = os.path.abspath(os.path.join(BASE_DIR, "../secret.txt"))
                if os.path.exists(file_path) and os.path.commonpath([BASE_DIR, file_path]) == BASE_DIR:
                    with open(file_path, "r", encoding="utf-8") as file:
                        file_content = file.read()
                    if user_input == lab["solution"]:
                        show_done_button = True
                elif os.path.exists(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as file:
                            file_content = file.read()
                        show_done_button = True
                    except Exception as e:
                        message = f"Error reading file: {str(e)}"
                else:
                    message = "File not found."
            elif "../" in user_input:
                message = "Access Denied: File paths cannot contain '../'."
            else:
                message = "Invalid input."

         # Lab 3: File Upload
        if lab_id == 3:
            # Handle file path submission
            if user_input:
                file_path = os.path.abspath(os.path.join(BASE_DIR, user_input))
                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as file:
                            file_content = file.read()
                            message = "File read successfully."
                            show_done_button = True
                    except Exception as e:
                        message = f"Error reading file: {str(e)}"
                else:
                    message = "File not found."
            # Handle file upload
            elif "file" in request.files:
                uploaded_file = request.files["file"]
                filename = secure_filename(uploaded_file.filename)
                if filename == "secret2.txt":
                    file_path = os.path.join(UPLOAD_DIR, filename)
                    try:
                        uploaded_file.save(file_path)
                        with open(file_path, "r", encoding="utf-8") as file:
                            file_content = file.read()
                        message = f"File '{filename}' uploaded successfully and content read!"
                        show_done_button = True
                    except Exception as e:
                        message = f"Error processing uploaded file: {str(e)}"
                else:
                    message = "Invalid file name. Please upload 'secret2.txt'."

        # Lab 4: Directory Bypass
        elif lab_id == 4:
            # Handle file path submission
            if user_input:
                file_path = os.path.abspath(os.path.join(BASE_DIR, user_input))
                if os.path.exists(file_path):
                    try:
                        with open(file_path, "r", encoding="utf-8") as file:
                            file_content = file.read()
                            message = "File read successfully."
                            show_done_button = True
                    except Exception as e:
                        message = f"Error reading file: {str(e)}"
                else:
                    message = "File not found."
            # Handle zip file upload
            elif "file" in request.files:
                uploaded_file = request.files["file"]
                filename = secure_filename(uploaded_file.filename)
                if filename.endswith(".zip"):
                    zip_path = os.path.join(UPLOAD_DIR, filename)
                    try:
                        uploaded_file.save(zip_path)
                        if is_safe_zip(zip_path, UPLOAD_DIR):
                            with zipfile.ZipFile(zip_path, "r") as zip_ref:
                                zip_ref.extractall(UPLOAD_DIR)
                    
                            # Move extracted files to BASE_DIR
                            move_extracted_files_to_base_dir(UPLOAD_DIR, BASE_DIR)

                            extracted_file = os.path.join(BASE_DIR, "secret2.txt")
                            if os.path.exists(extracted_file):
                                with open(extracted_file, "r", encoding="utf-8") as file:
                                    file_content = file.read()
                                message = "Zip file uploaded, extracted, and file read successfully!"
                                show_done_button = True
                            else:
                                message = "Expected file not found after extraction."
                        else:
                            message = "Unsafe zip file detected! Extraction denied."
                    except Exception as e:
                        message = f"Error processing zip file: {str(e)}"
                else:
                    message = "Invalid file type. Please upload a zip file."

        # Lab 5: File Upload Deletes an Existing File
        elif lab_id == 5:
            if request.method == "POST":
                user_input = request.form.get("solution", "").strip()
                file_content = None
                show_done_button = False

                # Handle file path input
                if user_input:
                    file_path = os.path.abspath(os.path.join(BASE_DIR, user_input))

                    # Check if the file exists and is within BASE_DIR
                    if os.path.exists(file_path) and file_path.startswith(BASE_DIR):
                        try:
                            # Read the file content
                            with open(file_path, "r", encoding="utf-8") as file:
                                file_content = file.read()
                            message = f"File '{user_input}' read successfully. Content is displayed below."
                            show_done_button = True
                        except Exception as e:
                            message = f"Error reading file: {str(e)}"
                    else:
                        message = "File not found or access denied."

                # Handle file upload
                elif "file" in request.files:
                    uploaded_file = request.files["file"]
                    filename = secure_filename(uploaded_file.filename)
                    upload_path = os.path.abspath(os.path.join(UPLOAD_DIR, filename))

                    if not upload_path.startswith(UPLOAD_DIR):
                        message = "Invalid file path. Path traversal attempt detected!"
                    else:
                        try:
                            # Save the uploaded file
                            uploaded_file.save(upload_path)

                            # Read the content of the uploaded file
                            with open(upload_path, "r", encoding="utf-8") as file:
                                uploaded_file_content = file.readlines()

                            # Parse the uploaded file for file paths to delete
                            deleted_files = []
                            for line in uploaded_file_content:
                                line = line.strip()
                                target_file_path = os.path.join(BASE_DIR, line)
                                if os.path.exists(target_file_path) and target_file_path.startswith(BASE_DIR):
                                    os.remove(target_file_path)
                                    deleted_files.append(line)

                            if deleted_files:
                                message = f"Uploaded file processed successfully. The following files were deleted: {', '.join(deleted_files)}."
                            else:
                                message = "No valid files were found to delete."

                            show_done_button = True

                        except Exception as e:
                            message = f"Error processing file: {str(e)}"
                else:
                    message = "No input provided. Please enter a file path or upload a file."

    # Handle "Done" button click
    if request.method == "POST" and "done" in request.form:
        if lab["id"] not in session["completed_labs"]:
            session["completed_labs"].append(lab["id"])
            session["score"] += lab["points"]
            session.modified = True
        return redirect(url_for("index"))

    return render_template("lab.html", lab=lab, message=message, file_content=file_content, show_done_button=show_done_button)

@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
