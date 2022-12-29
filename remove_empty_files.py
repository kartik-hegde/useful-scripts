"""Remove Empty files from a directory"""
import os
import sys

def remove_empty_files(path):
    """Remove Empty files from a directory"""
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.stat(os.path.join(root, file)).st_size == 0:
                print("Removing: ", os.path.join(root, file))
                os.remove(os.path.join(root, file))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python remove_empty_files.py <path>")
        sys.exit(1)
    remove_empty_files(sys.argv[1])                