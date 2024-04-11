import unittest
import pandas as pd
from app.io.input import *

class TestReadTextFromFile(unittest.TestCase):
    
    def test_read_existing_file(self):
        # Write a temporary file to read
        test_filename = 'test_file.txt'
        test_content = 'Hello, world!'
        with open(test_filename, 'w') as test_file:
            test_file.write(test_content)
        
        # Now test reading the file
        read_content = read_text_from_file(test_filename)
        self.assertEqual(read_content, test_content)

        # Clean up - delete the temporary file
        import os
        os.remove(test_filename)

    def test_read_non_existing_file(self):
        # Attempt to read a file that does not exist and expect a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            read_content = read_text_from_file('non_existent_file.txt')

class TestReadTextFromFileWithPandas(unittest.TestCase):
    
    def test_read_csv_file(self):
        # Prepare a temporary CSV file
        test_filename = 'test_file.csv'
        test_content = 'col1,col2\nval1,val2'
        with open(test_filename, 'w') as test_file:
            test_file.write(test_content)
        
        # Now test reading the CSV file
        df = read_text_from_file_with_pandas(test_filename)
        self.assertTrue(isinstance(df, pd.DataFrame))
        self.assertEqual(df.iloc[0]['col1'], 'val1')
        self.assertEqual(df.iloc[0]['col2'], 'val2')
        
        # Clean up - delete the temporary file
        import os
        os.remove(test_filename)

    def test_read_non_existing_csv_file(self):
        # Ensure pandas raises a FileNotFoundError when the CSV file does not exist
        with self.assertRaises(FileNotFoundError):
            df = read_text_from_file_with_pandas('non_existent_file.csv')
            
if __name__ == '__main__':
    unittest.main()