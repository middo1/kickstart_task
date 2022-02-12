class TennisBall(object):

    def __init__(self, name, mass, radius, color, posx , posy):
        self.name = "TennisBall"
        self.mass = 10
        self.radius = 7
        self.color = "Green"
        self.weight = 99.8
        self.posx = 0.0
        self.posy = 0.0

    def redefineweight(self, g ):
        self.weight = self.mass * g


    def ballimpact(self, angle, dis):
        #Given that angle is the angle at the ball thrown against the surface 
        #and dis is the distance of the ball from the surfac  
        pass

    

        