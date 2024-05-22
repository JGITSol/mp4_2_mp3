import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip
import os

def convert_mp4_to_mp3(input_file, output_file):
    """ Convert MP4 to MP3 using moviepy """
    video_clip = VideoFileClip(input_file)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(output_file)
    audio_clip.close()
    video_clip.close()

def select_input_file():
    file_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
    if file_path:
        input_file_var.set(file_path)

def select_output_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
    if file_path:
        output_file_var.set(file_path)

def on_convert():
    input_file = input_file_var.get()
    output_file = output_file_var.get()

    if input_file and output_file:
        try:
            convert_mp4_to_mp3(input_file, output_file)
            messagebox.showinfo("Success", "Conversion successful!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showwarning("Warning", "Please select a valid MP4 file and specify an output MP3 file.")

# Create the main window
root = tk.Tk()
root.title("MP4 to MP3 Converter")

# Variables to store file paths
input_file_var = tk.StringVar()
output_file_var = tk.StringVar()

# Create and place widgets
tk.Label(root, text="Select an MP4 file:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=input_file_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_input_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Save MP3 as:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_file_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Save As", command=select_output_file).grid(row=1, column=2, padx=10, pady=10)

tk.Button(root, text="Convert", command=on_convert).grid(row=2, column=1, pady=20)
tk.Button(root, text="Exit", command=root.quit).grid(row=2, column=2, pady=20)

# Start the main event loop
root.mainloop()
