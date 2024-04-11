from app.io.input import *
from app.io.output import *

def main():
    input_text_from_console()
    
    text = "Sample text"
    
    print_to_console(text)
    
    filename = "output.txt"
    write_text_to_file(text, filename)
    
    read_text = read_text_from_file(filename)
    print_to_console(read_text)
    
    read_text2 = read_text_from_file_with_pandas(filename)
    print_to_console(read_text2)

if __name__ == "__main__":
    main()