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
            #try:
            #    subprocess.run([f'{cls.ffmpeg_path}/bin/ffmpeg.exe'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
            #    print("FOUND!")
            #    cls.ffmpeg_path = cls.ffmpeg_path + "/bin/ffmpeg.exe"
            #    return cls.ffmpeg_path
            #except FileNotFoundError:
            #    print("Downloading ffmpeg to home/ffmpeg folder...")
            #    import patoolib
            #    path = cls._download_file("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z")
            #    patoolib.extract_archive(path, outdir="temp", verbosity=-1)
            #    os.remove(path)
            #    print("Downloaded")
            #    print("Final touches...")
            #    current_dir = ""
            #    for dirpath, dirnames, filenames in os.walk("temp"):
            #        current_dir = dirnames[0]
            #        break
            #    import shutil
            #    shutil.move(f"temp/{current_dir}", cls.ffmpeg_path)
            #    print("DONE!")
            #    os.remove(path)
            #    cls.ffmpeg_path = cls.ffmpeg_path + "/bin/ffmpeg.exe"
            #    return cls.ffmpeg_path
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
    