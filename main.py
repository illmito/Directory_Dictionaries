mport os
import streamlit as st

# Function to read contents of OneDrive folder
def read_onedrive_folder():
    # Get the value of the OneDrive environment variable
    onedrive_path = os.environ.get('OneDrive')
    
    if not onedrive_path:
        st.error("OneDrive environment variable not found.")
        return None, None

    # Path to the OneDrive task_templar folder
    onedrive_task_templar_path = os.path.join(onedrive_path, 'task_templar')
    
    # Initialize directory paths dictionary
    directory_paths = {}

    # Traverse through the OneDrive task_templar folder
    for root, dirs, files in os.walk(onedrive_task_templar_path):
        for dir_name in dirs:
            # Create key-value pairs for directory paths
            directory_paths[dir_name] = os.path.join(root, dir_name)[len(onedrive_task_templar_path):]

    # Initialize dictionary to store file names
    files_dict = {}

    # Traverse through the OneDrive task_templar folder again to get file names
    for root, dirs, files in os.walk(onedrive_task_templar_path):
        for file_name in files:
            folder_name = os.path.basename(root)
            # Create key-value pairs for file names
            if folder_name in directory_paths:
                key = f"{folder_name}_files"
                file_name_without_extension = os.path.splitext(file_name)[0]
                if key not in files_dict:
                    files_dict[key] = {}
                files_dict[key][file_name_without_extension] = file_name

    return directory_paths, files_dict

# Streamlit UI
st.title("Read OneDrive Folder Contents")

# Button to trigger reading OneDrive folder
if st.button("Read OneDrive Folder"):
    directory_paths, files_dict = read_onedrive_folder()
    if directory_paths is not None and files_dict is not None:
        st.write("Directory Paths:")
        st.write(directory_paths)
        st.write("Files Dictionary:")
        st.write(files_dict)
