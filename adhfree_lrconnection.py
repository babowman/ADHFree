import random
import time
import os
import winsound

frequency = 2500 # Set Frequency To 2500 Hertz
duration = 500 # Set Duration To 1000 ms == 1 second

# Here we will get the desired input from the user; check validity of input (must be integer)
iters = input("How many iterations would you like? ")
if iters == "":
    raise ValueError("Input cannot be empty.")
    print()
if not iters.isdigit():
    raise ValueError("Input must be an integer.")
    print()
else:
    iters = int(iters)
    if iters < 1:
        raise ValueError("Input must be a positive integer.")
        print()
    print(f"You have chosen {iters} iterations.")

# Let's prep the console for the exercise interface here
os.system("cls") # clear the console screen
def generate_lr():
    return random.choice(["L", "R"])
print("Get ready for the exercise! Press any key to start...")
input()  # Wait for user to press any key to start
os.system("cls")  # Clear the console again before starting the exercise

# Now we should loop through the determined number of iterations to let the exercise play out
i=0
while i<iters:
    i+=1
    winsound.Beep(frequency, duration)
    lr = generate_lr()
    print(f"{lr}")
    time.sleep(random.randint(1, 5))
    os.system("cls")