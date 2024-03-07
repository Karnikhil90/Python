import os
import subprocess

try:
    from moviepy.video.io.VideoFileClip import VideoFileClip
except ImportError:
    print("The 'moviepy' module is not installed. Installing now...")
    try:
        subprocess.run(['pip', 'install', 'moviepy'])
        from moviepy.video.io.VideoFileClip import VideoFileClip
    except Exception as e:
        print(f"Error installing 'moviepy': {e}")
        exit(1)

try:
    import ffmpeg
except ImportError:
    print("The 'ffmpeg' module is not installed. Installing now...")
    try:
        subprocess.run(['pip', 'install', 'ffmpeg-python'])
        import ffmpeg
    except Exception as e:
        print(f"Error installing 'ffmpeg': {e}")
        exit(1)

counter = False

def convert_mp4_to_mp3(input_folder, output_folder):
    global counter
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Loop through all .mp4 files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp4"):
            input_file = os.path.join(input_folder, filename)
            
            # Generate the corresponding output file name with .mp3 extension
            output_file = os.path.join(output_folder, os.path.splitext(filename)[0] + ".mp3")

            # Check if the output file already exists, and skip the conversion if it does
            if os.path.exists(output_file):
                print(f"\n{'=' * 20}")
                print(f"Skipping {filename} as {output_file} already exists.")
                continue
            print(f"\n{'=' * 20}")

            # Convert the current .mp4 file to .mp3
            video_clip = VideoFileClip(input_file)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_file)
            video_clip.close()

            # Print a message indicating successful conversion
            print(f"Conversion of {filename} completed.")
            counter = True

# Replace 'input_folder' and 'output_folder' with your actual input and output folder paths
try:
    convert_mp4_to_mp3('input_folder', 'output_folder')
except Exception as e:
    print(f"An error occurred: {e}")

if counter:
    print(f"\n{'=' * 20}")
    print("\n\tFile conversion completed")
    print(f"\n{'=' * 20}")
