# 8.1
class Ponto:
    'this class represents points on a plane'
    def __init__(self, coordx=0, coordy=0):
        'initializes coordinates'
        self.x = coordx
        self.y = coordy
    def setx(self, coordx):
        'defines point x coordinate as coordx'
        self.x = coordx
    def sety(self, coordy):
        'defines point y coordinate as coordy'
        self.y = coordy
    def get(self):
        'returns x and y coordinates as a tuple'
        return (self.x, self.y)
    def getx(self):
        'returns x coordinate'
        return self.coordx
    def gety(self):
        'returns y coordinate'
        return self.coordy
    def move(self, dx, dy):
        'changes x and y coordinates by dx and dy'
        self.x += dx
        self.y += dy
    
