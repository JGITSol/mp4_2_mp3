import PySimpleGUI as sg
from moviepy.editor import VideoFileClip
import os

"""
Tested manually, works, but PYSG is currently pay to use, or horrible trial banner on.
    """



def convert_mp4_to_mp3(input_file, output_file):
    """ Convert MP4 to MP3 using moviepy """
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file)
    audio_clip.close()
    video_clip.close()

# Define the window's contents
layout = [
    [sg.Text("Select an MP4 file:")],
    [sg.Input(key="-FILE-"), sg.FileBrowse(file_types=(("MP4 Files", "*.mp4"),))],
    [sg.Text("Save MP3 as:"), sg.Input(key="-SAVEAS-"), sg.SaveAs(file_types=(("MP3 Files", "*.mp3"),))],
    [sg.Button("Convert"), sg.Button("Exit")]
]

# Create the window
window = sg.Window("MP4 to MP3 Converter", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    if event == "Convert":
        mp4_file = values["-FILE-"]
        mp3_file = values["-SAVEAS-"]

        if mp4_file and mp3_file:
            try:
                convert_mp4_to_mp3(mp4_file, mp3_file)
                sg.popup("Conversion successful!", title="Success")
            except Exception as e:
                sg.popup(f"An error occurred: {e}", title="Error")
        else:
            sg.popup("Please select a valid MP4 file and specify an output MP3 file.", title="Error")

# Close the window
window.close()
