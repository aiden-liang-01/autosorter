# importing necessary libraries
import os # this is for file and directory operations
import shutil # this is for moving files from one location to another

# SETUP: Use absolute paths here is crucial for the script to work correctly on my pc
# 'r' before the quotes to escape the backslashes
source_folder = r"C:\Users\aiden\OneDrive\Desktop\Test_Downloads"
destination_folder = r"C:\Users\aiden\OneDrive\Desktop\Sorted_Files"

print(f"Targeting Source: {source_folder}")

# DICTIONARY: Map file extensions to folder names
# I can add more later
file_types = {
    ".pdf": "Documents",
    ".jpg": "Images",
    ".png": "Images",
    ".zip": "Archives",
    ".exe": "Installers"
}

def sort_files():
    # Create the source/destination folders if they don't exist yet
    if not os.path.exists(source_folder):
        os.makedirs(source_folder)
    
    # Check every file in the source folder
    for filename in os.listdir(source_folder):
        # Get the file extension (e.g., '.pdf')
        file_ext = os.path.splitext(filename)[1].lower()

        if file_ext in file_types: # compare the file extension to the dictionary keys
            # Determine which sub-folder it belongs in
            subfolder_name = file_types[file_ext] # get the corresponding folder name from the dictionary
            target_path = os.path.join(destination_folder, subfolder_name) 

            # Create the sub-folder if it doesn't exist
            if not os.path.exists(target_path):
                os.makedirs(target_path)

            # Move the file!
            original_path = os.path.join(source_folder, filename)
            new_path = os.path.join(target_path, filename)
            
            shutil.move(original_path, new_path)
            print(f"Moved: {filename} -> {subfolder_name}")

if __name__ == "__main__":
    sort_files()
    print("Sorting complete!")