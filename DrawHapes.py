import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Drawing Shapes") # Set window title

# Set frame rate
FPS = 30
game_clock = pygame.time.Clock()

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

    # Fill background with white color
    game_window.fill((255, 255, 255))
    
    # Define colors
    red, green, blue = (255, 0, 0), (0, 255, 0), (0, 0, 255)
    
    # Draw a polygon (hexagon)
    pygame.draw.polygon(game_window, red, ((491, 100), (788, 100), 
                                          (937, 357), (788, 614), 
                                          (491, 614), (342, 357)))
                        
    # Draw a circle
    pygame.draw.circle(game_window, green, (640, 350), 200)
    # Draw a line
    pygame.draw.line(game_window, blue, (468, 392), (812, 392), 10)
    # Draw a rectangle with border radius
    pygame.draw.rect(game_window, blue, (468, 307, 345, 70), border_radius=20)
    
    # Update display
    pygame.display.update()
    # Control frame rate
    game_clock.tick(FPS)