class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point(x={self.x}, y={self.y})'

    def midpoint(self, other):
        midX = (self.x + other.x)/2
        midY = (self.y + other.y)/2
        return Point(midX, midY)# makes a new instance here
    
    def addPoint(self, other):
        """
        Adds the x and y coordinates of another point to this instance
        """

        #Adding the x coordinates
        self.x += other.x

        #Adding the y coordinates
        self.y += other.y
    
    def projectToYAxis(self):
        """
        returns a new Point instance that is the same as the original, only with the x value set to 0
        """
        #Makes the x-coordinate zero
        newX = 0 

        # Make the y-coordinate the same as before
        newY = self.y 

        #Make a new instance here with these coordinates
        return Point(newX, newY)



p1 = Point(3, 4)
p2 = p1.projectToYAxis()
assert(str(p2) == 'Point(x=0, y=4)')