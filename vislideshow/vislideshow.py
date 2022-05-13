import pygame
import sys, os


#https://riptutorial.com/pygame/example/17502/drawing-and-a-basic-animation

background_color = (255,255,255)

class media:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Visual Illusion Slideshow")
        
        self.size = self.width, self.height=700, 700,
        self.screen = pygame.display.set_mode((self.size))
        self.screen.fill((background_color))
        self.load_image()
        
    def update_image(self, name):
        self.name=name
        self.image=pygame.image.load(self.name)
        
        self.screen.blit(self.image, (0,0))
        #pygame.display.flip()
        
        pygame.display.update()
        pygame.time.wait(2000) #time in miliseconds
        return True
    
    def load_image(self):
        x = 0
        data_list=[]
        path = r'files/'
        file_folder = os.listdir(path)
        
        for name in file_folder:
            if name.endswith(".jpg") or name.endswith(".png") or name.endswith(".gif"):
                data_list.append(name)
            data_list[x] = (r"files/" + data_list[x])
            x += 1
        
        for content in data_list:
            self.update_image(content)
            
    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



if __name__ == "__main__":
    obj=media()
    obj.main()
           
   

   
