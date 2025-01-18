# Lab 1: Simple Path Traversal
if lab_id == 1:
    file_path = os.path.abspath(os.path.join(BASE_DIR, user_input))
    
    # Ensure the path is within the BASE_DIR
    if file_path.startswith(BASE_DIR):
        if os.path.exists(file_path):
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    file_content = file.read()
                if user_input == lab["solution"]:
                    show_done_button = True
            except Exception as e:
                message = f"Error reading file: {str(e)}"
        else:
            message = "File not found."
    else:
        message = "Access Denied: Invalid file path."

