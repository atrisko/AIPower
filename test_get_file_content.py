from functions.get_file_content import get_file_content


# Test with lorem.txt file
result = get_file_content("calculator", "lorem.txt")
print("Result for 'lorem.txt':")
print(result)


#Test with main.py file
result = get_file_content("calculator", "main.py")
print("Result for 'main.py':")
print(result)


# Test with pkg/calculator.py file
result = get_file_content("calculator", "pkg/calculator.py")
print("Result for 'pkg/calculator.py':")
print(result)


# Test with /bin/cat:
result = get_file_content("calculator", "/bin/cat")
print("Result for '/bin/cat':")
print(result)


# Test with pkg/does_not_exist.py file
result = get_file_content("calculator", "pkg/does_not_exist.py")
print("Result for 'pkg/does_not_exist.py':")
print(result)