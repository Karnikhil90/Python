import json

# Function to add data to the JSON file and read also
class FileAccess:
    def __init__(self,json_file):
        self.json_file = json_file
    def add_data(self,recived_Data=None):
        json_file = self.json_file
        try:
            # Read existing data from the JSON file
            with open(json_file, 'r') as file:
                data = json.load(file)

            # Add new data to the existing data
            data.append(recived_Data)   # Write the updated data back to the JSON file
            with open(json_file, 'w') as file:
                json.dump(data, file, indent=2)
        except FileNotFoundError:
                                    # TODO: If the file doesn't exist..It creates a new 
            with open(json_file, 'x') as file:
                file.write('[]')
                print("File not found\nAnd Created a new file")
            self.add_data(recived_Data)
    def read_data(self) -> dict:
        try:
            with open(self.json_file, 'r') as file:
                readdata = json.load(file)
                return readdata
        except FileNotFoundError:
            with open(self.json_file, 'w') as file:
                file.write('[]')
                print("File not found\nAnd Created a new file")
                return []
        
        #*DEBUG
# Specify the JSON file and new data
# json_file_path = 'advLogin\\userdata.json'
# new_entry = {"name": input("Name: "), "password": input("Pass: ")}

# # Add the new entry to the JSON file
# obj = FileAccess(json_file_path)
# obj.add_data(new_entry)
# print(obj.read_data())