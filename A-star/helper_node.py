import numpy as np
class Node:
    def __init__(self,x,y):
        self.parent = None
        self.current_node = (x,y)
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
    def updateParent(self,parent):
        self.parent = parent
    def __eq__(self, other):
        return (self.h == other.h) and (self.g == other.g)

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        return (self.h < other.h) and (self.g < other.g)

    def __gt__(self, other):
        return (self.h > other.h) and (self.g > other.g)

    def __le__(self, other):
        return (self < other) or (self == other)

    def __ge__(self, other):
        return (self > other) or (self == other)
    
        
    
    

