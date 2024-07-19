import shutil

# Specify the path of the file you want to copy
file_to_copy = './demo.py'

# Specify the path of the destination directory you want to copy the file into
destination_directory = './projects'

# Use the shutil.copy2() method to copy the file to the destination directory
shutil.copy2(file_to_copy, destination_directory)
