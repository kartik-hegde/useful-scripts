"""
    Scripts for dealing with email addesses in strings.
"""
import re

def is_email_address(line: str) -> bool:
    """
        Return True if string is a valid email address.

        Args:
            line (str): String to check.

        Returns:
            bool: True if string is a valid email address.
    """
    return re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line) is not None

def return_email_address(line: str) -> str:
    """
        Return the email address in a string.

        Args:
            line (str): String to check.

        Returns:
            str: Email address in the string.
    """
    match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
    if match is not None:
        return match.group(0)
    else:
        print("No email address found in string: " + line)
        return ""
    