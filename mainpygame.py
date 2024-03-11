import pygame
import sys
import math
import random
import time
import mysql.connector

# This establishes the connection to the mysql server
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="P@$$w0rd",
    database="ai_data"
    )

#clock
#clock = pygame.time.clock()
#FPS = 150 # adjust this value as needed

# setup the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JoinTheClub")

#charachterAnimation
class CharacterAnimation:
    def __init__(self, frames, frame_duration=100):
        self.frames = frames
        self.frame_index = 0
        self.frame_duration = frame_duration
        self.last_frame_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time > self.frame_duration:
            self.frame_index = (self.frame_index + 1) % len(self.frames)
            self.last_frame_time = current_time

    def get_current_frame(self):
        return self.frames[self.frame_index]


# Character class
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (255, 215, 0, 255)  # Gold color for character
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.animation = CharacterAnimation(player_frames)

    def draw(self):
        #pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))
        current_frame = self.animation.get_current_frame()
        screen.blit(current_frame, (self.x, self.y))

    def update_animation(self):
        self.animation.update()

# Define The Background Class
# class Background:
#     def __init__(self, image_path):
#         self.image = pygame.image.load(image_path)
#         self.rect = self.image.get_rect()
#     def draw(self, screen):
#         screen.blit(self.image, self.rect)

