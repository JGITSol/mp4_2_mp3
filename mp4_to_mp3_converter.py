import tkinter as tk
from tkinter import filedialog, messagebox
from moviepy.editor import VideoFileClip

"""Refactored, manually tested"""

class MP4toMP3Converter:
    def __init__(self, root):
        self.root = root
        self.setup_ui()

    def setup_ui(self):
        """ Set up the user interface for the converter """
        self.root.title("MP4 to MP3 Converter")

        # Variables to store file paths
        self.input_file_var = tk.StringVar()
        self.output_file_var = tk.StringVar()

        # Create and place widgets
        tk.Label(self.root, text="Select an MP4 file:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.input_file_var, width=50).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.select_input_file).grid(row=0, column=2, padx=10, pady=10)

        tk.Label(self.root, text="Save MP3 as:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.output_file_var, width=50).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Save As", command=self.select_output_file).grid(row=1, column=2, padx=10, pady=10)

        tk.Button(self.root, text="Convert", command=self.on_convert).grid(row=2, column=1, pady=20)
        tk.Button(self.root, text="Exit", command=self.root.quit).grid(row=2, column=2, pady=20)

    def select_input_file(self):
        """ Open a dialog to select the input MP4 file """
        file_path = filedialog.askopenfilename(filetypes=[("MP4 Files", "*.mp4")])
        if file_path:
            self.input_file_var.set(file_path)

    def select_output_file(self):
        """ Open a dialog to select the output MP3 file """
        file_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])
        if file_path:
            self.output_file_var.set(file_path)

    def on_convert(self):
        """ Handle the conversion process """
        input_file = self.input_file_var.get()
        output_file = self.output_file_var.get()

        if input_file and output_file:
            try:
                self.convert_mp4_to_mp3(input_file, output_file)
                messagebox.showinfo("Success", f"Conversion successful! Saved as {output_file}")
            except FileNotFoundError:
                messagebox.showerror("Error", "The specified file was not found.")
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred during conversion: {e}")
        else:
            messagebox.showwarning("Warning", "Please select valid input and output files.")

    @staticmethod
    def convert_mp4_to_mp3(input_file, output_file):
        """ Convert MP4 to MP3 using moviepy """
        video_clip = VideoFileClip(input_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(output_file)
        audio_clip.close()
        video_clip.close()

# Create the main window and start the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MP4toMP3Converter(root)
    root.mainloop()
