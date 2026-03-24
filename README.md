# AudioVisual Helper

* ***This program, on windows, installs FFMPEG via WinGet for you.***

## TSA JUDGES INFO

The program's code is in `main`, the branch that (hopefully) you should be on. This contains all the changes we have made. Code is in the `src` folder.

Our team ID is SDHS~2138-1. This ID is also in credits.md, which is shown under Help --> Credits...

## What is this?

This program has 2 functions:

1. Captions from Video (via Whisper)
2. Contrast-enhancing Screenshot (via opencv)
3. Magnification (via GraphicsView)

Captions will automatically be saved with the same filename as the video as a VTT format. This should ensure auto-discovery by most modern media players (Windows Media Player, VLC, etc.)

For screenshots and magnification, the image is (hopefully) deleted right after the image is closed. Program crashes may not delete the file, so you can delete it manually in the program's data directory located at:

`$HOME/.audiovisualhelp/screenshot.png` on Linux-based systems (expands to `/home/USER/.audiovisualhelp/screenshot.png`)

or

`%USERPROFILE%\.audiovisualhelp\screenshot.png` on Windows-based systems (expands to `C:\Users\USER\.audiovisualhelp\screenshot.png`)

## Usage

### Via Release

Download the release zip file, unzip it, and run the executable file within the zip file. It should be on the top level of the zip file, so make sure you extract it to its own directory.

Additionally, you can make a shortcut to it on your desktop.

### Manually

Make a virtual environment with `python -m venv .venv` and activate it (`./venv/Scripts/Activate.ps1` on Powershell, `source ./venv/bin/activate` for UNIX based systems).

Install the required packages with `pip install -r requirements.txt`. Run the program with `python ./src/app.py` and it should open up the main window.

There is one convenience shortcut for your pleasure:

* Control + \\: Show a contrast-enhanced screenshot.
