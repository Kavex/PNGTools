import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image

def convert_webp_to_png(folder_path):
    converted = 0
    failed = []

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".webp"):
            webp_path = os.path.join(folder_path, filename)
            png_filename = os.path.splitext(filename)[0] + ".png"
            png_path = os.path.join(folder_path, png_filename)

            try:
                with Image.open(webp_path) as img:
                    img.save(png_path, "PNG")
                    converted += 1
            except Exception as e:
                failed.append((filename, str(e)))

    return converted, failed

def select_folder():
    folder_selected = filedialog.askdirectory()
    if not folder_selected:
        return

    converted, failed = convert_webp_to_png(folder_selected)

    msg = f"✅ Converted {converted} file(s) to PNG."
    if failed:
        msg += f"\n⚠️ {len(failed)} file(s) failed:\n"
        msg += "\n".join([f"- {name}: {err}" for name, err in failed])

    messagebox.showinfo("Conversion Complete", msg)

# GUI setup
root = tk.Tk()
root.title("WebP to PNG Converter")
root.geometry("350x150")

label = tk.Label(root, text="Select a folder to convert all .webp to .png", pady=10)
label.pack()

btn = tk.Button(root, text="Select Folder & Convert", command=select_folder, padx=10, pady=5)
btn.pack()

root.mainloop()
