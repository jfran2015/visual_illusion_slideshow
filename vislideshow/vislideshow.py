import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk

class format:
    num_format = 0
    
    def __init__(self, name, path):
        self.name = name
        self.path = path
        num_format += 1
        

class gif(format):
    num_gif = 0
    
    def __init__(self, name, path, extension):
        super().__init__(name, path)
        self.extension = extension
        num_gif += 1
        
class video(format):
    num_video = 0
    
    def __init__(self, name, path, extension):
        super().__init__(name, path)
        self.extension = extension
        num_video += 1
        
class image(format):
    num_image = 0
    
    def __init__(self, name, path, extension):
        super().__init__(name, path)
        self.extension = extension
        num_image += 1
        


if __name__ == "__main__":
   print("File one executed when ran directly")
   kanizsaTriangle = image("Kanizsa Triangle", "files/35_kanizsa_main.png", ".png")
   print(kanizsaTriangle.name)
   
else:
   print("File one executed when imported")