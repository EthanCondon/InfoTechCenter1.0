# Print a decorative line separator
print("\n*******************************************************************************\n")

# Print the branch information
print("Gasoline Branch\n")

# Import the 'random' module for generating random values and 'sleep' from the 'time' module for delays
import random
from time import sleep


# Define a function that simulates the gas level gauge by randomly choosing from predefined levels
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)


# Define a function that simulates a random gas station name from a list of stations
def gasStations():
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)


# Define a function that provides alerts based on the gas level and the distance to the nearest gas station
def gasLevelAlert():
    # Generate a random distance to the gas station if the tank is Low
    milesToGasStationLow = round(random.uniform(1, 25), 1)
    # Generate a random distance to the gas station if the tank is at a Quarter Tank
    milesToGasStationQuarterTank = round(random.uniform(25.1, 50), 1)

    # Call gasLevelGauge() to get the current gas level
    gasLevelIndicator = gasLevelGauge()

    # Check if the gas tank is Empty
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(1)
        print("Calling Triple AAA")  # Simulate calling for help

    # Check if the gas tank is Low
    elif gasLevelIndicator == "Low":
        print("***Your gas tank is extremely low, checking GPS for the closest gas station***\n")
        sleep(1)
        # Display the nearest gas station and the distance
        print("The closest gas station is ", gasStations(), " which is ", milesToGasStationLow, " miles away.")

    # Check if the gas tank is at a Quarter Tank
    elif gasLevelIndicator == "Quarter Tank":
        print("***Your gas tank is on a quarter of a tank, checking GPS for a gas station***\n")
        sleep(1)
        # Display the nearest gas station and the distance
        print("The closest gas station is ", gasStations(), " which is ", milesToGasStationQuarterTank, " miles away.")

    # Check if the gas tank is at Half Tank
    elif gasLevelIndicator == "Half Tank":
        print("***Your gas tank is a half a tank full, enough to get to your destination***")

    # Check if the gas tank is at Three Quarter Tank
    elif gasLevelIndicator == "Three Quarter Tank":
        print("***Your gas tank is three quarters of a tank full***")

    # Otherwise, the gas tank must be Full
    else:
        print("***Your gas tank is full! Have a nice day!***")


# Call the gasLevelAlert() function to simulate the gas level check and response
gasLevelAlert()
