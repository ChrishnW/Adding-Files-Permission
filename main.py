import subprocess
import os
from typing import List

def get_all_files_and_directories(directory: str) -> List[str]:
    paths = []
    for root, dirs, files in os.walk(directory):
        for dir in dirs:
            paths.append(os.path.join(root, dir))
        for file in files:
            paths.append(os.path.join(root, file))
    return paths

def add_all_permissions(file_path: str, username: str):
    try:
        subprocess.run(
            [
                "icacls",
                file_path,
                "/grant",
                "Everyone:(F)",
                "/grant",
                f"{username}:(F)",
                "/grant",
                "SYSTEM:(F)",
                "/grant",
                "Administrators:(F)",
                "/T",
                "/C",
            ],
            check=True,
        )
        print(f"Permissions changed successfully for {file_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to change permissions for {file_path}: {e}")

def change_permissions_in_directory_windows(directory: str, username: str):
    all_paths = get_all_files_and_directories(directory)
    for path in all_paths:
        add_all_permissions(path, username)

if __name__ == "__main__":
    directory_path = "DIRECTORY"
    local_username = "USERNAME"
    change_permissions_in_directory_windows(directory_path, local_username)