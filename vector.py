import random
import math

'''
    This class represents a vector, which is a kind of object which has both a size and a direction, like when you move your body,
    your delta-x vector has two things: your direction, which is from the first point to the second, and the size which is the
    distance between the two points.
'''
class Vector:  
    x = 0
    y = 0
    angle = None
    size = None


    def __init__(self, size = random.uniform(1, 10), angle = random.uniform(0, 2 * math.pi)):
        '''
            This function is the constructor function of the class Vector, it will initiallize all the fields of the vector
            object. the angle, and the size.
        '''
        self.x = math.cos(angle) * size
        self.y = math.sin(angle) * size
        self.angle = angle
        self.size = size

    def set_xy(self, x, y):
        '''
            This function will let the programmer change the x and y variables of the vector, which in turn will change the
            size and angle of the vector.
        '''
        size = math.sqrt(x ** 2 + y ** 2)
        angle = math.atan2(y, x)
        self.__init__(size = size, angle = angle)

    def get_values(self):
        # This function will return the x and y variables of the vector.
        return (self.x, self.y)

    def change_angle(self, new_angle):
        '''
            This function will change the angle of the vecot,r which in turn will change the x and y variables of it and
            The size of the vector.
        '''
        self.angle = new_angle
        self.x = math.cos(self.angle) * self.size
        self.y = math.sin(self.angle) * self.size

    def change_y(self, new_y):
        '''
            This function will change the y variable of the vector, which in turn will change the size and angle of the
            vector.
        '''
        if self.x == 0:
            # If x = 0, then the angle of the vector must be 90 or 270 degrees but in radians.
            if new_y > 0:
                self.angle = math.pi / 2
            else:
                self.angle = math.pi * 1.5
            self.size = new_y
            self.y = new_y
        else:
            self.y = new_y
            self.angle = math.atan2(self.y, self.x)
            self.size = math.sqrt(self.x ** 2 + self.y ** 2)

    def change_x(self, new_x):
        '''
            This function will change the x variable of the vector, which in turn will change the size and angle of the 
            vector.
        '''
        if new_x == 0:
            if self.y > 0:
                self.angle = math.pi / 2
            else:
                self.angle = math.pi * 1.5
            self.size = self.y
            self.x = new_x
        else:
            self.x = new_x
            self.angle = math.atan2(self.y, self.x)
            self.size = math.sqrt(self.x ** 2 + self.y ** 2)