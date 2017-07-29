import math
class Tilemap(object):
    def __init__(self, width, height, size):
        self.width = width
        self.height = height
        self.size = size
        #Don't modify this directly
        self.data = []
        for i in range(math.ceil(width / size)):
            self.data.append([])
            for j in range(math.ceil(height / size)):
                self.data[i].append(False)
    #Transform a point from game-space to map-space
    def transform(self, x, y):
        return (int(x / self.size), int(y / self.size))
    #Returns if a given point falls within the map
    def valid(self, x, y):
        return x >= 0 and y >= 0 and x < self.width and y < self.height
    #Get the value at a given point of the tilemap
    def get(self, x, y):
        if self.valid(x, y):
            x, y = self.transform(x, y)
            return self.data[x][y]
        else:
            return "Out of Bounds"
    #Set the value at a given point in the tilemap
    def set(self, x, y, value):
        x, y = self.transform(x, y)
        self.data[x][y] = value
    #Checks if a point is free
    def free(self, x, y):
        return not self.get(x, y)
    #Return if a given region contains only Falsey values
    def empty(self, x, y, width, height):
        #Check the interior of the box
        for i in range(int(x), int(x + width), self.size):
            for j in range(int(y), int(y + height), self.size):
                if self.get(i, j):
                    return False
        #Check the other corners
        return (self.free(x, y)
            and self.free(x + width, y)
            and self.free(x, y + height)
            and self.free(x + width, y + height))
    #Find the largest amount a rectangle can move
    def move_contact(self, x, y, width, height, speed_x, speed_y):
        #If the object can just move to the desired position
        if self.empty(x + speed_x, y + speed_y, width, height):
            return speed_x, speed_y
        #If the object is stuck and cannot move at all
        if not self.empty(x, y, width, height):
            return 0, 0
        #Roll back the speed until the object can move
        try_x = speed_x
        try_y = speed_y
        sign = lambda x: 1 if x > 0 else (-1 if x < 0 else 0) #Find the sign of a number
        delta_try_x = -sign(try_x)
        delta_try_y = -sign(try_y)
        while not self.empty(x + try_x, y + try_y, width, height):
            try_x += delta_try_x
            try_y += delta_try_y
        if abs(try_x) < 1: try_x = 0
        if abs(try_y) < 1: try_y = 0
        return try_x, try_y
    #Slide an object, allowing it to move part of its velocity for both components
    def slide_contact(self, x, y, width, height, speed_x, speed_y):
        move_x = self.move_contact(x, y, width, height, speed_x, 0)[0]
        move_y = self.move_contact(x + move_x, y, width, height, 0, speed_y)[1]
        return move_x, move_y
