import os

#todo: add sth about directory

file_content = """
Some text file
of multiple lines
"""

text_file_path = "/tmp/tmp_file.txt"
binary_file_path = "../files/forest.jpg"

print(os.getcwd())

with open(text_file_path, "w") as f:
    f.write(file_content)

with open(text_file_path, "r") as f:
    txt_content = f.read()
    print(f"File: {text_file_path} content:")
    print(type(txt_content))
    print(txt_content)

with open(binary_file_path, "rb") as f:
    content = f.read()
    print(type(content))
    print(len(content))
