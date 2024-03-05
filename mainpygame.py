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

# Initialize Pygame
pygame.init()

# setup the display
width, height = 1280, 720
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("JoinTheClub")

# Character class
class Character:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 50
        self.color = (255, 215, 0, 255)  # Gold color for character
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

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
screen.blit(player, (200,200))
# Define the dimensions of each frame on the sprite sheet
        
# Create a list to store individual frames
frames = ['assets/fireball_1','assets/fireball_2','assets.fireball_3','assets.fireball_4','assets.fireball_5','assets.fireball_6','assets.fireball_7','assets.fireball_8']
# list is in 'assets folder        

# Create character instance
player = Character(width - 50, height - 50) 

# Create a wall instance
wall = Wall(200, 200, 50, 200)
  # Positioned at the bottom of the screen
floor = Wall(200, 400, 700, 50)
             
            
# Create goalpost instances
goalpost_left = Goalpost(50, 200, 10, 200)
goalpost_right = Goalpost(740, 200, 10, 200)


# Characte movement functions
def moveLeft():
    player.x -= 2
def moveRight():
    player.x += 2
def moveNowhere():
    player.x += 0

## Hidden Layer Value Generation ##
    
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

#starts the timer
start = time.time()

score = None

# This calculates the score
def scoreCalc(goalX, goalY):
    return goalX + goalY
    
# This creates a cursor
mycursor = db.cursor()
    
mycursor.execute("SELECT * FROM ai_save")

aiNumber = 0

# Main game loop
while True:
    
    for ai in mycursor:
        
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
            if keys[pygame.K_UP] and player.y > 0:  # Check if the character is within the top boundary
                player.y -= 2
            #if keys[pygame.K_DOWN]:
                #player.y += 2
    
    
            # Update character's rect for collision detection
            player.rect = pygame.Rect(player.x, player.y, player.width, player.height)

            # Check for collision between character and wall
            if player.rect.colliderect(wall.rect):
                # If collision occurs, adjust character position to prevent overlap
                if keys[pygame.K_LEFT]:
                    player.x = wall.rect.right
                elif keys[pygame.K_RIGHT]:
                    player.x = wall.rect.left
                elif keys[pygame.K_UP]:
                    player.y = wall.rect.bottom
            
            # Adds gravity
            if not player.rect.colliderect(floor.rect):
                player.y += 0.5

            # Check if character reaches the bottom of the screen
            if player.y > height - player.height:
                player.y = height - player.height  # Reset the character's y-coordinate to the bottom


            # Check for win condition (character within a certain distance to goalpost)
            if goalpost_left.distance_to_character(player) < 30 or goalpost_right.distance_to_character(player) < 30:
                win_screen()

            # Clear the screen
            screen.fill((255, 255, 255))  # White background

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
    
    
    # end #
        
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
        
            elif goalpost_rightX < int(ai[7]):
                if int(ai[5]) == 1:
                    moveLeft()
                elif int(ai[5]) == 2:
                    moveRight()
                elif int(ai[6]) == 3:
                    moveNowhere()
    
            # Checks if the time limit has been reached and if it has it will print the score and end the game.
            end = time.time()
            #print(end - start)
            if end - start >= 15:
                print(scoreCalc(goalpost_rightX, goalpost_rightY))
                player.x = width - 50
                player.y = height - 50
                start = time.time()
                reset = True