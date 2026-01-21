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
            print("Downloading ffmpeg to home/ffmpeg folder...")
            import patoolib
            patoolib.extract_archive("https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-full.7z", outdir=ffmpeg_path)
    else:
        print("ERROR: Unable to Find FFMPEG. This isn't a Windows system so you will have to install it yourself.")
        
# Source - https://stackoverflow.com/a/16696317
# Posted by Roman Podlinov, modified by community. See post 'Timeline' for change history
# Retrieved 2026-01-21, License - CC BY-SA 4.0

def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                f.write(chunk)
    return local_filename