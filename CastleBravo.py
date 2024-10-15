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
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because "
              "of the forcast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 65mph.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because "
              "of the forcast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 70mph.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because "
              "of the forcast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 30mph.")
    else:
        print("The National Weather Service is calling for", weatherAlert, "skies. drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS has been disengaged...")
vehicleResponseSystem()