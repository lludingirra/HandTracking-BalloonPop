import pygame
import cv2
import numpy as np
import random
from cvzone.HandTrackingModule import HandDetector
import time

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Balloon Pop Game") # Set window title

# Set frame rate
FPS = 30
game_clock = pygame.time.Clock()

# Initialize webcam capture
camera_capture = cv2.VideoCapture(0) # 0 for default camera
camera_capture.set(3, WINDOW_WIDTH) # Set camera width
camera_capture.set(4, WINDOW_HEIGHT) # Set camera height

# Load balloon image and get its rectangle
balloon_image = pygame.image.load("Resources/BalloonRed.png").convert_alpha()
balloon_rect = balloon_image.get_rect()
balloon_rect.x, balloon_rect.y = 500, 300 # Initial position of the balloon

# Game variables
balloon_speed = 5 # Initial speed of the balloon
game_score = 0 # Player's score
game_start_time = time.time() # Time when the game starts
total_game_time = 30 # Total duration of the game in seconds

# Initialize hand detector
# detectionCon: confidence threshold for detection (0.8 = 80%)
# maxHands: maximum number of hands to detect (1 for this game)
hand_detector = HandDetector(detectionCon=0.8, maxHands=1)

# Function to reset balloon position
def reset_balloon_position() :
    # Place balloon at a random X and below the screen
    balloon_rect.x = random.randint(100, WINDOW_WIDTH - 100)
    balloon_rect.y = WINDOW_HEIGHT + 50

# Main game loop
is_game_running = True
while is_game_running :
    
    # Handle Pygame events (e.g., closing the window)
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            is_game_running = False # End game loop
            pygame.quit() # Uninitialize Pygame
        # Check for 'q' key press to quit
        if event.type == pygame.KEYDOWN: # When a key is pressed
            if event.key == pygame.K_q: # If the pressed key is 'q'
                is_game_running = False # Stop the game loop
                pygame.quit() # Uninitialize Pygame

    # Calculate time remaining in the game
    time_remaining = int(total_game_time - (time.time() - game_start_time))

    if time_remaining < 0 : # If game time is over
        # Display game over screen
        game_window.fill((255, 255, 255)) # Fill background with white
        
        # Prepare and display score and "Time Up" messages
        font = pygame.font.Font('Resources/Marcellus-Regular.ttf', 50)
        score_text = font.render(f'Your Score: {game_score}', True, (255, 0, 255))
        time_up_text = font.render(f'Time Up', True, (255, 0, 255))
        
        # Center the text on the screen
        game_window.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, WINDOW_HEIGHT // 2 + 50))
        game_window.blit(time_up_text, (WINDOW_WIDTH // 2 - time_up_text.get_width() // 2, WINDOW_HEIGHT // 2 - 25))
        
    else : # If game is still active
        # Read frame from camera and detect hands
        success, camera_frame_bgr = camera_capture.read()
        if not success or camera_frame_bgr is None: # Handle camera read failure
            print("Failed to read frame from camera. Exiting.")
            is_game_running = False
            pygame.quit()
            continue

        hands_data, camera_frame_bgr = hand_detector.findHands(camera_frame_bgr) # Detect hands and update frame
        
        # Move the balloon upwards
        balloon_rect.y -= balloon_speed
        
        # If balloon goes off screen, reset its position and increase speed
        if balloon_rect.y < 0 :
            reset_balloon_position()
            balloon_speed += 1
            
        if hands_data : # If hands are detected
            first_hand = hands_data[0] # Get details of the first detected hand
            
            # Get landmark list (lmList) and access tip of index finger (typically landmark 8)
            landmarks = first_hand['lmList']
            # Safely get coordinates if landmark 8 exists
            if len(landmarks) > 8: 
                index_finger_tip_x, index_finger_tip_y = landmarks[8][0], landmarks[8][1] 
            else:
                # If landmark 8 is not available, set invalid coordinates to avoid errors
                index_finger_tip_x, index_finger_tip_y = -1, -1 
            
            # Check if index finger tip collides with the balloon
            if balloon_rect.collidepoint(index_finger_tip_x, index_finger_tip_y) :
                reset_balloon_position() # Reset balloon
                game_score += 10 # Increase score
                balloon_speed += 1 # Increase balloon speed
            
        # Convert OpenCV frame to Pygame surface for display
        frame_rgb = cv2.cvtColor(camera_frame_bgr, cv2.COLOR_BGR2RGB) # BGR to RGB
        frame_rotated = np.rot90(frame_rgb) # Rotate 90 degrees clockwise for correct orientation
        pygame_frame = pygame.surfarray.make_surface(frame_rotated).convert() 
        # Flip horizontally for mirror effect
        pygame_frame = pygame.transform.flip(pygame_frame, True, False) 
        
        # Blit camera feed and balloon onto the window
        game_window.blit(pygame_frame, (0, 0))
        game_window.blit(balloon_image, balloon_rect)

        # Display current score and time remaining
        font = pygame.font.Font('Resources/Marcellus-Regular.ttf', 50)
        score_display_text = font.render(f'Score: {game_score}', True, (255, 0, 255))
        time_display_text = font.render(f'Time: {time_remaining}', True, (255, 0, 255))
        
        game_window.blit(score_display_text, (35, 35))
        game_window.blit(time_display_text, (WINDOW_WIDTH - time_display_text.get_width() - 35, 35))
    
    # Update the entire display
    pygame.display.update()
    # Ensure game runs at specified FPS
    game_clock.tick(FPS)