import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Image Transformations") # Set window title

# Set frame rate
FPS = 30
game_clock = pygame.time.Clock()

# Load images
background_image = pygame.image.load("Resources/BackgroundBlue.jpg").convert()
balloon_red_image = pygame.image.load("Resources/BalloonRed.png").convert_alpha()

# Apply initial image transformations
# Rotates image by 90 degrees and scales to 0.3 (30%)
balloon_red_image = pygame.transform.rotozoom(balloon_red_image, 90, 0.3)
# To rotate by 90 degrees without zoom: # imgBalloonRed = pygame.transform.rotate(imgBalloonRed, 90)
# To flip horizontally: # imgBalloonRed = pygame.transform.flip(imgBalloonRed, True, False)

# Main game loop
is_running = True
while is_running :
    # Event handling
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            is_running = False # End loop on quit event
            pygame.quit() # Uninitialize Pygame
        # Check for 'q' key press to quit
        if event.type == pygame.KEYDOWN: # When a key is pressed
            if event.key == pygame.K_q: # If the pressed key is 'q'
                is_running = False # Stop the game loop
                pygame.quit() # Uninitialize Pygame
            
    # Example of runtime scaling (uncomment to see effect)
    # imgBalloonRed = pygame.transform.scale(imgBalloonRed, (50,100))
    # imgBalloonRed = pygame.transform.smoothscale(imgBalloonRed, (50,100))

    # Blit background image
    game_window.blit(background_image, (0, 0))
    # Blit transformed balloon image
    game_window.blit(balloon_red_image, (200, 300))
    
    # Update display
    pygame.display.update()
    # Control frame rate
    game_clock.tick(FPS)