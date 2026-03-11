import os
from config import max_characters


def get_file_content(working_dir, file_path):

    try:
        working_dir_abs = os.path.abspath(working_dir)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_file_path = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_path_abs):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(file_path_abs, 'r', encoding='utf-8') as file:
            file_content_as_string = file.read(max_characters)

        return file_content_as_string

    except Exception as e:
        return f"Error: {str(e)}"
    
