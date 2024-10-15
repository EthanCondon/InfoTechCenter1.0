print("\n*******************************************\n")

print("Weather Branch\n")

# Import necessary libraries: random for selecting a random weather condition, and sleep for adding delays
import random
from time import sleep

# Function to randomly choose a weather condition from a predefined list
def weather():
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]  # List of possible weather conditions
    weatherCondition = random.choice(weatherForcast)  # Randomly select one weather condition
    return weatherCondition  # Return the selected condition

# Store the randomly selected weather condition in the weatherAlert variable
weatherAlert = weather()

# Function to determine the vehicle's response based on the current weather condition
def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.\n")
        sleep(1)  # Pause for 1 second
        print("VRS system has been engaged only allowing you to drive 55mph.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 45mph.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 65mph.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 70mph.")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 50 minutes because "
              "of the forecast of", weatherAlert, "weather conditions.\n")
        sleep(1)
        print("VRS system has been engaged only allowing you to drive 30mph.")
    else:  # Default case for sunny or other non-listed weather conditions
        print("The National Weather Service is calling for", weatherAlert, "skies. Drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS has been disengaged...")

# Call the vehicle response system function to provide feedback based on the weather
vehicleResponseSystem()