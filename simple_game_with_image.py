import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
screen_width = 1900
screen_height = 980
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Game With Image")

# Colors
yellow = (255, 255, 0)  # Background color (Yellow)

# Load the image
player_image = pygame.image.load('IRobot2.png')  # Load your image here
player_size = player_image.get_size()  # Get the size of the image
player_x = screen_width // 2 - player_size[0] // 2  # Centering the image on the screen
player_y = screen_height // 2 - player_size[1] // 2

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys
    keys = pygame.key.get_pressed()
    
    # Move character
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= 5  # Adjust speed as needed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size[0]:
        player_x += 5
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= 5
    if keys[pygame.K_DOWN] and player_y < screen_height - player_size[1]:
        player_y += 5

    # Fill screen with yellow (background)
    screen.fill(yellow)

    # Draw character (the loaded image)
    screen.blit(player_image, (player_x, player_y))  # Draw the image at the player's coordinates

    # Update display
    pygame.display.flip()

    # Control game frame rate
    pygame.time.Clock().tick(90)