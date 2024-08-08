#Automatically organise the files in your downloads folder based on file type.

import os,shutil,platform
from tkinter import *

class Organize:
    def __init__(self):
        self.start_graphics()

    def start_graphics(self):
        self.root = Tk()
        self.root.title("Organizing Download Files Based On File Type")
        self.root.minsize(width=400,height=200)
        self.root.maxsize(width=400,height=200)

        self.label1 = Label(self.root,text="Organizing Download Files Based On File Type")
        self.label1.place(x=50,y=20)

        self.download_button = Button(self.root,text="Downloads Folder",command=lambda:self.move_files(type="Downloads"))
        self.download_button.place(x=120,y=80)

        self.download_button = Button(self.root, text="        Desktop        ", command=lambda:self.move_files(type="Desktop"))
        self.download_button.place(x=120, y=110)

        self.download_button = Button(self.root, text="     Documents      ", command=lambda:self.move_files(type="Documents"))
        self.download_button.place(x=120, y=140)

        self.root.mainloop()

    def move_files(self,type:str):
        # This will check what operating system(OS) you use
        if platform.system() == "Windows":
            path = os.path.join(os.path.expanduser("~"), f"{type}")
        else:
            path = os.path.expanduser(f"~/{type}")

        # This will make a list of the files
        download_files = os.listdir(path)
        for file in download_files:
            if os.path.isfile(f"{path}/{file}"):
                extension = file.split(".")[-1]
                # Invincible file macOS
                # This file is a hidden system file used by macOS to store custom attributes of a folder, such as the position of icons or the choice of a background image.
                if extension == "DS_Store":
                    pass
                elif extension == "localized":
                    pass
                else:
                    try:
                        items = os.listdir(f"{path}/{extension}")
                    except FileNotFoundError:
                        os.makedirs(f"{path}/{extension}")
                    # This will move the files
                    finally:
                        shutil.move(f"{path}/{file}", f"{path}/{extension}")


if __name__ == "__main__":
    organize = Organize()