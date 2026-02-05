import requests # To get the file
import pathlib # to get home
import os # to check os name
import subprocess # to run ffmpeg to check
import pathlib # to manage paths
import ffmpeg

class ffmpeg_manager:
    def __init__(self):
        pass
    
    ffmpeg_path = pathlib.Path.home()._str + "/ffmpeg" if os.name == "nt" else "native"
    
    @classmethod
    def download_ffmpeg(cls) -> None:
        if cls.ffmpeg_path != "native":
            try:
                subprocess.run(['ffmpeg', '-version'],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)
                print("FOUND!")
            except FileNotFoundError:
                print("FFMPEG not found. Installing via winget...")
                try:
                    subprocess.run(['winget', 'install', 'ffmpeg', '--accept-source-agreements', '--accept-package-agreements'])
                except FileNotFoundError:
                    print("ERROR. CANNOT FIND WINGET.")
                    print("ABORTING...")
        else:
            print("ERROR: Unable to Find FFMPEG. This isn't a Windows system so you will have to install it yourself.")
    
    @classmethod
    def remove_video(cls, video_path: str) -> str:
        video_path = video_path.strip("\"\'")
        video_path_pathlib = pathlib.Path.resolve(pathlib.Path(video_path))
        output = video_path_pathlib.parent._str + "/" + video_path_pathlib.name.split(".")[0] + ".wav"
        video = ffmpeg.input(video_path_pathlib).output(output).overwrite_output().run()
        return output
    