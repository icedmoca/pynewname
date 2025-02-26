import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.font import Font


def rename_files():
    old_ext = old_ext_entry.get().strip()
    new_ext = new_ext_entry.get().strip()

    if add_num_checkbox_var.get():
        try:
            num = int(starting_num_entry.get().strip())
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid starting number.")
            return
    else:
        num = None

    if not os.path.exists(directory_path.get()):
        messagebox.showerror("Error", "Invalid directory path.")
        return

    count = 0

    for file in os.listdir(directory_path.get()):
        if file.endswith(old_ext):
            filename, ext = os.path.splitext(file)
            new_filename = filename + "_" + str(num) if num else filename
            new_filename += "." + new_ext if new_ext else ext

            os.rename(
                os.path.join(directory_path.get(), file),
                os.path.join(directory_path.get(), new_filename)
            )
            count += 1
            num += 1 if num is not None else 0

    messagebox.showinfo("Success", f"Successfully renamed {count} files.")


def select_directory():
    dir_path = filedialog.askdirectory()
    if dir_path:
        directory_path.set(dir_path)


def toggle_num_textbox():
    if add_num_checkbox_var.get():
        starting_num_entry.config(state="normal")
        starting_num_label.config(foreground="#1E88E5")
    else:
        starting_num_entry.config(state="disabled")
        starting_num_label.config(foreground="#757575")


def create_tooltip(widget, text):
    def enter(event):
        x, y, _, _ = widget.bbox("insert")
        x += widget.winfo_rootx() + 25
        y += widget.winfo_rooty() + 25
        
        # Create a toplevel window
        tooltip = tk.Toplevel(widget)
        tooltip.wm_overrideredirect(True)
        tooltip.wm_geometry(f"+{x}+{y}")
        tooltip.attributes('-alpha', 0.9)  # Transparency
        
        label = tk.Label(tooltip, text=text, justify='left',
                         background="#424242", foreground="white",
                         relief="solid", borderwidth=1,
                         font=("Segoe UI", 9, "normal"), padx=5, pady=2)
        label.pack(ipadx=1)
        
        widget.tooltip = tooltip
        
    def leave(event):
        if hasattr(widget, "tooltip"):
            widget.tooltip.destroy()
            
    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)


# Create the main window with a modern look
window = tk.Tk()
window.geometry("800x600")
window.title("File Renamer")
window.configure(bg="#F5F5F5")  # Light gray background

# Set custom fonts
title_font = Font(family="Segoe UI", size=16, weight="bold")
label_font = Font(family="Segoe UI", size=10)
button_font = Font(family="Segoe UI", size=10, weight="bold")

# Set up variables
directory_path = tk.StringVar()
add_num_checkbox_var = tk.BooleanVar()

# Create a frame for the title
title_frame = tk.Frame(window, bg="#F5F5F5")
title_frame.pack(fill="x", padx=20, pady=20)

title_label = tk.Label(title_frame, text="File Renamer", font=title_font, bg="#F5F5F5", fg="#1E88E5")
title_label.pack()

# Create a main frame with some padding
main_frame = tk.Frame(window, bg="#F5F5F5", padx=20, pady=10)
main_frame.pack(fill="both", expand=True)

# Directory selection section
dir_frame = tk.LabelFrame(main_frame, text="Directory Selection", font=label_font, bg="#F5F5F5", fg="#1E88E5", padx=10, pady=10)
dir_frame.pack(fill="x", pady=10)

dir_inner_frame = tk.Frame(dir_frame, bg="#F5F5F5")
dir_inner_frame.pack(fill="x")

select_dir_button = tk.Button(
    dir_inner_frame, 
    text="Select Directory", 
    command=select_directory,
    bg="#1E88E5",
    fg="white",
    font=button_font,
    relief="flat",
    padx=10
)
select_dir_button.grid(column=0, row=0, padx=10, pady=10)

directory_entry = tk.Entry(dir_inner_frame, textvariable=directory_path, width=50, font=label_font)
directory_entry.grid(column=1, row=0, padx=10, pady=10, sticky="ew")

# Extension settings section
ext_frame = tk.LabelFrame(main_frame, text="Extension Settings", font=label_font, bg="#F5F5F5", fg="#1E88E5", padx=10, pady=10)
ext_frame.pack(fill="x", pady=10)

ext_inner_frame = tk.Frame(ext_frame, bg="#F5F5F5")
ext_inner_frame.pack(fill="x")

old_ext_label = tk.Label(ext_inner_frame, text="Current extension:", font=label_font, bg="#F5F5F5", fg="#424242")
old_ext_label.grid(column=0, row=0, padx=10, pady=10, sticky="w")

old_ext_entry = tk.Entry(ext_inner_frame, font=label_font, width=20)
old_ext_entry.grid(column=1, row=0, padx=10, pady=10)
create_tooltip(old_ext_entry, "Enter without the dot (e.g., 'txt' not '.txt')")

new_ext_label = tk.Label(ext_inner_frame, text="New extension:", font=label_font, bg="#F5F5F5", fg="#424242")
new_ext_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")

new_ext_entry = tk.Entry(ext_inner_frame, font=label_font, width=20)
new_ext_entry.grid(column=1, row=1, padx=10, pady=10)
create_tooltip(new_ext_entry, "Enter without the dot (e.g., 'doc' not '.doc')")

# Numbering section
num_frame = tk.LabelFrame(main_frame, text="Numbering Options", font=label_font, bg="#F5F5F5", fg="#1E88E5", padx=10, pady=10)
num_frame.pack(fill="x", pady=10)

num_inner_frame = tk.Frame(num_frame, bg="#F5F5F5")
num_inner_frame.pack(fill="x")

add_num_checkbox = tk.Checkbutton(
    num_inner_frame, 
    text="Add number to filename", 
    variable=add_num_checkbox_var,
    command=toggle_num_textbox,
    font=label_font,
    bg="#F5F5F5",
    fg="#424242",
    selectcolor="#E3F2FD"
)
add_num_checkbox.grid(column=0, row=0, padx=10, pady=10, sticky="w")

starting_num_label = tk.Label(num_inner_frame, text="Starting number:", font=label_font, bg="#F5F5F5", fg="#757575")
starting_num_label.grid(column=0, row=1, padx=10, pady=10, sticky="w")

starting_num_entry = tk.Entry(num_inner_frame, state="disabled", font=label_font, width=10)
starting_num_entry.grid(column=1, row=1, padx=10, pady=10, sticky="w")
create_tooltip(starting_num_entry, "Enter the starting number for file numbering")

# Action buttons section
button_frame = tk.Frame(main_frame, bg="#F5F5F5")
button_frame.pack(fill="x", pady=20)

run_button = tk.Button(
    button_frame, 
    text="Rename Files", 
    command=rename_files,
    bg="#1E88E5",
    fg="white",
    font=button_font,
    relief="flat",
    padx=15,
    pady=8
)
run_button.pack(side="right", padx=20)

# Status bar
status_bar = tk.Label(window, text="Ready", bd=1, relief=tk.SUNKEN, anchor=tk.W, bg="#E0E0E0", fg="#424242")
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

# Configure grid weights for resizing
ext_inner_frame.columnconfigure(1, weight=1)
dir_inner_frame.columnconfigure(1, weight=1)

# Run the main loop
window.mainloop()
