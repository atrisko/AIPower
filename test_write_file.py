from functions.write_file import write_file


# Test 1
result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
print("Result for writing to 'lorem.txt':")
print(result)

# Test 2
result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
print("Result for writing to 'pkg/morelorem.txt':")
print(result)

# Test 3
result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
print("Result for writing to '/tmp/temp.txt':")
print(result)

