import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def select_images():
    files = filedialog.askopenfilenames(
        title="Select Images",
        filetypes=[("Image Files", "*.jpg *.jpeg *.webp *.bmp *.gif *.tiff *.tif *.heic *.png")]
    )
    if files:
        image_paths.clear()
        image_paths.extend(files)
        status_label.config(text=f"{len(files)} image(s) selected.")

def select_output_folder():
    folder = filedialog.askdirectory(title="Select Output Folder")
    if folder:
        output_folder.set(folder)
        status_label.config(text=f"Output folder: {folder}")

def convert_images():
    if not image_paths:
        messagebox.showwarning("No Images", "Please select image files to convert.")
        return
    if not output_folder.get():
        messagebox.showwarning("No Output Folder", "Please select an output folder.")
        return

    for img_path in image_paths:
        try:
            with Image.open(img_path) as img:
                base = os.path.basename(img_path)
                filename = os.path.splitext(base)[0] + ".png"
                output_path = os.path.join(output_folder.get(), filename)
                img.save(output_path, format="PNG", optimize=True, compress_level=(100 - quality_slider.get()) // 10)
        except Exception as e:
            messagebox.showerror("Conversion Error", f"Failed to convert {img_path}:\n{e}")

    messagebox.showinfo("Done", "Conversion to PNG completed.")

# GUI setup
root = tk.Tk()
root.title("Image to PNG Converter")

image_paths = []
output_folder = tk.StringVar()

tk.Label(root, text="1. Select image files:").pack()
tk.Button(root, text="Select Images", command=select_images).pack(pady=5)

tk.Label(root, text="2. Select output folder:").pack()
tk.Button(root, text="Select Folder", command=select_output_folder).pack(pady=5)

tk.Label(root, text="3. Quality / Compression Level:").pack()
quality_slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
quality_slider.set(90)
quality_slider.pack(pady=5)

tk.Button(root, text="Convert to PNG", command=convert_images).pack(pady=10)

status_label = tk.Label(root, text="Select images and folder to begin.")
status_label.pack()

root.mainloop()
