# create a new directory
import os
new_directory="package"
os.mkdir(new_directory)
print(new_directory)

# listing files and directory
items=os.listdir("-")
print(items)

# joining paths
dir_name = "folder"
file_name = "file.txt"
full_path = os.path.join(os.getcwd(),dir_name,file_name)
print(full_path)

path="example.txt"
if os.path.exists(path):
    print(f"File {path} exists")
else:
    print(f"File {path} does not exist")

# checking if a path is a file or directory
import os

path="example.txt"
if os.path.isfile(path):
    print(f"the path {path} is file.")
elif os.path.isdir(path):
    print(f"the path {path} is a directory.")
else:
    print(f"the path {path} is neither a file nor a directory.")

#  getting the absolute path
relative_path="example.txt"
absolute_path=os.path.abspath(relative_path)
print(absolute_path)