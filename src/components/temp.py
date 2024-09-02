def reformat_string(s):
    """
    This function reformats the string such that all digits are grouped together
    and appear before the letters, which are sorted alphabetically. All special 
    characters are moved to the end of the string in their original order.
    
    Parameters:
    s (str): The input string containing digits, letters, and special characters.
    
    Returns:
    str: The reformatted string with digits first, followed by sorted letters, and 
    finally the special characters in their original order.
    """


def process_input_and_call_function(func):
    input_value = input("Enter the string: ")
    
    if not all(char.isdigit() or char.islower() or not char.isalnum() for char in input_value):
        print("The string should only contain lowercase English letters, digits, and special characters.")
        return
    
    result = func(input_value)
    print(result)

process_input_and_call_function(reformat_string)
