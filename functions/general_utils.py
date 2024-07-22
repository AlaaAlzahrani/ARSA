import tempfile
import os

def create_temp_directory():
    return tempfile.mkdtemp()

def create_subfolder(temp_dir, folder_name):
    subfolder_path = os.path.join(temp_dir, folder_name)
    os.makedirs(subfolder_path, exist_ok=True)
    return subfolder_path

def remove_temp_directory(temp_directory):
    os.rmdir(temp_directory)