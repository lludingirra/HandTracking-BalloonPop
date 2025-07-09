import pygame
import cv2
import numpy as np

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("OpenCV Camera Feed") # Set window title

# Set frame rate
FPS = 30
game_clock = pygame.time.Clock()

# Initialize webcam capture
camera_capture = cv2.VideoCapture(0) # 0 for default camera
camera_capture.set(3, WINDOW_WIDTH) # Set camera width
camera_capture.set(4, WINDOW_HEIGHT) # Set camera height

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
            
    # Read frame from camera
    success, frame_bgr = camera_capture.read()
    if not success or frame_bgr is None: # Check if frame was read successfully
        print("Failed to read frame from camera. Exiting.")
        is_running = False
        pygame.quit()
        continue

    # Convert OpenCV BGR image to Pygame RGB format
    frame_rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
    # Rotate image for correct orientation in Pygame
    frame_rgb = np.rot90(frame_rgb)
    # Create Pygame surface from numpy array
    pygame_frame_surface = pygame.surfarray.make_surface(frame_rgb).convert()
    # Flip image horizontally for mirror effect (common for webcam)
    pygame_frame_surface = pygame.transform.flip(pygame_frame_surface, True, False)
    
    # Blit camera feed onto the window
    game_window.blit(pygame_frame_surface, (0, 0))
    
    # Update display
    pygame.display.update()
    # Control frame rate
    game_clock.tick(FPS)