from functions.get_files_info import get_files_info

# Test with current directory
result = get_files_info("calculator", ".")
print("Result for current directory:")
print(result)

# Test with pgk subdirectory
result = get_files_info("calculator", "pkg")
print("Result for 'pkg' directory:")
print(result)

# Test with /bin directory
result = get_files_info("calculator", "/bin")
print("Result for '/bin' directory:")
print(result)

# Test with ../ directory
result = get_files_info("calculator", "../")
print("Result for '../' directory:")
print(result)

