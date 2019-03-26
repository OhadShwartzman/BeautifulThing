
'''
    This function will define the location of an object, it will hold two variables which represent the coordinates
    of the object on the canvas.
'''
class Location:
    locationX = 0
    locationY = 0

    def __init__(self, x = 0, y = 0):
        # The constructor of the Location class, which will initialize all the fields of it.
        self.locationX = x
        self.locationY = y

    def get_values(self):
        # This function will return a tuple which holds the x and y coordinates of the location of an object.
        return (int(self.locationX), int(self.locationY))