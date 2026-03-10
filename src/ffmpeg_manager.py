import requests # To get the file
import pathlib # to get home
import os # to check os name
import subprocess # to run ffmpeg to check
import pathlib # to manage paths

class ffmpeg_manager:
    def __init__(self):
        pass
    
    ffmpeg_path = pathlib.Path.home()._str + "/ffmpeg" if os.name == "nt" else "native"
    
    @classmethod
    def download_ffmpeg(cls) -> None:
        if cls.ffmpeg_path != "native":
            try:
                subprocess.run(['ffmpeg', '-version'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
            except FileNotFoundError:
                try:
                    subprocess.run(['winget', 'install', 'ffmpeg', '--accept-source-agreements', '--accept-package-agreements'])
                except FileNotFoundError:
                    print("ERROR. CANNOT FIND WINGET.")
                    print("ABORTING...")
        else:
            raise(FFmpegNotFoundException("ERROR: Unable to Find FFMPEG. This isn't a Windows system so you will have to install it yourself."))


class FFmpegNotFoundException(Exception):
    def __init__(self, *args):
        super().__init__(*args)
    