'''
Problem Statement: Create a Python script that lists all files and subdirectories in a given directory. 
Your script should prompt the user for the directory path and then display the contents.

Code Example:
    import os

    def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
Expected Outcome: The script should correctly list all files and subdirectories in the specified directory.
 Handle exceptions for invalid paths or inaccessible directories.
'''

import os

def list_directory_contents():
    while True:
        path = input("Enter the directory path (or 'Q' to quit): ")

        if path.lower() == 'q':
            break

        try:
            for item in os.listdir(path):
                item_path = os.path.join(path, item)
                if os.path.isfile(item_path):
                    print(f"File: {item_path}")
                elif os.path.isdir(item_path):
                    print(f"Directory: {item_path}")
        except FileNotFoundError:
            print("The specified path does not exist.")
        except PermissionError:
            print("You do not have permission to access the specified directory.")
        except Exception as e:
            print(f"An error occurred: {e}")

list_directory_contents()  # Call the function to start the script

            
