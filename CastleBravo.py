import sys  # Imports the sys module to use for system-specific parameters and functions
import time  # Imports the time module to handle timing events like delays

# Prints the welcome message when the program starts
print("\nWelcome To InfoTechCenter V1.0\n")

x = 0  # Initialize counter variable to control the while loop
ellipsis = 0  # Initialize ellipsis counter for the dots displayed in the booting message

# Loop to simulate system booting by printing a message repeatedly
while x != 20:
    x += 1  # Increment the loop counter
    # Create the booting message with increasing number of dots (ellipsis)
    message = ("InfoTech Center System Booting" + "." * ellipsis)
    ellipsis += 1  # Increment the ellipsis counter to add more dots in each iteration
    # Overwrite the same line with updated message (using \r to return to the beginning of the line)
    sys.stdout.write("\r" + message)
    time.sleep(.5)  # Wait for 0.5 seconds before the next iteration
    # Reset the ellipsis counter after 3 dots (so it cycles from 0 to 3)
    if ellipsis == 4:
        ellipsis = 0
    # Check if the loop has run 20 times
    if x == 20:
        # Print final message indicating system boot is complete
        print("\n\nOperating System Booted Up - Retina Scanned - Access Granted")
