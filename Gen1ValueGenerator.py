import random
## Hidden Layer 1st Gen Value Generation ##

for ai in range(1000):
    # This generates a random value that the AI will use to define where on the X-axis it should make a specific decision
    leftXValue = random.randrange(-1280, 1280)
    rightXValue = random.randrange(leftXValue, 1280)

    # This sets a random movement direction for the three possible movements of go left, go right, and go nowhere.
    # 1 = left, 2= right, 3 = nowheres
    movementValues = [1,2,3]
    movement1 = movementValues[random.randrange(0, 2)]
    movementValues.remove(movement1)
    movement2 = movementValues[random.randrange(0, 1)]
    movementValues.remove(movement2)
    movement3 = movementValues[0]
    
print("Done!")