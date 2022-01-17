import math
import os
from pathlib import Path
from ExperimentalData import ExperimentalData
import json


# gun = "ADAR 2-15"
# caliber = "5.56 X 45 mm"
# ammunition = "M995"
# velocity_ms = 1013
# Building = "Caribbean Sea View"
# BuildingHeight = 334
# gravity_Ms = 9.81

#Convert your variables into parameters

def projectileFunction(experimentalData: ExperimentalData):
    
    planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    g_ms2 = [3.7, 8.87, 9.81, 3.711, 24.79, 10.44, 8.69, 11.15]

    planet = planets.index(experimentalData.planet)

    time_s =math.sqrt((2 * experimentalData.BuildingHeight) / g_ms2[planet])

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)

    print(f"The gun selected for the experiment is {experimentalData.gun}. The caliber of {experimentalData.gun} is {experimentalData.caliber}. Time: {time_s}. Distance: {distance_m}")
    print(f"The experiment is carried out in {experimentalData.planet} with a gravity of {g_ms2[planet]}.")


#Convert your script parameters into a single JSON Object
# experimentalData = {

# "gun": "ADAR 2-15",
# "caliber": "5.56 X 45 mm",
# "ammunition": "M995",
# "velocity_ms": 1013,
# "Building":  "Caribbean Sea View",
# "BuildingHeight": 334,
# "gravity_Ms":  9.81   

# }

# experimentalData = ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M995", 1013, "Caribbean Sea View", 334, 9.81)


myDataSet = [
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M8556A1", 890, "Caribbean Sea View", 334, "Earth"),
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M8555", 910, "Caribbean Sea View", 334,"Mars"),
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M8556", 856, "Caribbean Sea View", 334, "Venus"),
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M995", 1013, "Caribbean Sea View", 334, "Saturn"),
ExperimentalData("AKM", "762x69", "PS", 600, "Bruj khalifa", 1500, "Mercury")

]

for data in myDataSet:
    print("\n-------------------------------------------------\n")
    projectileFunction(data)

#Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, 'Projectile-Motion.json')

print(myOutputFilePath)

with open(myOutputFilePath, 'w') as outfile:
    json.dump([data.__dict__ for data in myDataSet], outfile)

#Deserialization
deserialize = open(myOutputFilePath)
experimentJson = json.load(deserialize)

for e in experimentJson:
    print("\n-------------------------------------------------\n")
    projectileFunction(ExperimentalData(**e))
# projectileFunction(experimentalData)









