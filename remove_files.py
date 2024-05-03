import os


def remove_files(path: str) -> None:
    for root, dirs, files in os.walk(path):
        print(root, dirs, files)


remove_files(path="../../")
