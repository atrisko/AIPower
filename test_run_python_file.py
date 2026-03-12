from functions.run_python_file import run_python_file

# Test 1
result = run_python_file("calculator", "main.py")
print("Test 1 - Running main.py without arguments:")
print(result)

# Test 2
result = run_python_file("calculator", "main.py", ["3 + 5"])
print("\nTest 2 - Running main.py with argument '3 + 5':")
print(result)

# Test 3
result = run_python_file("calculator", "tests.py")
print("\nTest 3 - Running tests.py without arguments:")
print(result)

# Test 4
result = run_python_file("calculator", "../main.py")
print("\nTest 4 - Running main.py from parent directory:")
print(result)

# Test 5
result = run_python_file("calculator", "nonexistent.py")
print("\nTest 5 - Running nonexistent.py:")
print(result)

# Test 6
result = run_python_file("calculator", "lorem.txt")
print("\nTest 6 - Running a non-Python file (lorem.txt):")
print(result)

