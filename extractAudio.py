import os
import subprocess

class AudioExtractor:
    def __init__(self, output_dir="cache", audio_format="mp3"):
        self.output_dir = output_dir
        self.audio_format = audio_format
        
        os.makedirs(output_dir, exist_ok=True) # Ensure the output directory exists


    def download_audio(self, video_url): 
        
        output_file = os.path.join(self.output_dir, f"audio.{self.audio_format}")
        
        # yt-dlp command to download and convert to audio
        command = [
            "yt-dlp",
            "-x",  # Extract audio
            "--audio-format", self.audio_format,  
            "--output", output_file,  
            video_url
        ]
        
        print(f"Downloading and converting audio from {video_url}...")
        subprocess.run(command, check=True)
        print(f"Audio saved at: {output_file}")
        return output_file

    def set_audio_format(self, audio_format):
        """
        Updates the desired audio format.

        Parameters:
            audio_format (str): New desired audio format (e.g., 'mp3', 'wav').
        """
        self.audio_format = audio_format
        print(f"Audio format set to: {self.audio_format}")
