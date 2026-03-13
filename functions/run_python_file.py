import os
import subprocess
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file in a path relative to the working directory, with optional arguments, and captures its output",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to execute, relative to the working directory",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                description="Optional arguments to pass to the Python file",
                items=types.Schema(type=types.Type.STRING)
            ),
        },
        required=["file_path"],
    ),
)


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