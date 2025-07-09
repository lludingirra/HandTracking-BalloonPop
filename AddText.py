import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Text Display") # Set window title

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
    
    # Load fonts and render text
    custom_font = pygame.font.Font('Resources/Marcellus-Regular.ttf', 100) # Custom font
    default_font = pygame.font.Font(None, 100) # Default system font
    
    welcome_text = custom_font.render("HELLO", True, (50, 50, 50))
    greeting_text = default_font.render("WORLD", True, (50, 50, 50))
    
    # Blit text onto the window
    game_window.blit(welcome_text, (350, 300))
    game_window.blit(greeting_text, (350, 400))
    
    # Update display
    pygame.display.update()
    # Control frame rate
    game_clock.tick(FPS)