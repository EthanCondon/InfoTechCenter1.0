print("\n*******************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]
    weatherCondition = random.choice(weatherForcast)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because "
              "of the forcast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 55mph.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because "
              "of the forcast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 45mph.")

vehicleResponseSystem()