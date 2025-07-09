import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Collision Detection") # Set window title

# Set frame rate
FPS = 30
game_clock = pygame.time.Clock()

# Load images
background_image = pygame.image.load("Resources/BackgroundBlue.jpg").convert()
balloon_red_image = pygame.image.load("Resources/BalloonRed.png").convert_alpha()

# Create rect for the balloon image
balloon_rect = balloon_red_image.get_rect()
balloon_rect.x, balloon_rect.y = 100, 300 # Initial position for balloon rect

# Create a new rectangle for collision detection
collision_rect = pygame.Rect(500, 0, 200, 200)

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

    # Check for collision between the two rectangles and print result
    print(balloon_rect.colliderect(collision_rect))
    
    # Move the balloon rect
    balloon_rect.x += 2
    
    # Blit background image
    game_window.blit(background_image, (0, 0))
    # Optionally draw rectangles (uncomment to visualize)
    # pygame.draw.rect(game_window, (0,255,0), balloon_rect)
    # pygame.draw.rect(game_window, (0,255,0), collision_rect)
    # Blit the balloon image
    game_window.blit(balloon_red_image, balloon_rect)
    
    # Update display
    pygame.display.update()
    # Control frame rate
    game_clock.tick(FPS)