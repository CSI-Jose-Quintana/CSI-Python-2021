import math
from ExperimentalData import ExperimentalData
# gun = "ADAR 2-15"
# caliber = "5.56 X 45 mm"
# ammunition = "M995"
# velocity_ms = 1013
# Building = "Caribbean Sea View"
# BuildingHeight = 334
# gravity_Ms = 9.81

#Convert your variables into parameters

def ProjectileFunction(experimentalData: ExperimentalData):
    time_s =math.sqrt((2 * experimentalData.BuildingHeight) / experimentalData.gravity_Ms)

    distance_m = (experimentalData.velocity_ms * time_s)
    # distance_m = (experimentalData[velocity_ms] * time_s)


    print(f"The gun selected for the experiment is {experimentalData.gun}. The caliber of {gun} is {caliber}.")

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

experimentalData = ExperimentalData("ADAR 2-15", "5.56 X 45 mm", "M995", 1013, "Caribbean Sea View", 334, 9.81)

ProjectileFunction









