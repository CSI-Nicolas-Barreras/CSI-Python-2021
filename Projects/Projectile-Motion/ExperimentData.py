
import math
class ExperimentData:

    def __init__(self, gun:str,CartigeCalibre:str, ammulation:str, Projectilevelocity_mps:int, building:str, height_m:int,gravity:float):
        self.gun= gun
        self. CartigeCalibre=CartigeCalibre
        self.ammulation=ammulation
        self.Projectilevelocity_mps=Projectilevelocity_mps
        self.building=building
        self.height_m= height_m
        self.gravity=gravity

    def getTime(self):
        return ( math.sqrt((2*self.height_m)/self.gravity))

    def getDistance(self):
        return ( self.Projectilevelocity_mps * self.getTime())

    def run(self):
        print(f"We will shoot a {self.gun},from a building {self.building} the building height it's {self.height_m}. The {self.gun} have a calibre {self.CartigeCalibre} and for ammulation {self.ammulation}. The {self.gun} shoots at a velocity of {self.Projectilevelocity_mps} the distance was {self.getDistance()} with a time of {self.getTime()}")





