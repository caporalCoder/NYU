#
# Problem statement:
#      Create a python script that will check if a particular string is a palindrome or not.
#      (Reads the same forwards and backwards). You can either pass the string as an argument 
#      or ask for user input.
#
#
# Run instruction:
#         python python_skills_programming_lab_1.py "YourStringHere"

import argparse

def is_palindrome(s):
    """
    Check if a given string is a palindrome.
    
    This function converts the string to lowercase and then checks if 
    the string reads the same forwards and backwards. No character is 
    filtered out.

    Args:
    - s (str): The string to be checked.

    Returns:
    - bool: True if the string is a palindrome, False otherwise.
    """
    # Convert the string to lowercase.
    s = s.lower()
    
    # Compare the string with its reverse.
    return s == s[::-1]


def main():
    # Create argument parser.
    parser = argparse.ArgumentParser(description="Check if a given string is a palindrome.")

    # Add a positional argument for the string to be checked.
    parser.add_argument("string", type=str, help="The string to be checked for palindrome property")

    # Parse the arguments.
    args = parser.parse_args()

    # Check if string is a palindrome and print the result.
    if is_palindrome(args.string):
        print(f"'{args.string}' is a palindrome.")
    else:
        print(f"'{args.string}' is not a palindrome.")

if __name__ == "__main__":
    main()
