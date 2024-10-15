print("\n*******************************************\n")

print("Weather Branch\n")

# Import necessary libraries: random for selecting a random weather condition, and sleep for adding delays
import random
from time import sleep

# Function to randomly choose a weather condition from a predefined list
def weather():
    weatherForcast = ["snowy", "blizzard", "rainy", "windy", "icy", "sunny"]  # List of possible weather conditions
    return random.choice(weatherForcast)  # Randomly select and return a weather condition

# Store the randomly selected weather condition in the weatherAlert variable
weatherAlert = weather()

# Define a dictionary mapping weather conditions to alarm updates and speed limits
weather_responses = {
    "snowy": {"delay": 30, "speed": 55},
    "blizzard": {"delay": 50, "speed": 45},
    "rainy": {"delay": 30, "speed": 65},
    "windy": {"delay": 5, "speed": 70},
    "icy": {"delay": 50, "speed": 30},
}

# Function to determine the vehicle's response based on the current weather condition
def vehicleResponseSystem():
    if weatherAlert in weather_responses:
        # Retrieve the delay and speed for the current weather condition
        response = weather_responses[weatherAlert]
        print(f"\nThe National Weather Service has updated our alarm by {response['delay']} minutes because of the forecast of {weatherAlert} weather conditions.\n")
        sleep(1)
        print(f"VRS system has been engaged only allowing you to drive {response['speed']}mph.")
    else:  # Default case for sunny or other non-listed weather conditions
        print(f"The National Weather Service is calling for {weatherAlert} skies. Drive carefully to get to your destination!")
        sleep(1)
        print("\nVRS has been disengaged...")

# Call the vehicle response system function to provide feedback based on the weather
vehicleResponseSystem()