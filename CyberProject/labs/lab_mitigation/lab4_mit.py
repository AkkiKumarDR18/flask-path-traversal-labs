# Lab 4: Directory Bypass
if lab_id == 4:
    # Handle zip file upload
    if "file" in request.files:
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
