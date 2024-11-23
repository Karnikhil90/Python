"""
The function `map_directory_to_extensions` converts a string input into a dictionary, 
mapping a directory name to a list of file extensions.

* in simple , From str to dictionary. key is the directory's name and value is file types
Example:
    user_input: "mydoc:txt,pdf" 
    
    Output: {'mydoc': ['txt', 'pdf']}
"""


def map_directory_to_extensions(user_input : str) -> dict[str:list[str]]:
    directory, file_types = user_input.split(':')
    return {directory: file_types.split(',')}
print(map_directory_to_extensions("mydoc:txt,pdf"))