

from ast import Num


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
        
        
#how to blah blah blah 