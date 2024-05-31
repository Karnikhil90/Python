import os

def get_name(file_name):
    if not os.path.exists(file_name):  # Check if the file doesn't exist
        return file_name

    directory, base_filename = os.path.split(file_name)
    filename, file_extension = os.path.splitext(base_filename)

    index = 1
    while True:
        new_filename = os.path.join(directory, f"{filename}({index}){file_extension}")
        if not os.path.exists(new_filename):
            return new_filename
        index += 1

# Usage
# file_name = "file.png"
# new_file_name = get_unique_file_name(file_name)
# print(new_file_name)
