import random
from time import sleep

# Simulate gas level gauge by randomly choosing a gas level from the list
def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

# Simulate gas station selection
def gasStations():
    gasStationsList = ["BP", "Shell", "Meijer", "Sams Club", "Marathon", "Mobile", "Speedway", "Circle K"]
    return random.choice(gasStationsList)

# Provide alerts based on gas level
def gasLevelAlert():
    # Get the current gas level and nearest gas station
    gasLevelIndicator = gasLevelGauge()
    nearestStation = gasStations()

    # Distance to gas stations based on gas level
    distance = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }

    # Mapping gas levels to responses
    responses = {
        "Empty": "***WARNING - YOU ARE ON EMPTY***\nCalling Triple AAA",
        "Low": f"***Your gas tank is extremely low, checking GPS for the closest gas station***\nThe closest gas station is {nearestStation} which is {distance['Low']} miles away.",
        "Quarter Tank": f"***Your gas tank is on a quarter of a tank, checking GPS for a gas station***\nThe closest gas station is {nearestStation} which is {distance['Quarter Tank']} miles away.",
        "Half Tank": "***Your gas tank is half full, enough to get to your destination***",
        "Three Quarter Tank": "***Your gas tank is three quarters full***",
        "Full Tank": "***Your gas tank is full! Have a nice day!***"
    }

    # Print the response based on the gas level
    print(responses.get(gasLevelIndicator))

    # Add a slight delay to mimic a real-time process
    if gasLevelIndicator in ["Empty", "Low", "Quarter Tank"]:
        sleep(1)

# Call the gasLevelAlert() function to simulate the gas level check
print("\n*******************************************************************************\n")
print("Gasoline Branch\n")
gasLevelAlert()