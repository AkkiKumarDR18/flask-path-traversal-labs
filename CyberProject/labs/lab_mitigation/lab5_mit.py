# Lab 5: File Upload Deletes an Existing File
if lab_id == 5:
    if request.method == "POST":
        user_input = request.form.get("solution", "").strip()
        file_content = None

        # Handle file path input
        if user_input:
            file_path = os.path.abspath(os.path.join(BASE_DIR, user_input))
        
            # Ensure the file is within BASE_DIR
            if file_path.startswith(BASE_DIR) and os.path.exists(file_path):
                try:
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

                    # Ensure only files within BASE_DIR are affected
                    target_file_path = os.path.join(BASE_DIR, filename)
                    if os.path.exists(target_file_path):
                        # Instead of deleting, overwrite or log the action
                        os.replace(upload_path, target_file_path)  # Safely replace the file
                        message = f"Uploaded file '{filename}' successfully. Existing file replaced."
                    else:
                        message = f"Uploaded file '{filename}' successfully. No matching file found for replacement."

                    show_done_button = True
                except Exception as e:
                    message = f"Error processing file: {str(e)}"
        else:
            message = "No input provided. Please enter a file path or upload a file."
