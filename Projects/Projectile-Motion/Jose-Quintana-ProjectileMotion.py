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
    time_s =math.sqrt((2 * experimentalData.BuildingHeight) / experimentalData.gravity_Ms)

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)

    print(f"The gun selected for the experiment is {experimentalData.gun}. The caliber of {experimentalData.gun} is {experimentalData.caliber}. Time: {time_s}. Distance: {distance_m}")

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
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M8556A1", 890, "Caribbean Sea View", 334, 9.81),
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M8555", 910, "Caribbean Sea View", 334, 9.81),
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M8556", 856, "Caribbean Sea View", 334, 9.81),
ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M995", 1013, "Caribbean Sea View", 334, 9.81),
ExperimentalData("AKM", "762x69", "PS", 600, "Bruj khalifa", 1500, 9.81)

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

# projectileFunction(experimentalData)









