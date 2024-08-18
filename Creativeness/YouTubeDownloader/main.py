import os
import yt_dlp

class YouTubeDownloader:
    def __init__(self):
        self.links = []
        self.download_path = os.path.join(os.getcwd(), 'downloads')
        self.file_location = os.getcwd()

    def get_file_location(self):
        print("\nEnter the path of your 'yt_links.txt' file (Press Enter to use the current directory):")
        user_input = input(f"[Default: {self.file_location}]: ").strip()
        if user_input:
            self.file_location = user_input

    def read_links(self):
        try:
            file_path = os.path.join(self.file_location, "yt_links.txt")
            with open(file_path, "r") as file:
                self.links = [line.strip() for line in file if line.strip()]
            if not self.links:
                print("No valid links found in the file.")
                exit()
        except FileNotFoundError:
            print("File not found. Make sure 'yt_links.txt' exists in the specified location.")
            exit()

    def get_download_path(self):
        print(f"\nWhere do you want to save the files? (Press Enter to use the default directory '{self.download_path}'):")
        user_input = input(f"[Default: {self.download_path}]: ").strip()
        if user_input:
            self.download_path = user_input
        os.makedirs(self.download_path, exist_ok=True)

    def choose_format(self):
        print("\nWhat format do you want to download?")
        print("1. Audio Only (MP3)")
        print("2. Video Only")
        print("3. Both Video and Audio")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            return "audio"
        elif choice == "2":
            return "video"
        elif choice == "3":
            return "both"
        else:
            print("Invalid option selected. Defaulting to 'audio'.")
            return "audio"

    def download_videos(self):
        format_choice = self.choose_format()

        for link in self.links:
            print(f"\nDownloading: {link}")
            try:
                ydl_opts = {}
                if format_choice == "audio":
                    ydl_opts = {
                        'format': 'bestaudio/best',
                        'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                        'postprocessors': [{
                            'key': 'FFmpegExtractAudio',
                            'preferredcodec': 'mp3',
                            'preferredquality': '192',
                        }],
                    }
                elif format_choice == "video":
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio',
                        'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                    }
                elif format_choice == "both":
                    ydl_opts = {
                        'format': 'bestvideo+bestaudio',
                        'outtmpl': os.path.join(self.download_path, '%(title)s.%(ext)s'),
                        'merge_output_format': 'mp4',
                    }

                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([link])

            except Exception as e:
                print(f"Failed to download {link}: {e}")

    def run(self):
        self.get_file_location()
        self.read_links()
        self.get_download_path()
        self.download_videos()

if __name__ == "__main__":
    downloader = YouTubeDownloader()
    downloader.run()
