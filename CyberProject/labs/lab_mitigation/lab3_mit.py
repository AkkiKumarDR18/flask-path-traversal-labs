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
        
        # Ensure the file is named 'secret2.txt'
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
