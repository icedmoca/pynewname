import os

# Replace "PATH" with the path to the folder containing your photo files
folder = "PATH"

# Get a list of all the files in the folder
files = os.listdir(folder)

# Loop through the files
for file in files:
  # Get the file's current name and extension
  name, ext = os.path.splitext(file)

  # Create the new name by adding "2" to the end of the current name
  new_name = name + "2" + ext

  # Use the os.rename() function to rename the file
  os.rename(os.path.join(folder, file), os.path.join(folder, new_name))
