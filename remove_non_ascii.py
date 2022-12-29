""" Remove all Non ASCII characters from a string """
import sys
import re
import os



def remove_non_ascii_str(text):
    """ Remove all Non ASCII characters from a string """
    return re.sub(r'[^\x00-\x7f]',r'', text).encode("utf-8")

def remove_non_ascii_dir(path):
    """ Remove all Non ASCII characters from a directory """
    for root, dirs, files in os.walk(path):
        for file in files:
            print("Reading: ", os.path.join(root, file))
            with open(os.path.join(root, file), 'r', encoding="ISO-8859-1") as f:
                text = f.read()
            for line in text:
                line=remove_non_ascii_str(line)
            text = remove_non_ascii_str(text)
            with open(os.path.join(root, file), 'wb') as f:
                f.write(text)

def test_if_ascii_file(path):
    """ Test if a file is ASCII """
    try:
        with open(path, 'r') as f:
            text = f.read()
    except UnicodeDecodeError:
        return False

    return True

def test_if_ascii_dir(path):
    """ Test if a directory is ASCII """
    for root, dirs, files in os.walk(path):
        for file in files:
            if not test_if_ascii_file(os.path.join(root, file)):
                print("Non ASCII file: ", os.path.join(root, file))
            

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python remove_non_ascii.py <path> <remove|test|encode>")
        sys.exit(1)
    
    if(sys.argv[2] == "remove"):
        remove_non_ascii_dir(sys.argv[1])
    elif(sys.argv[2] == "test"):
        test_if_ascii_dir(sys.argv[1])
    else:
        print("Usage: python remove_non_ascii.py <path> <remove|test|encode>")
        sys.exit(1)