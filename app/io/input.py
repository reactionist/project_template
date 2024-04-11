def input_text_from_console():
    """
    Function for inputting text from the console.
    """
    text = input("Please enter text: ")
    return text

def read_text_from_file(filename):
    """
    Function for reading text from a file using Python's built-in capabilities.
    
    Parameters:
    filename (str): The path to the file to be read.
    """
    with open(filename, 'r') as file:
        content = file.read()
    return content

def read_text_from_file_with_pandas(filename):
    """
    Function for reading text from a file using the pandas library.
    
    Parameters:
    filename (str): The path to the file to be read.
    """
    import pandas as pd
    data = pd.read_csv(filename)
    return data