import os
from PIL import Image, PngImagePlugin
from datetime import datetime

class FileConverter:
    def __init__(self, filepath=r'./', extension='jpg', output_dir='./Output_files'):
        self.filepath = filepath
        self.extension = extension
        self.output_dir = output_dir
        
    def save_with_unique_name(self, output_path):
        """Generate a unique filename if one already exists."""
        filename, ext = os.path.splitext(output_path)
        counter = 1
        while os.path.exists(output_path):
            output_path = f"{filename}({counter}){ext}"
            counter += 1
        return output_path
    
    def get_default_metadata(self):
        """Return default metadata including current time and a description."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return {
            "ConvertedTime": current_time,
            "Description": "Converted using karnikhil90's converter"
        }
    
    def image(self, output_format, metadata=None):
        # Load the image
        with Image.open(self.filepath) as img:
            # Split the filename and extension
            filename, _ = os.path.splitext(os.path.basename(self.filepath))
            # Set the output path
            output_path = os.path.join(self.output_dir, f"{filename}.{output_format}")
            
            # Ensure the output directory exists
            if not os.path.exists(self.output_dir):
                os.makedirs(self.output_dir)
                
            # Check and rename if the file already exists
            output_path = self.save_with_unique_name(output_path)
            
            # Use default metadata if none is provided
            if metadata is None:
                metadata = self.get_default_metadata()
            
            # Save the image with the provided or default metadata
            img_info = PngImagePlugin.PngInfo()
            for key, value in metadata.items():
                img_info.add_text(key, value)
            img.save(output_path, pnginfo=img_info)
            print(f"Image saved as {output_path}")

# Extension types for user input
extension_types = ['jpg', 'png', 'webp']

def clear_terminal():
    """Clear the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def test_file():
    while True:
        choice_lst = """
        Converting extensions one to another
            1. Convert image
            
        Enter 0 to exit.
        """
        user_input_choice = input(choice_lst + 'Enter your choice: ')
        
        if user_input_choice.strip() in ['0']:
            break
        
        if user_input_choice.strip() in ['1']:
            print(
        """
            \tType of extension
            1. jpg
            2. png
            3. webp
        """
            )
            user_input_path = input('Enter the image path: ')
            user_output_dir = input('Enter the output directory (default "./Output_files"): ').strip() or './Output_files'
            
            try:
                user_input_format = int(input('Enter the format number: '))
                if user_input_format in range(1, len(extension_types) + 1):
                    file_converter = FileConverter(user_input_path, extension_types[user_input_format - 1], user_output_dir)
                    file_converter.image(extension_types[user_input_format - 1])
                else:
                    print("Invalid format. Please try again.")
            except ValueError as e:
                print(f'Error [{e}]: Please select the correct choice only.')
        elif user_input_choice.strip() == 'clear':
            clear_terminal()
        else:
            print('Invalid choice. Please try again.')

# Run the test
test_file()
