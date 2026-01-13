import os
import shutil

# Folder to organize
source_folder = r"C:\Users\REHAN KHAN\Downloads"

# File type mapping
file_types = {
    "Documents": [".pdf", ".docx", ".txt"],
    "Images": [".jpg", ".jpeg", ".png"],
    "Data": [".csv", ".xlsx"],
    "Archives": [".zip", ".rar"]
}

# Create folders if they don't exist
for folder in file_types:
    folder_path = os.path.join(source_folder, folder)
    if not os.path.exists(folder_path):
        os.mkdir(folder_path)

# Move files
for file_name in os.listdir(source_folder):
    file_path = os.path.join(source_folder, file_name)

    if os.path.isfile(file_path):
        for folder, extensions in file_types.items():
            if file_name.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(source_folder, folder, file_name))
                break

print("✅ Files organized successfully!")
