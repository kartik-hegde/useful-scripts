"""Rename files in a directory by removing a prefix (e.g., '.file.txt' -> 'file.txt')."""
import os
import sys

def remove_prefix_from_filenames(directory, prefix):
    """Remove a prefix from all filenames recursively in a directory."""
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.startswith(prefix):
                print('Renaming {} to {}'.format(filename, filename[len(prefix):]))
                new_filename = filename[len(prefix):]
                os.rename(os.path.join(root, filename), os.path.join(root, new_filename))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python rename_files.py <directory> <prefix>')
        sys.exit(1)
    remove_prefix_from_filenames(sys.argv[1], sys.argv[2])