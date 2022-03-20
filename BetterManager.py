import os
import time
import shutil
import platform
from tkinter import filedialog
import getpass

"""
BetterManager BY EFROXE

Check the README.md file
located in the installation
directory/folder.
"""

class UnsupportedOSError(Exception):
    """CUSTOM ERROR IF THE OS IS LINUX"""
    __raisedmessage__ = "Not supported OS (Windows needed)"

    def __init__(self, message=__raisedmessage__, code=325):
        super().__init__(message)
        self.code = code
        self.message = message

    def __str__(self):
        return f'{self.message} ERROR CODE; {self.code}'

mode = input("Mode > ")
if mode == "normal":
    exit_app = False
    while not exit_app:
        error_list = ["Unknown command", "Not supported OS (Windows needed)", "Permission denied", "Could not copypaste file"]
        get_os = platform.system()
        if get_os == 'Windows':
            file_options = input("Normal > ")
            if file_options == "open -h":
                try:
                    file = filedialog.askopenfilename()
                    f=open(file, 'rb')
                    bytes = 0
                    line = []
                    fileContents = f.read()
                    for b in fileContents:
                        bytes = bytes + 1
                        line.append(b)
                        print("{0:0{1}x}".format(b, 2), end=' ')
                        if bytes %16 == 0:
                            print("#", end=' ')
                            for b2 in line:
                                if (b2 >= 32) and (b2 <= 126):
                                    print(chr(b2), end=' ')
                                else:
                                    print("*", end=' ')
                            line = []
                            print("")

                except FileNotFoundError as fnfe:
                    print("No such file or directory. Check for typos, or deleted files.")
            # FILE OPTIONS

            elif file_options == "delete":
                try:
                    deletefile = filedialog.askopenfilename()
                    os.remove(deletefile)

                except Exception as e:
                    print(e)

            elif file_options == "help":
                print("""Available commands:
                'delete', deletes a specified file
                'exit()', exits the application
                'rename', renames a specified file
                'copypaste', copies a file and pastes it in a new location
                'movefile', moves a file to a specified destination
                'create', creates a new file in the Desktop
                'createdir', creates a directory
                'removedir', removes a specified directory
                'list', lists the contents of a directory
                
                MANAGEMENT:
                'open -h', opens the HEX code of a specified file""")

            elif file_options == "exit()":
                print("Exiting...")
                exit()

            elif file_options == "rename":
                try:
                    old_name = input(r"Enter the path of the file (Old name): ")
                    new_name = input(r"Enter the path of the file (New name): ")

                    os.rename(old_name, new_name)
                    print("Renamed file successfully.")

                except PermissionError as PE:
                    print(error_list[2])

                except FileNotFoundError as fnfe:
                    print("File not found")

            elif file_options == "copypaste":
                try:
                    original_location = input(r"Enter the location of the file: ")
                    pasted_location = input(r"Enter the location to paste the file: ")

                    shutil.copyfile(original_location, pasted_location)
                except Exception as E:
                    print(error_list[3])

            elif file_options == "movefile":
                try:
                    current_destination = input(r"Enter the current destination of the file: ")
                    new_destination = input(r"Enter the new destination of the file: ")

                    shutil.move(current_destination, new_destination)

                except PermissionError as PE:
                    print(error_list[2])

                except FileNotFoundError as fnfe:
                    print("File not found")

            elif file_options == "create":
                try:
                    username = getpass.getuser()
                    contents = input("Write in the file: ")
                    with open(r"C:/Users/" + username + "/Desktop/python_file.txt", 'w') as created_file:
                        created_file.write(contents)
                    print("Created file successfully!")

                except Exception as e:
                    print("Could not create the file.")

            elif file_options == "createdir":
                try:
                    create_directory = input(r"Enter the directory you want to create: ")
                    os.mkdir(create_directory)
                    print("Directory successfully created!")

                except Exception as e:
                    print("""Unable to create directory. This error may be caused
                    Because the location you are trying to create the directory is
                    hold under administrative permissions.""")

            elif file_options == "removedir":
                try:
                    remove_dir = input(r"Enter the directory you want to remove: ")
                    os.rmdir(remove_dir)
                    print("Directory successfully removed")

                except Exception as e:
                    print("Unable to remove directory")

            elif file_options == "list":
                try:
                    list_directory = input(r"Enter a directory to list: ")
                    print(os.listdir(list_directory))
                    print("Directory successfully listed.")

                except Exception as e:
                    print("Unable to list directory.")

            else:
                print(error_list[0])

        elif get_os == 'Linux':
            raise UnsupportedOSError()
elif mode == "permission":
    open = input(r"Enter a file to open (type 'ABOUT'): ")
    writable_permission = os.access(open, os.W_OK)
    redeable_permission = os.access(open, os.R_OK)

    print(f"Writable permission: {writable_permission}")
    print(f"Redeable permission: {redeable_permission}")

    if open == "ABOUT":
        print("""
        Why does 'Permission Mode' Exist?
            
        Permission mode is all about file permissions.
        Permission mode allows you to check the file
        permissions and decide if you want to
        open the file in normal mode, or not.
            
        Permission types: REDEABLE | WRITABLE
        """)

else:
    print("Invalid mode; Type: 'normal' or 'permission'.")