import os
import shutil


def remove_folder_contents(folder_path):
    # Check if the folder exists
    if os.path.exists(folder_path):
        # Iterate over all items in the folder
        for item in os.listdir(folder_path):
            item_path = os.path.join(folder_path, item)
            print(item_path)
            # Check if it's a file or directory
            if os.path.isfile(item_path):
                # Remove the file
                os.remove(item_path)
            elif os.path.isdir(item_path):
                # Remove the directory and its contents recursively
                shutil.rmtree(item_path)


# Example usage:
folder_to_clean = "my_path"
remove_folder_contents(folder_to_clean)
