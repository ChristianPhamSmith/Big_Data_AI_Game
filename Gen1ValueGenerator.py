import random
import mysql.connector

# This establishes the connection to the mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="P@$$w0rd",
    database="ai_data"
    )

## Hidden Layer 1st Gen Value Generation ##

for ai in range(1000):
    # This generates a random value that the AI will use to define where on the X-axis it should make a specific decision
    leftXValue = random.randrange(-1280, 1280)
    rightXValue = random.randrange(leftXValue, 1280)
    
    
    nearLeftJump = random.randrange(-1278, 0)
    midLeftJump = random.randrange(-1279, nearLeftJump)
    farLeftJump = random.randrange(-1280, midLeftJump)
    if nearLeftJump == 0:
        nearRightJump = random.randrange(1, 1278)
    else:
        nearRightJump = random.randrange(0, 1278)
    midRightJump = random.randrange(nearRightJump, 1279)
    farRightJump = random.randrange(midRightJump, 1280)

    # This sets a random movement direction for the three possible movements of go left, go right, and go nowhere.
    # 1 = left, 2= right, 3 = nowheres
    movementValues = [1,2,3]
    movement1 = movementValues[random.randrange(0, 3)]
    movementValues.remove(movement1)
    movement2 = movementValues[random.randrange(0, 2)]
    movementValues.remove(movement2)
    movement3 = movementValues[0]
    
    jump1 = random.randrange(0, 2)
    jump2 = random.randrange(0, 2)
    jump3 = random.randrange(0, 2)
    jump4 = random.randrange(0, 2)
    jump5 = random.randrange(0, 2)
    jump6 = random.randrange(0, 2)
    
    # This creates a cursor
    mycursor = db.cursor()
    
    # This puts an SQL insert statement into the cursor
    mycursor.execute(f"INSERT INTO ai_save (generation, score, movement1, movement2, movement3, leftXValue, rightXValue, jump1, jump2, jump3, jump4, jump5, jump6, nearLeftJump, midLeftJump, farLeftJump, nearRightJump, midRightJump, farRightJump) VALUES (1, 9000, {movement1}, {movement2}, {movement3}, {leftXValue}, {rightXValue}, {jump1}, {jump2}, {jump3}, {jump4}, {jump5}, {jump6}, {nearLeftJump}, {midLeftJump}, {farLeftJump}, {nearRightJump}, {midRightJump}, {farRightJump})")
    
    # This commits the statement into the database
    db.commit()
    
    print("AI " + str(ai) + " created")

print("Done!")