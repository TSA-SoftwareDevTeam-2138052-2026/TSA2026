import requests # To get the file
import pathlib # to get home
import os # to check os name
import subprocess # to run ffmpeg to check

ffmpeg_path = pathlib.Path.home()._str + "/ffmpeg" if os.name == "nt" else "native"

def download_ffmpeg():
    if ffmpeg_path != "native":
        try:
            subprocess.run(['ffmpeg'])
        except FileNotFoundError:
            ffmpeg_download = requests.get("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z")
    else:
        print("ERROR: Unable to Find FFMPEG. This isn't a Windows system so ")