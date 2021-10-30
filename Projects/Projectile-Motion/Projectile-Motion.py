import math

import json
from ExperimentData import  ExperimentData
from pathlib import Path
import os

#gun= "AK-74N"
#CartigeCalibre= "5.45x39mm"
#ammulation= "5.45x39mm PS gs"
#Projectilvelocity_mps = 905 
#building= "Empire State Building"
#height_m= 382
#time_s= math.sqrt((2*height_m)/9.8)
#distance_m=  Projectilvelocity_mps * time_s

myDataSet = {
    ExperimentData("AK-74N","5.45x39mm","5.45x39mm PS gs",905 ,"Empire State Building",382,9.807)
    ,ExperimentData("AK-103","7.62x39mm","7.62x39mm BP gzh",543 ,"Empire State Building",382,24.79)
    ,ExperimentData("AK-101","5.56x45mm ","5.56x45mm FMJ",650,"Empire State Building",382,10.44)
    ,ExperimentData("AK-102","5.56x45mm ","5.56x45mm FMJ",550 ,"Empire State Building",382,8.87)
    ,ExperimentData("AK-104","7.62x39mm","7.62x39mm BP gzh",679 ,"Empire State Building",382,3.7)
}



outputPath = Path(__file__).parents[0]
outputPathFile = os.path.join(outputPath,"ExperimentData.json")

with open(outputPathFile,"w") as outfile:
    json.dump ([data.__dict__ for data in myDataSet], outfile)

#print(f"We will shoot a {gun},from a building {building} the building height it's {height_m}. The {gun} have a calibre {CartigeCalibre} and for ammulation {ammulation}. The {gun} shoots at a velocity of {Projectilvelocity_mps} then we will calculate the distance the bullet where it landed")



deserialize = open(outputPathFile,)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("\n")
    ExperimentData(**e).run()
         