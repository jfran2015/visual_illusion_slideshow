from pickle import FALSE, TRUE
from turtle import width
import pygame
import os

class format:
    num_format = 0
    
    def __init__(self, name, path):
        self.name = name
        self.path = path
        format.num_format += 1
        

class gif(format):
    num_gif = 0
    
    def __init__(self, name, path, extension):
        super().__init__(name, path)
        self.extension = extension
        gif.num_gif += 1
        
class video(format):
    num_video = 0
    
    def __init__(self, name, path, extension):
        super().__init__(name, path)
        self.extension = extension
        video.num_video += 1
        
class image(format):
    num_image = 0
    
    def __init__(self, name, path, extension):
        super().__init__(name, path)
        self.extension = extension        
        image.num_image += 1
   
#read in folder with illusions in it and sort to relative classes     
def sort_illusions(folder):
    paths = os.listdir(folder)
    for file in paths:
        print(file)
        if file[-4:] == ".png" or file[-4:] == ".jpg":
        
  
        


if __name__ == "__main__":
    image1 = image("Kanizsa Triangle", r"\files\35_kanizsa_main.png", ".png")
    
    sort_illusions('files/')
    
    
    image = pygame.image.load(r'files\rotsnake2.gif')
    background_color = (255,255,255)
    (width, height) = (500, 500)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Visual Illusions")
    screen.fill(background_color)
    screen.blit(image, (0,0))
    
    
    pygame.display.flip()
    running = TRUE
    while running:
        
        screen.fill(background_color)
        screen.blit(image, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = FALSE
                pygame.quit()
                quit()  
            pygame.display.update()


else:
    print("file not rain as main")            
   
kanizsaTriangle = image("Kanizsa Triangle", "files/35_kanizsa_main.png", ".png")
   
