import os
import shutil

def organize_files(directory):
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Dictionary to map file extensions to their corresponding folders
    file_type_folders = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif'],
        'Documents': ['.pdf', '.docx', '.txt'],
        'Spreadsheets': ['.xls', '.xlsx', '.csv'],
        'Presentations': ['.ppt', '.pptx'],
        'Archives': ['.zip', '.rar'],
        'Audio': ['.mp3', '.wav'],
        'Video': ['.mp4', '.mkv', '.flv'],
        'Scripts': ['.py', '.js', '.html'],
    }

    for folder in file_type_folders:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        
        if os.path.isdir(file_path):
            continue

        file_extension = os.path.splitext(file_name)[1].lower()
        moved = False
        for folder, extensions in file_type_folders.items():
            if file_extension in extensions:
                destination_folder = os.path.join(directory, folder)
                shutil.move(file_path, destination_folder)
                print(f"Moved: {file_name} to {destination_folder}")
                moved = True
                break
        
        if not moved:
            print(f"No matching folder for: {file_name}")

directory_to_organize = "C:\\Users\\teja\\OneDrive\\Pictures"

organize_files(directory_to_organize)