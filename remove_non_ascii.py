""" Remove all Non ASCII characters from a string """
import sys
import re

def remove_non_ascii(text):
    return re.sub(r'[^\x00-\x7f]',r'', text)