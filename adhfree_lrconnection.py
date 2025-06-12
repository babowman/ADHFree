import random
import time
import os
import winsound

frequency = 2500 # Set Frequency To 2500 Hertz
duration = 500 # Set Duration To 1000 ms == 1 second

iters = input("How many iterations would you like? ")
iters = int(iters)
os.system("cls")
def generate_lr():
    return random.choice(["L", "R"])
i=0
while i<iters:
    i+=1
    winsound.Beep(frequency, duration)
    lr = generate_lr()
    print(f"{lr}")
    time.sleep(random.randint(1, 5))
    os.system("cls")