# Lab 2: Encoding Tricks (Updated Mitigation)
if lab_id == 2:
    if is_valid_base64(user_input):
        decoded_content = base64.b64decode(user_input).decode("utf-8")
        
        # Check for dangerous patterns in decoded content
        dangerous_patterns = ["../", "..\\", "/etc/", "C:\\", "\\windows\\"]
        if any(pattern in decoded_content.lower() for pattern in dangerous_patterns):
            message = "Decoded content contains unsafe patterns. Access denied."
        else:
            # Proceed if decoded content is safe
            file_path = os.path.abspath(os.path.join(BASE_DIR, decoded_content))
            
            # Ensure the path is within the BASE_DIR
            if file_path.startswith(BASE_DIR) and os.path.exists(file_path):
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        file_content = file.read()
                    if decoded_content == lab["solution"]:
                        show_done_button = True
                    else:
                        message = "Decoded content does not match the expected solution."
                except Exception as e:
                    message = f"Error reading file: {str(e)}"
            else:
                message = "Access Denied: Invalid file path or file not found."
    else:
        message = "Invalid Base64 encoding."
