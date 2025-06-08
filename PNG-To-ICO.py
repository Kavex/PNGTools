import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

def select_file():
    # Open file dialog to select a PNG file
    file_path = filedialog.askopenfilename(
        filetypes=[("PNG Files", "*.png")],
        title="Select a PNG file"
    )
    if file_path:
        entry_input.delete(0, tk.END)
        entry_input.insert(0, file_path)

def convert():
    # Get the selected file path
    input_file = entry_input.get()
    if not input_file:
        messagebox.showerror("Error", "Please select a PNG file to convert.")
        return

    # Define output file path (same name as input but with .ico extension)
    base, _ = os.path.splitext(input_file)
    output_file = base + ".ico"
    
    # Use the scale filter to resize the image to 256x256 before conversion
    command = ["ffmpeg", "-y", "-i", input_file, "-vf", "scale=256:256", output_file]
    
    try:
        subprocess.run(command, check=True)
        messagebox.showinfo("Success", f"Conversion successful!\nOutput: {output_file}")
    except subprocess.CalledProcessError as e:
        messagebox.showerror("Conversion Failed", f"Error during conversion:\n{e}")
    except FileNotFoundError:
        messagebox.showerror("Error", "ffmpeg not found. Please ensure it is installed and in your PATH.")

# Setup the main window
root = tk.Tk()
root.title("PNG to ICO Converter (using ffmpeg)")

# Create and position widgets
label = tk.Label(root, text="Select PNG file:")
label.pack(padx=10, pady=5)

entry_input = tk.Entry(root, width=50)
entry_input.pack(padx=10, pady=5)

button_browse = tk.Button(root, text="Browse", command=select_file)
button_browse.pack(padx=10, pady=5)

button_convert = tk.Button(root, text="Convert to ICO", command=convert)
button_convert.pack(padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
