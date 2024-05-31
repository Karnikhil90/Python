import os

class NameGenerator:
    def __init__(self, file_name):
        self.file_name = file_name

        if not os.path.exists(self.file_name):  # Check if the file doesn't exist
            self.unique_name = self.file_name
        else:
            directory, base_filename = os.path.split(self.file_name)
            filename, file_extension = os.path.splitext(base_filename)

            index = 1
            while True:
                new_filename = os.path.join(directory, f"{filename}({index}){file_extension}")
                if not os.path.exists(new_filename):
                    self.unique_name = new_filename
                    break
                index += 1

# Usage
# file_name = "file.png"
# generator = UniqueFileNameGenerator(file_name)
# print(generator.unique_name)
