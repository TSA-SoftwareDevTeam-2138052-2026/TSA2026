import requests # To get the file
import pathlib # to get home
import os # to check os name
import subprocess # to run ffmpeg to check
import pathlib # to manage paths

class ffmpeg_manager():
    def __init__(self):
        pass
    
    ffmpeg_path = pathlib.Path.home()._str + "/ffmpeg" if os.name == "nt" else "native"
    
    @classmethod
    def download_ffmpeg(cls) -> str:
        if cls.ffmpeg_path != "native":
            try:
                subprocess.run([f'{cls.ffmpeg_path}/bin/ffmpeg.exe'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
                print("FOUND!")
                cls.ffmpeg_path = cls.ffmpeg_path + "/bin/ffmpeg.exe"
                return cls.ffmpeg_path
            except FileNotFoundError:
                print("Downloading ffmpeg to home/ffmpeg folder...")
                import patoolib
                path = cls._download_file("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z")
                patoolib.extract_archive(path, outdir="temp", verbosity=-1)
                os.remove(path)
                print("Downloaded")
                print("Final touches...")
                current_dir = ""
                for dirpath, dirnames, filenames in os.walk("temp"):
                    current_dir = dirnames[0]
                    break
                import shutil
                shutil.move(f"temp/{current_dir}", cls.ffmpeg_path)
                print("DONE!")
                os.remove(path)
                cls.ffmpeg_path = cls.ffmpeg_path + "/bin/ffmpeg.exe"
                return cls.ffmpeg_path
        else:
            print("ERROR: Unable to Find FFMPEG. This isn't a Windows system so you will have to install it yourself.")
            return ""
    
    @classmethod
    def remove_video(cls, video_path: str) -> str:
        video_path = video_path.strip("\"\'")
        video_path_pathlib = pathlib.Path.resolve(pathlib.Path(video_path))
        output = video_path_pathlib.parent._str + "/" + video_path_pathlib.name.split(".")[0] + ".wav"
        subprocess.run([f'{cls.ffmpeg_path}', '-i', video_path_pathlib, output])
        return output
    
    # Source - https://stackoverflow.com/a/16696317
    # Posted by Roman Podlinov, modified by community. See post 'Timeline' for change history
    # Retrieved 2026-01-21, License - CC BY-SA 4.0
    @classmethod
    def _download_file(cls, url: str) -> str:
        local_filename = url.split('/')[-1]
        # NOTE the stream=True parameter below
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                chunks = 0
                print("Downloaded chunk:")
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    f.write(chunk)
                    print(str(chunks) + "\r", end='')
                    chunks += 1
        print("\n")
        return local_filename