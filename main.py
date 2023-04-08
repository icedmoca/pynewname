import os
import tkinter as tk
from tkinter import filedialog, messagebox

def browse_dir():
    global selected_dir
    selected_dir = filedialog.askdirectory()
    if selected_dir:
        dir_label.config(text=selected_dir)

def rename_files():
    if not selected_dir:
        messagebox.showwarning("Warning", "Please select a directory")
        return
    old_ext = old_ext_entry.get().strip()
    new_ext = new_ext_entry.get().strip()
    if not old_ext or not new_ext:
        messagebox.showwarning("Warning", "Please enter old and new extensions")
        return
    if old_ext[0] != '.':
        old_ext = '.' + old_ext
    if new_ext[0] != '.':
        new_ext = '.' + new_ext
    for filename in os.listdir(selected_dir):
        if filename.endswith(old_ext):
            base_name = os.path.splitext(filename)[0]
            new_name = base_name + new_ext
            os.rename(os.path.join(selected_dir, filename), os.path.join(selected_dir, new_name))
    messagebox.showinfo("Success", "File extensions have been changed")

window = tk.Tk()
window.geometry("600x300")
window.title("File Extension Changer")

browse_button = tk.Button(window, text="Select Directory", command=browse_dir)
browse_button.pack(pady=10)

dir_label = tk.Label(window, text="No directory selected")
dir_label.pack()

old_ext_label = tk.Label(window, text="Enter old extension:")
old_ext_label.pack(pady=10)

old_ext_entry = tk.Entry(window)
old_ext_entry.pack()

new_ext_label = tk.Label(window, text="Enter new extension:")
new_ext_label.pack(pady=10)

new_ext_entry = tk.Entry(window)
new_ext_entry.pack()

run_button = tk.Button(window, text="Run", command=rename_files)
run_button.pack(pady=10)

window.mainloop()
