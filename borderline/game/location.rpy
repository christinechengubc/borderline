init -2 python:
    class Location():
        
        #takes in a String description, x-position, y-position, height and width (of box on map) and the label to jump to.
        def __init__(self, description, x, y, w, h, label):
            # self.name = name
            self.description = description
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.label = label
            
        def getHotspot(self):
            return (self.x, self.y, self.w, self.h)