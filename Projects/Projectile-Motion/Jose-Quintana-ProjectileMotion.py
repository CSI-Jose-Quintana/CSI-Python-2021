import math


# gun = "ADAR 2-15"
# caliber = "5.56 X 45 mm"
# ammunition = "M995"
# velocity_ms = 1013
# Building = "Caribbean Sea View"
# BuildingHeight = 334
# gravity_Ms = 9.81

#Convert your variables into parameters

def ProjectileFunction(gun:str, caliber:str, ammunition: str, velocity_ms: int, Building:str, BuildingHeight:int, gravity:int):

    time_s =math.sqrt((2 * BuildingHeight) / gravity_MS)

    distance_m = (velocity_ms * time_s)

    print(f"The gun selected for the experiment is {gun}. The caliber of {gun} is {caliber}.")

#Convert your script parameters into a single JSON Object


ProjectileFunction("ADAR 2-15", "5.56 X 45 mm", "M995", 1013, "Caribbean Sea View", 334, 9.81)











