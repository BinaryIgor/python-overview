import os
import shutil
from os import path

file_content = """
Some text file
of multiple lines
"""

text_file_path = "/tmp/tmp_file.txt"
binary_file_path = "../files/forest.jpg"
dir_path = "/tmp/dir"

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

print()
print(f"Does {dir_path} exists?: {path.exists(dir_path)}")

if not path.exists(dir_path):
    os.mkdir(dir_path)

print(f"Files in: {dir_path} - {os.listdir(dir_path)}")

shutil.copy(text_file_path, path.join(dir_path, "txt_file.txt"))
shutil.copy(binary_file_path, path.join(dir_path, "binary_file.jpg"))

print(f"After copying files: {dir_path} - {os.listdir(dir_path)}")