# Wall Class
class Wall:
    def __init__(self, x, y, width, height, color=(0, 0, 255)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Goalpost Class
class Goalpost:
    def __init__(self, x, y, width, height, color=(0, 255, 0)):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def distance_to_character(self, character):
        # Calculate distance between the goalpost and character using Pythagorean theorem
        dx = self.x - character.x
        dy = self.y - character.y
        return math.sqrt(dx ** 2 + dy ** 2)
    
# Initialize Pygame
pygame.init()

# Win state screen function
def win_screen():
    font = pygame.font.Font(None, 74)
    text = font.render("You Win!", True, (0, 0, 0))
    screen.blit(text, (width // 2 - text.get_width() // 2, height // 2 - text.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)  # Display the win screen for 10000 milliseconds (10 seconds)
    pygame.quit()
    sys.exit()

# Load animated chracter sprites
player = pygame.transform.scale(pygame.image.load('assets/fireball_1.png'), (150,150))   
player_frames = [pygame.image.load(f"assets/fireball_{i}.png") for i in range(1, 9)]
screen.blit(player, (200,200))
# Define the dimensions of each frame on the sprite sheet
        
# Create a list to store individual frames
frames = ['assets/fireball_1','assets/fireball_2','assets.fireball_3','assets.fireball_4','assets.fireball_5','assets.fireball_6','assets.fireball_7','assets.fireball_8']
# list is in 'assets folder        

# Create character instance
<<<<<<< HEAD
player = Character(width - 75, height - 75) 
=======
player = Character(0, height - 50) 
>>>>>>> 8cf83a3eff215ce266411fb68e8099ce30ebcc4e

# Create a wall instance
wall = Wall(200, 520, 50, 200)
  # Positioned at the bottom of the screen
<<<<<<< HEAD
floor = Wall(200, 400, 700, 50)
         
=======
floor = Wall(200, 520, 700, 50)
             
            
>>>>>>> 8cf83a3eff215ce266411fb68e8099ce30ebcc4e
# Create goalpost instances
goalpost_left = Goalpost(50, 200, 10, 200)
goalpost_right = Goalpost(840, 320, 10, 200)

# Characte movement functions
def moveLeft():
    # Check for collision between character and wall
    wallx = wall.x
    if not wall.rect.colliderect(player.x - 1, player.y, player.width, player.height) and not floor.rect.colliderect(player.x - 1, player.y, player.width, player.height):
        player.x -= 1
def moveRight():
    wallx = wall.x
    if not wall.rect.colliderect(player.x + 1, player.y, player.width, player.height) and not floor.rect.colliderect(player.x + 1, player.y, player.width, player.height):
        player.x += 1
def moveNowhere():
    player.x += 0


jumpHeight = 10000000
jumping = False

## Hidden Layer Value Generation ##
    
# This generates a random value that the AI will use to define where on the X-axis it should make a specific decision
leftXValue = random.randrange(-1280, 1280)
rightXValue = random.randrange(leftXValue, 1280)

#starts the timer
start = time.time()

score = None

# This calculates the score
def scoreCalc(goalX, goalY):
    calculatedScore = abs(goalX) + abs(goalY)
    return calculatedScore

# This generated a random number to decide if each movement variable should mutate
def mutationDice():
    number = random.randrange(1, 10)
    if number > 8:
        return True
    if number <= 8:
        return False

# These are here so that these variables exist for when creating new AIs
generation = 1
score = None
movement1 = None
movement2 = None
movement3 = None
leftXValue = None
rightXValue = None
    
# This creates a cursor
mycursor = db.cursor()
    


aiNumber = 0
aiGeneration = 0

topTen = {}

# Create an instance of the Background class
#background = Background('assets/bg_image/bg_img.png')

# Main game loop
while True:
    
    aiGeneration += 1
    
    #Selects the AIs for that are in the latest generation
    # If you are testing or changing things with the AI I recomend that you write LIMIT 20 at the end of the SQL statement
    mycursor.execute(f"SELECT * FROM ai_save Where Generation = {aiGeneration} LIMIT 20")
    aiSaveData = mycursor.fetchall()
    
    for ai in aiSaveData:
        
        aiNumber += 1
        print("AI #" + str(aiNumber) + " is playing the game")
        
        reset = False
        
        while reset == False:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            # Handle character movements (for example, using arrow keys)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x > 0:  # Check if the character is within the left boundary
                moveLeft()
            if keys[pygame.K_RIGHT] and player.x < width - player.width:  # Check if the character is within the right boundary
                moveRight()
            if keys[pygame.K_UP] and player.y > 0 and jumping == False:  # Check if the character is within the top boundary
                jumpHeight = player.y - 200
                jumping = True
            
            # When jumping the player goes up intil they reach the jump height and then the jump height is reset so that gravity can bring the player down
            if jumping == True and player.y > jumpHeight and not wall.rect.colliderect(player.x, player.y -1.3, player.width, player.height) and not floor.rect.colliderect(player.x, player.y -1.3, player.width, player.height):
                player.y -= 1.3
            elif (jumping == True and player.y <= jumpHeight) or not wall.rect.colliderect(player.x, player.y -1.3, player.width, player.height) or not floor.rect.colliderect(player.x, player.y -1.3, player.width, player.height):
                jumpHeight = 2000
            
            # Checks if player is no longer jumping so that jumping can be set to false
            if player.y == 670 or wall.rect.colliderect(player.x, player.y + 0.5, player.width, player.height) or floor.rect.colliderect(player.x, player.y + 0.5, player.width, player.height):
                jumping = False
    
    
            # Update character's rect for collision detection
            player.rect = pygame.Rect(player.x, player.y, player.width, player.height)

            # Check for collision between character and wall
            if player.rect.colliderect(wall.rect):
                # If collision occurs, adjust character position to prevent overlap
                if player.x > wall.x:
                    player.x = wall.rect.right
                elif player.x < wall.x:
                    player.x = wall.rect.left
                elif keys[pygame.K_UP]:
                    player.y = wall.rect.bottom
            
            # Adds gravity
            if not player.rect.colliderect(floor.rect) and not wall.rect.colliderect(player.x, player.y + 0.5, player.width, player.height) and not floor.rect.colliderect(player.x, player.y + 0.5, player.width, player.height):
                player.y += 0.5

            # Check if character reaches the bottom of the screen
            if player.y > height - player.height:
                player.y = height - player.height  # Reset the character's y-coordinate to the bottom


            # Check for win condition (character within a certain distance to goalpost)
            if goalpost_left.distance_to_character(player) < 30 or goalpost_right.distance_to_character(player) < 30:
                #win_screen()
                start += 10

            # Clear the screen
            screen.fill((255, 255, 255))  # White background

            # Draw the background
            #background.draw(screen)

            # Draw the walls
            wall.draw(screen)
            floor.draw(screen)

            # Draw the goalposts
            goalpost_left.draw(screen)
            goalpost_right.draw(screen)

            # Draw the character
            player.draw()

            # Update the display
            pygame.display.flip()

            #cap the frame rate to
            #clock.tick(150)
    
            ## Input layer ##
    
            # Player location input
            playerX = player.rect.left
            playerY = player.rect.top
            #print(str(playerX) + ", " + str(playerY))

            # Goal left location input
            goalpost_leftX = goalpost_left.rect.left - playerX
            goalpost_leftY = goalpost_left.rect.top - playerY
            #print(str(goalpost_leftX) + ", " + str(goalpost_leftY))
    
            # Goal right location input
            goalpost_rightX = goalpost_right.rect.left - playerX
            goalpost_rightY = goalpost_right.rect.top - playerY
            #print(str(goalpost_rightX) + ", " + str(goalpost_rightY))
    
            # Wall location input
            wallX = wall.rect.left - playerX
            wallY = wall.rect.top - playerY
            #print(str(wallX) + ", " + str(wallY))
    
            # floor location input
            floorX = floor.rect.left - playerX
            floorY = floor.rect.top - playerY
            #print(str(floorX) + ", " + str(floorY))
    
    
            ## Hidden Layer ##
            
        
            # This is the hidden layer node for the right goalpost 
            if goalpost_rightX < int(ai[6]):
                if int(ai[3]) == 1:
                    moveLeft()
                elif int(ai[3]) == 2:
                    moveRight()
                elif int(ai[3]) == 3:
                    moveNowhere()
        
            elif goalpost_rightX >= int(ai[6]) and goalpost_rightX <= int(ai[7]):
                if int(ai[4]) == 1:
                    moveLeft()
                elif int(ai[4]) == 2:
                    moveRight()
                elif int(ai[4]) == 3:
                    moveNowhere()
        
            elif goalpost_rightX > int(ai[7]):
                if int(ai[5]) == 1:
                    moveLeft()
                elif int(ai[5]) == 2:
                    moveRight()
                elif int(ai[6]) == 3:
                    moveNowhere()
                    
            # Far Left
            if goalpost_rightX >= int(ai[16]) and int(ai[10]) == 1 and jumping == False:
                jumpHeight = player.y - 200
                jumping = True
            # Mid Left
            if goalpost_rightX < int(ai[16]) and goalpost_rightX >= int(ai[15]) and int(ai[9]) == 1 and jumping == False:
                jumpHeight = player.y - 200
                jumping = True
            # Near Left
            if goalpost_rightX < int(ai[15]) and goalpost_rightX >= int(ai[14]) and int(ai[8]) == 1 and jumping == False:
                jumpHeight = player.y - 200
                jumping = True
            # Center
            if goalpost_rightX < int(ai[14]) and goalpost_rightX >= int(ai[17]) and int(ai[20]) == 1 and jumping == False:
                jumpHeight = player.y - 200
                jumping = True
            # Near Right
            if goalpost_rightX < int(ai[17]) and goalpost_rightX >= int(ai[18]) and int(ai[11]) == 1 and jumping == False:
                jumpHeight = player.y - 200
                jumping = True
            # Mid Right
            if goalpost_rightX < int(ai[18]) and goalpost_rightX >= int(ai[19]) and int(ai[12]) == 1 and jumping == False:
                jumpHeight = player.y - 200
                jumping = True
            # Far Right
            if goalpost_rightX < int(ai[19]) and int(ai[12]) == 1 and jumping == False:
                jumpHeight = player.y - 200
                jumping = True
    
            # Checks if the time limit has been reached and if it has it will print the score and end the game.
            end = time.time()
            #print(end - start)
            if end - start >= 10:
                
                if goalpost_left.distance_to_character(player) < 30 or goalpost_right.distance_to_character(player) < 30:
                    score = -1
                else:
                    score = scoreCalc(goalpost_rightX, goalpost_rightY)
                aiID = ai[0]
                
                #prints the AI's score
                print("AI #" + str(aiNumber) + " scored: " + str(score))
                
                # Adds the AI's id and score to the topTen dictionary
                topTen.update({aiID:score})
                # Prints the topTen AI's scores
                print(sorted(topTen.items(), key=lambda x: x[1], reverse=False)[:10])
                # Updates each AI so that they have a real score
                mycursor.execute(f"UPDATE ai_save SET score = {score} WHERE id = {aiID}")
                db.commit()
                
                # Resets the player
                player.x = 0
                player.y = height - 50
                start = time.time()
                reset = True
    for survivor in sorted(topTen.items(), key=lambda x: x[1], reverse=False)[:10]:
        idNumber = survivor[0]
        mycursor.execute(f"SELECT * FROM ai_save WHERE id = {idNumber}")
        survivorData = mycursor
        
        for ai in survivorData:
            print(ai)
            for child in range(100):
                generation = ai[1] + 1
                score = 9000
                movement1 = ai[3]
                movement2 = ai[4]
                movement3 = ai[5]
                leftXValue = ai[6]
                rightXValue = ai[7]
                jump1 = ai[8]
                jump2 = ai[9]
                jump3 = ai[10]
                jump4 = ai[11]
                jump5 = ai[12]
                jump6 = ai[13]
                jump7 = ai[20]
                nearLeftJump = ai[14]
                midLeftJump = ai[15]
                farLeftJump = ai[16]
                nearRightJump = ai[17]
                midRightJump = ai[18]
                farRightJump = ai[19]
                
                if mutationDice() == True:
                    movement1 = random.randrange(1,3)
                if mutationDice() == True:
                    movement2 = random.randrange(1,3)
                if mutationDice() == True:
                    movement3 = random.randrange(1,3)
                if mutationDice() == True:
                    leftXValue = random.randrange(-1280, rightXValue)
                if mutationDice() == True:
                    rightXValue = random.randrange(leftXValue, 1280)
                if mutationDice() == True:
                    jump1 = random.randrange(0,2)
                if mutationDice() == True:
                    jump2 = random.randrange(0,2)
                if mutationDice() == True:
                    jump3 = random.randrange(0,2)
                if mutationDice() == True:
                    jump4 = random.randrange(0,2)
                if mutationDice() == True:
                    jump5 = random.randrange(0,2)
                if mutationDice() == True:
                    jump6 = random.randrange(0,2)
                if mutationDice() == True:
                    jump7 = random.randrange(0,2)
                if mutationDice() == True:
                    nearLeftJump = random.randrange(midLeftJump, 0)
                if mutationDice() == True:
                    midLeftJump = random.randrange(farLeftJump, nearLeftJump)
                if mutationDice() == True:
                    farLeftJump = random.randrange(-1280, midLeftJump)
                if mutationDice() == True:
                    if nearLeftJump == 0:
                        nearRightJump = random.randrange(1, midRightJump)
                    else:
                        nearRightJump = random.randrange(0, midRightJump)
                if mutationDice() == True:
                    midRightJump = random.randrange(nearRightJump, farRightJump)
                if mutationDice() == True:
                    farRightJump = random.randrange(midRightJump, 1280)
                    
                
                
                # This inserts the AI children into the database
                mycursor.execute(f"INSERT INTO ai_save (Generation, score, movement1, movement2, movement3, leftXValue, rightXValue, jump1, jump2, jump3, jump4, jump5, jump6, jump7, nearLeftJump, midLeftJump, farLeftJump, nearRightJump, midRightJump, farRightJump) VALUES ({generation}, {score}, {movement1}, {movement2}, {movement3}, {leftXValue}, {rightXValue}, {jump1}, {jump2}, {jump3}, {jump4}, {jump5}, {jump6}, {jump7}, {nearLeftJump}, {midLeftJump}, {farLeftJump}, {nearRightJump}, {midRightJump}, {farRightJump})")
                
                db.commit()
                    
                print(generation, score, movement1, movement2, movement3, leftXValue, rightXValue)
                    