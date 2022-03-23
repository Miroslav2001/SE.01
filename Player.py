import time
import datetime


# Create class that acts as a countdown
def countdown():
    # Calculate the total number of seconds
    total_seconds = 10

    # While loop that checks if total_seconds reaches zero
    # If not zero, decrement total time by one second
    while total_seconds > 0:

        # Timer represents time left on countdown
        timer = datetime.timedelta(seconds=total_seconds)
        # Delays the program one second
        time.sleep(1)
        # Reduces total time by one second
        total_seconds -= 1
        print(timer/100000)

    print("Bzzzt! The countdown is at zero seconds!")


# Inputs for hours, minutes, seconds on timer

countdown()
