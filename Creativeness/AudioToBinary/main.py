import numpy as np
from pydub import AudioSegment
from pathlib import Path
import os, shutil, subprocess, struct

class AudioToFrequencyConverter:
    def __init__(self, input_file, output_dir=None):
        self.input_file = input_file
        self.output_dir = output_dir or str(Path.home() / "Music")
        self.sampling_rate = None
        self.audio_data = None
        self.frequency_data = []

    def check_ffmpeg(self):
        # Check if ffmpeg is available
        return shutil.which('ffmpeg') is not None

    def convert_to_wav(self):
        if not self.check_ffmpeg():
            raise RuntimeError("FFmpeg not found. Please ensure it is installed and added to your PATH.")
        
        # Convert audio file to WAV format using ffmpeg
        output_wav_file = str(Path(self.input_file).with_suffix('.wav'))
        command = [
            'ffmpeg', '-i', self.input_file,
            '-ar', '44100', '-ac', '1',  # 44.1 kHz, mono
            output_wav_file
        ]
        print(f"Running command: {' '.join(command)}")  # Debug print

        try:
            result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(f"FFmpeg output: {result.stdout}")  # Print standard output
            print(f"FFmpeg errors: {result.stderr}")   # Print error output
        except subprocess.CalledProcessError as e:
            print(f"FFmpeg conversion failed: {e.stderr}")  # Print error output
            raise RuntimeError(f"FFmpeg conversion failed: {e}")
        return output_wav_file

    def load_audio(self):
        wav_file = self.convert_to_wav()
        # Load the audio file using pydub
        audio_segment = AudioSegment.from_wav(wav_file)
        self.sampling_rate = audio_segment.frame_rate
        self.audio_data = np.array(audio_segment.get_array_of_samples())
        print(f"Loaded audio file: {self.input_file}")

    def extract_frequencies(self):
        if self.audio_data is None:
            raise RuntimeError("Audio data is not loaded. Please run load_audio() first.")

        # Perform Fourier Transform to extract frequency content
        n = len(self.audio_data)
        k = np.arange(n)
        T = n / self.sampling_rate
        frq = k / T 
        frq = frq[range(n // 2)] 
        Y = np.fft.fft(self.audio_data) / n
        Y = Y[range(n // 2)]

        magnitude = np.abs(Y)
        self.frequency_data = [(frq[i], magnitude[i]) for i in range(len(frq)) if magnitude[i] > 0.1]

    def get_unique_filename(self, base_name):
        """
        Generates a unique file name by appending numbers if the file already exists.
        Example: If 'music.bin' exists, it will generate 'music(1).bin', 'music(2).bin', etc.
        """
        base_path = Path(self.output_dir) / f"{base_name}.bin"
        if not base_path.exists():
            return base_path

        counter = 1
        while True:
            new_name = Path(self.output_dir) / f"{base_name}({counter}).bin"
            if not new_name.exists():
                return new_name
            counter += 1

    def save_to_bin(self):
        if not self.frequency_data:
            raise RuntimeError("Frequency data is empty. Please run extract_frequencies() first.")

        base_name = Path(self.input_file).stem  # Use the input file name as the base name
        unique_filename = self.get_unique_filename(base_name)

        # Create output directory if it doesn't exist
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)

        # Save the frequency data as a .bin file
        with open(unique_filename, 'wb') as f:
            for freq, mag in self.frequency_data:
                # Write the frequency and magnitude as floats in binary format
                f.write(struct.pack('ff', freq, mag))

        print(f"Frequency data saved to: {unique_filename}")

    def process(self):
        # Complete process: load audio, extract frequencies, and save to file
        self.load_audio()
        self.extract_frequencies()
        self.save_to_bin()

def convert_directory_to_bin(input_dir, output_dir):
    # Get all audio files from the specified directory
    audio_files = [f for f in Path(input_dir).iterdir() if f.suffix.lower() in ['.mp3', '.wav', '.flac', '.m4a', '.webm']]
    if not audio_files:
        print("No audio files found in the directory.")
        return

    print(f"Found {len(audio_files)} audio files. Starting conversion...")
    for audio_file in audio_files:
        converter = AudioToFrequencyConverter(str(audio_file), output_dir)
        converter.process()

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    while True:
        print("\nOptions:")
        print("1. Convert a single audio file to .bin")
        print("2. Convert all audio files from a directory to .bin")
        print("3. Clear terminal")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            input_audio_file = input("Enter the path of the audio file: ")
            default_output_dir = str(Path.home() / "Music")
            custom_output_dir = input(f"Enter the output directory (press Enter to use default '{default_output_dir}'): ").strip() or default_output_dir
            converter = AudioToFrequencyConverter(input_audio_file, custom_output_dir)
            converter.process()

        elif choice == "2":
            input_dir = input("Enter the directory containing audio files: ")
            default_output_dir = str(Path.home() / "Music")
            custom_output_dir = input(f"Enter the output directory (press Enter to use default '{default_output_dir}'): ").strip() or default_output_dir
            convert_directory_to_bin(input_dir, custom_output_dir)

        elif choice == "3":
            clear_terminal()

        elif choice == "4":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
