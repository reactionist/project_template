def print_to_console(text):
    """
    Function to output text to the console.
    
    Parameters:
    text (str): The text to be printed.
    """
    print(text)

def write_text_to_file(text, filename):
    """
    Function to write text to a file using Python's built-in capabilities.
    
    Parameters:
    text (str): The text to be written.
    filename (str): The path to the file where the text will be written.
    """
    with open(filename, 'w') as file:
        file.write(text)
