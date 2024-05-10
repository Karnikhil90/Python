import os

def list_files(directory:str) -> list:
    # Check if the directory exists
    if not os.path.isdir(directory):
        print("Error: Directory not found")
        return
    
    # List all the files in the directory
    files = os.listdir(directory)
    
    # Create an empty list to store file names
    file_names = []
    
    # Add file names to the list
    for file_name in files:
        # Check if the current item is a file
        if os.path.isfile(os.path.join(directory, file_name)):
            file_names.append(file_name)
    
    return file_names

# file_list = list_files("./images/")

# Print the list of file names
# print("="*50)
print('\n'.join([name for name in list_files("./images/") ]))
# print("="*50)
# print('\n'.join([name for name in list(filter(lambda name: name[-4:] == ".png", file_list))]))
