import os
import shutil

# 1. SETUP: Using your exact absolute paths here is crucial for the script to work correctly.
# The 'r' before the quotes is very important for Windows!
source_folder = r"C:\Users\aiden\OneDrive\Desktop\Test_Downloads"
destination_folder = r"C:\Users\aiden\OneDrive\Desktop\Sorted_Files"

print(f"Targeting Source: {source_folder}")

# 2. DICTIONARY: Map file extensions to folder names
# You can add more to this list later!
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

        if file_ext in file_types:
            # Determine which sub-folder it belongs in
            subfolder_name = file_types[file_ext]
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