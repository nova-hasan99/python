def return_anythings(a, b):
    num1 = a
    num2 = b
    sum = num1 + num2
    sub = num1 - num2
    div = round(num1 / num2, 2)
    mul = num1 * num2
    return[sum, sub, div, mul]
result = return_anythings(20, 30)
print(result)
print(" ")
#..............................................................

def multiNumber(*numbers):
    for number in numbers:
        print(number)
    print(" ")
multiNumber(20,252,456,98, 'hello', True)
#..............................................................

def multiObject(**object):
    for key, value in object.items():
        print(f'{key}: {value}')
    print(" ")

multiObject(
    name = 'hasan',
    age = 22,
    city = 'khulna'
)
#..............................................................

result = lambda x, y: x if x >= y else y         # lambda function
print(result(10, 20))
print(" ")
#..............................................................

import os             # for rename file name
# os.mkdir('test')                                  # for create folder
# os.rename('newFile', 'example.text')            # for change file name
# os.remove('example.text2')                      # for delete file

import zipfile
# with open('test3.txt', 'w') as file:
#     file.write()

# with zipfile.ZipFile('my.zip', 'w') as zip:    # make many files to zip 
#     zip.write('test.txt')
#     zip.write('test2.txt')
#     zip.write('test3.txt')

# with zipfile.ZipFile('my.zip', 'r') as unZip:    # extract zip
#     unZip.extractall()

import shutil
# shutil.make_archive('test.zip', 'zip', 'archive')b   # make folder to zip 
  
# with open("example.text2", "w") as file:  # for over all content together
#     file.write("Hello python")
#     print('success')



import re             # for manage latter

# Function to clean up multiple spaces and make case-insensitive search
def normalize_text(text):
    return re.sub(r'\s+', ' ', text).strip().lower()

# Function to search the content based on cleaned query
def search_content(search_query, content_lines):
    search_query = normalize_text(search_query)
    matching_lines = [line for line in content_lines if search_query in normalize_text(line)]
    return matching_lines

# Read the content from the file
with open("example.text", "r") as file:
    content_lines = file.readlines()

# Example search query
search_query = "hello p"  # or "Hello    ", or any variation

# Get the search results
results = search_content(search_query, content_lines)

# Print the search results
if results:
    for result in results:
        print(result.strip())
else:
    print(f"'{search_query}' not found")

    

        