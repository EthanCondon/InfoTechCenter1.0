import sys  # Imports the sys module to use for system-specific parameters and functions
import time  # Imports the time module to handle timing events like delays

# ANSI escape sequences for colors
RESET = "\033[0m"  # Resets color to default
GREEN = "\033[92m"  # Bright green
RED = "\033[91m"  # Red
YELLOW = "\033[93m"  # Yellow
CYAN = "\033[96m"  # Bright cyan

# Prints the welcome message when the program starts with green color
print(f"{GREEN}\nWelcome To InfoTechCenter V1.0\n{RESET}")

TimeToSleep = 1.5 # Variable to se the time library to 1.5 seconds when called
time.sleep(TimeToSleep) # Calling the sleep library with the variable TimeToSleep's value

x = 0  # Initialize counter variable to control the while loop
ellipsis = 0  # Initialize ellipsis counter for the dots displayed in the booting message

# Loop to simulate system booting by printing a message repeatedly
while x != 20:
    x += 1  # Increment the loop counter
    # Create the booting message with increasing number of dots (ellipsis)
    message = (f"{YELLOW}InfoTech Center System Booting" + "." * ellipsis + RESET)
    ellipsis += 1  # Increment the ellipsis counter to add more dots in each iteration
    # Overwrite the same line with updated message (using \r to return to the beginning of the line)
    sys.stdout.write("\r" + message)
    time.sleep(.5)  # Wait for 0.5 seconds before the next iteration
    # Reset the ellipsis counter after 3 dots (so it cycles from 0 to 3)
    if ellipsis == 4:
        ellipsis = 0
    # Check if the loop has run 20 times
    if x == 20:
        # Print final message indicating system boot is complete with red color
        print(f"\n\n{RED}Operating System Booted Up - Retina Scanned - Access Granted{RESET}")

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
