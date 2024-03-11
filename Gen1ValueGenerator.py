import random
import mysql.connector

# This establishes the connection to the mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="P@$$w0rd",
    database="ai_data"
    )

## 1st Gen Value Generation ##


# This for loop is used to generate each AI. It is currentlly set to generate 250 AIs
for ai in range(250):
    # The X-values are the points on the X-axis that the AI uses to create zones where the AI will make movement decisions based on if the goal post is within that zone
    leftXValue = random.randrange(-1280, 1280)
    rightXValue = random.randrange(leftXValue, 1280)
    
    # These left and right jump points are like the X-values above but for jumping
    # There are more of them and they are supposed to be to the left and right of the player so that the AI can be more precise in its descision making
    nearLeftJump = random.randrange(-1278, 1)
    midLeftJump = random.randrange(-1279, nearLeftJump)
    farLeftJump = random.randrange(-1280, midLeftJump)
    nearRightJump = random.randrange(1, 1278)
    midRightJump = random.randrange(nearRightJump, 1279)
    farRightJump = random.randrange(midRightJump, 1280)

    # This sets a random movement direction for the three possible movements of go left, go right, and go nowhere
    # 1 = left, 2 = right, 3 = nowheres
    # movement1 = left zone, movement2 = center zone, movement3 = right zone
    movement1 = random.randrange(0, 3)
    movement2 = random.randrange(0, 3)
    movement3 = random.randrange(0, 3)
    
    # This sets the jump values to randomly be set to either 1 or 0
    # 0 = no jump, 1 = jump
    # jump1 = nearLeftJump, jump2 = midLeftJump, jump3 = farLeftJump, jump4 = nearRightJump, jump5 = midRightJump, jump6 = farRightJump, jump7 = centerJump
    jump1 = random.randrange(0, 2)
    jump2 = random.randrange(0, 2)
    jump3 = random.randrange(0, 2)
    jump4 = random.randrange(0, 2)
    jump5 = random.randrange(0, 2)
    jump6 = random.randrange(0, 2)
    jump7 = random.randrange(0, 2)
    
    # This creates a cursor that is used to access the data in the database
    mycursor = db.cursor()
    
    # This puts an SQL insert statement into the cursor that inserts the AI values into the ai_save table
    mycursor.execute(f"INSERT INTO ai_save (generation, score, movement1, movement2, movement3, leftXValue, rightXValue, jump1, jump2, jump3, jump4, jump5, jump6, nearLeftJump, midLeftJump, farLeftJump, nearRightJump, midRightJump, farRightJump, jump7) VALUES (1, 9000, {movement1}, {movement2}, {movement3}, {leftXValue}, {rightXValue}, {jump1}, {jump2}, {jump3}, {jump4}, {jump5}, {jump6}, {nearLeftJump}, {midLeftJump}, {farLeftJump}, {nearRightJump}, {midRightJump}, {farRightJump}, {jump7})")
    
    # This commits the statement into the database
    db.commit()
    
    # This is a print statement that tells you which ai was just created
    print("AI " + str(ai + 1) + " created")

# This informs the user that the AI is done generating
print("Done!")