from vector import *
from location import *
from config import *
import random

'''
    This function will represent a Particle, which is a ball with a color, size, speed and location in space.
    it will be able to handle deflections with walls, other particles and stuff
'''
class Particle:
    loc = None
    speed = None
    size = None
    color = None
    changed = False
    def __init__(self, color = (0, 0, 0), loc = Location(), speed = Vector(), size = 1):
        '''
            This is the constructor function of the class Particle, it will initialize all fields in the class.
        '''
        self.loc = loc
        self.speed = speed
        self.size = size
        self.color = color

    def deflection(self, deflector):
        '''
            This function will handle the deflection of the object, it will get itself and the object which deflects with it
            and calculate the new speed of this particle.
        '''
        tangent = math.atan2((self.loc.locationY - deflector.loc.locationY), (self.loc.locationX - deflector.loc.locationX))
        self.speed.change_angle(2*tangent - self.speed.angle)
        deflector.speed.change_angle(2*tangent - deflector.speed.angle)
        angle = 0.5 * math.pi + tangent
        # Move the objects a bit from eachother for the deflection to work, this is like some friction
        self.loc.locationX += math.sin(angle)
        self.loc.locationY -= math.cos(angle)
        deflector.loc.locationX -= math.sin(angle)
        deflector.loc.locationY += math.cos(angle)
        # Change the size of the speed of each object due to elasticity. 
        self.speed.size *= ELAS
        deflector.speed.size *= ELAS
        # finally, flip the speeds of both object for them to continue moving away from eachother.
        deflector.speed, self.speed = self.speed, deflector.speed
        

    def check_obj_collision(self, obj):
        '''
            This function will check if two objects are coliding, how ? with math. 
            it will calculate the distance between both object with pythogrea and check if it's less than
            the addition of radiuses of both objects, which is like the shared radius between them.
            in short, it works. don't touch it.
        '''
        # Delta - y and Delta - x help us to calculate the distance between both objects.
        dx = self.loc.locationX - obj.loc.locationX
        dy = self.loc.locationY - obj.loc.locationY
        distance = math.hypot(dx, dy)
        if distance < self.size + obj.size:
            return True
        return False
        
        
    def bounce_off_static(self, width, height):
        '''
            This function will check if the object is bouncing off a wall, if it is, it will change it's speed for it to bounce
            off the wall.
        '''
        if self.loc.locationX > width - self.size:
            self.loc.locationX = width - self.size
            self.speed.change_x(- self.speed.x)
            return True
        elif self.loc.locationX < self.size:
            self.loc.locationX = self.size
            self.speed.change_x(- self.speed.x)
            return True
        elif self.loc.locationY > height - self.size:
            self.loc.locationY = height - self.size
            self.speed.change_y(- self.speed.y)
            return True
        elif self.loc.locationY < self.size:
            self.loc.locationY = self.size
            self.speed.change_y(- self.speed.y)
            return True
        return False