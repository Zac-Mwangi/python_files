# class is a blueprint of how an object behaves
# describes how an object looks and behave

class Planet:

    # class level attribute
    shape = "Spherical" 

    # instant attribute
    def __init__(self,name,radius,gravity,system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    # instant methods
    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'
    
    # class method (common to all planet)
    # has access to class level attributes
    @classmethod
    def common (cls):
        return f'All planets are {cls.shape} because of gravity'
    
    # method that doesn't have access to self nor class
    # it has access to parameters that we pass to it individually
    @staticmethod
    def spin(speed = 2500):
        return f'The planet spins and spins @ {speed} miles per hour'



