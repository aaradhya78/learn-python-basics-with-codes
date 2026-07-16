import os

def list_directory_contents(path='/'):
    """
    Prints the contents of the directory specified by `path`.
    If no path is given, defaults to the current working directory.
    """
    try:
        entries = os.listdir(path)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' does not exist.")
        return
    except NotADirectoryError:
        print(f"Error: The path '{path}' is not a directory.")
        return
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
        return
    except OSError as e:
        print(f"OS error occurred: {e}")
        return

    print(f"Contents of directory '{path}':")
    for entry in entries:
        print(entry)

if __name__ == '__main__':
    # You can change the path below to the directory you want to list:
    directory_path = input("Enter directory path (leave blank for current directory): ").strip()
    if not directory_path:
        directory_path = '.'
    list_directory_contents(directory_path)
