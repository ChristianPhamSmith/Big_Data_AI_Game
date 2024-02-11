import pygame
import sys
import math

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
    pygame.time.delay(10000)  # Display the win screen for 10000 milliseconds (10 seconds)
    pygame.quit()
    sys.exit()

# Load animated chracter sprites
        
# Define the dimensions of each frame on the sprite sheet
        
# Create a list to store individual frames
        
# Create character instance
player = Character(400,300) 

# Create a wall instance
wall = Wall (200, 200, 50, 200)

# Create goalpost instances
goalpost_left = Goalpost(50, 200, 10, 200)
goalpost_right = Goalpost(740, 200, 10, 200)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle character movements (for example, using arrow keys)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 2
    if keys[pygame.K_RIGHT]:
        player.x += 2
    if keys[pygame.K_UP]:
        player.y -= 2
    if keys[pygame.K_DOWN]:
        player.y += 2

    # Update character's rect for collision detection
    player.rect = pygame.Rect(player.x, player.y, player.width, player.height)

    # Check for collision between character and wall
    if player.rect.colliderect(wall.rect):
        # If collision occurs, adjust character position to prevent overlap
        if keys[pygame.K_LEFT]:
            player.x = wall.rect.right
        if keys[pygame.K_RIGHT]:
            player.x = wall.rect.left - player.width
        if keys[pygame.K_UP]:
            player.y = wall.rect.bottom
        if keys[pygame.K_DOWN]:
            player.y = wall.rect.top - player.height

    # Check for win condition (character within a certain distance to goalpost)
    if goalpost_left.distance_to_character(player) < 30 or goalpost_right.distance_to_character(player) < 30:
        win_screen()

    # Clear the screen
    screen.fill((255, 255, 255))  # White background

    # Draw the wall
    wall.draw(screen)

    # Draw the goalposts
    goalpost_left.draw(screen)
    goalpost_right.draw(screen)

    # Draw the character
    player.draw()

    # Update the display
    pygame.display.flip()
