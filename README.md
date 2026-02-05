# AudioVisual Helper

* ***This program, on windows, installs FFMPEG via WinGet for you.***

## TSA JUDGES INFO

The program's code is in `main`, the branch that (hopefully) you should be on. This contains all the changes we have made. Code is in the `src` folder.

## What is this?

This program has 2 functions:

1. Transcript Making from Video (via Whisper)
2. Black and White Screenshot (via opencv)

For video transcripts, the output will be a txt file in the same directory with the same name as the video but with a "_transcript" added in front of it. Whisper speech to text is done locally on your device with the 'base' model.

For screenshots, the image is (hopefully) deleted right after the image is closed. Program crashes may not delete the file, so you can delete it manually in the program directory.

## Usage

Make a virtual environment with `python -m venv .venv` and activate it (`./venv/Scripts/Activate.ps1` on Powershell, `source ./venv/bin/activate` for UNIX based systems).

Install the required packages with `pip install -r requirements.txt`. Run the program with `python ./src/main.py` and it should install ffmpeg for you.

Then, you can just see the commands in the terminal, but we will put it here for your reference:

* Control + Shift + Enter: Make a transcript.
* Control + \\: Show a black and white screenshot.

###### End of README
