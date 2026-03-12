import os
import subprocess



def run_python_file(working_directory, file_path, args=None):

    try:
        
        working_dir_abs = os.path.abspath(working_directory)
        file_path_abs = os.path.normpath(os.path.join(working_dir_abs, file_path))

        valid_file_path = os.path.commonpath([working_dir_abs, file_path_abs]) == working_dir_abs

        if not valid_file_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        
        if not os.path.isfile(file_path_abs):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        
        command = ["python", file_path_abs]

        if args:
            command.extend(args)

        run_command = subprocess.run(command, capture_output=True, text=True, cwd=working_dir_abs, timeout=30)

        output_parts = []

        if run_command.returncode != 0:
            output_parts.append(f"Process exited with code {run_command.returncode}")

        if run_command.stdout:
            output_parts.append(f"STDOUT:\n{run_command.stdout.strip()}")

        if run_command.stderr:
            output_parts.append(f"STDERR:\n{run_command.stderr.strip()}")

        if not output_parts:
            return "No output produced"

        return "\n".join(output_parts)
        

    except Exception as e:
        return f"Error: executing Python file: {e}"