# pynewname

A Python script to rename file extensions and optionally add numbers to the end of file names in a specified directory using a graphical user interface (GUI) built with `tkinter`.

## Description

This script allows users to rename all files with a specified extension in a selected directory to a new extension. Users can also add a number to the end of each file name. The user selects the directory through a file explorer dialog, inputs the old and new extensions, and optionally checks a box to add numbers to the file names. Upon clicking the "Run" button, the script processes the renaming. A message box notifies the user when the renaming is complete.

## How to Use

1. **Download the Script**
   - Download the `main.py` file from the GitHub repository.

2. **Install Python**
   - Install Python if it's not already installed. [Download Python](https://www.python.org/downloads/)

3. **Install Required Modules**
   - Open your command prompt or terminal and run:
     ```bash
     pip install tk
     ```

4. **Run the Script**
   - Double-click the `main.py` file to open the GUI.

5. **Select Directory**
   - Click the "Select Directory" button to choose the directory containing the files you want to rename.

6. **Enter Current Extension**
   - In the "Enter current extension" field, input the current extension of the files (e.g., `txt` for `.txt` files, without quotes).

7. **Enter New Extension**
   - In the "Enter new extension" field, input the new extension you want for the files (e.g., `doc` for `.doc` files, without quotes).

8. **Add Number to File Names (Optional)**
   - Check the "Add number to the end of file name" box if you want to add numbers.
   - Enter the starting number in the "Enter Number if applicable" field.

9. **Rename Files**
   - Click the "Rename Files" button to start renaming the files in the selected directory.

10. **Confirmation**
    - A message box will appear indicating the renaming process was successful.
    - Check the directory to confirm that the files have been renamed according to your specifications.

## Example

1. **Before Renaming:**
   - `file1.txt`
   - `file2.txt`

2. **After Renaming (with new extension `.doc` and starting number `1`):**
   - `file1_1.doc`
   - `file2_2.doc`

## License

This project is licensed under the MIT License.

