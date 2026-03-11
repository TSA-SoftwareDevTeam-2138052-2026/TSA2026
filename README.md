# AudioVisual Helper

* ***This program, on windows, installs FFMPEG via WinGet for you.***

## TSA JUDGES INFO

The program's code is in `main`, the branch that (hopefully) you should be on. This contains all the changes we have made. Code is in the `src` folder.

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

Make a virtual environment with `python -m venv .venv` and activate it (`./venv/Scripts/Activate.ps1` on Powershell, `source ./venv/bin/activate` for UNIX based systems).

Install the required packages with `pip install -r requirements.txt`. Run the program with `python ./src/app.py` and it should open up the main window.

Some convinience shortcuts for your pleasure:

* Control + Shift + Enter: Make a transcript.
* Control + \\: Show a black and white screenshot.
