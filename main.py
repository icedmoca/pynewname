import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox


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
    directory_path.set(dir_path)


def toggle_num_textbox():
    starting_num_entry.config(state=NORMAL if add_num_checkbox_var.get() else DISABLED)


# Create the main window
window = Tk()
window.geometry("800x600")
window.title("File Renamer")

# Set up variables
directory_path = StringVar()
add_num_checkbox_var = BooleanVar()

# Add widgets to the window
select_dir_button = Button(window, text="Select Directory", command=select_directory)
select_dir_button.grid(column=0, row=0, padx=10, pady=20)

directory_entry = Entry(window, textvariable=directory_path, width=50)
directory_entry.grid(column=1, row=0, padx=10, pady=20)

old_ext_label = Label(window, text="Enter current extension:")
old_ext_label.grid(column=0, row=1)

old_ext_entry = Entry(window)
old_ext_entry.grid(column=1, row=1)

new_ext_label = Label(window, text="Enter new extension:")
new_ext_label.grid(column=0, row=2)

new_ext_entry = Entry(window)
new_ext_entry.grid(column=1, row=2)

add_num_checkbox = Checkbutton(window, text="Add number to filename", variable=add_num_checkbox_var,
                               command=toggle_num_textbox)
add_num_checkbox.grid(column=0, row=3)

starting_num_label = Label(window, text="Enter Number if applicable:")
starting_num_label.grid(column=0, row=4)

starting_num_entry = Entry(window, state=DISABLED)
starting_num_entry.grid(column=1, row=4)

run_button = Button(window, text="Run", command=rename_files)
run_button.grid(column=1, row=5, padx=10, pady=20)

# Run the main loop
window.mainloop()
