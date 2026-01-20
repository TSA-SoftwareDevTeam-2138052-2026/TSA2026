import requests # To get the file
import pathlib # to get home
import os # to check directory

ffmpeg_path = pathlib.Path.home()._str + "/ffmpeg"

def download_ffmpeg():
    while True:
        if os.name == 'nt':
            if pathlib.Path.exists(ffmpeg_path):
                for item in os.scandir(ffmpeg_path):
                    if item.name.split(".")[0].lower() == "ffmpeg":
                        return "FFMPEG INSTALLED"

                
            ffmpeg_download = requests.get("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z")