import pygame

# Initialize Pygame
pygame.init()

# Set window dimensions
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
game_window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("GUI Design Project") # Set window title

# Set frame rate
FPS = 30
game_clock = pygame.time.Clock()

# Define color palette
colors = {"lightGreen": (189, 209, 197),
          "lightOrange": (238, 204, 140),
          "lightPink": (232, 178, 152),
          "darkPink": (211, 162, 157),
          "darkGreen": (158, 171, 162),
          "darkGray": (128, 126, 126),
          "lightGray": (204, 204, 204),
          "darkBrown": (89, 61, 61),
          "white": (255, 255, 255),
          "black": (0, 0, 0),
         }

# Load GUI images
background_image = pygame.image.load("Resources/Project - GUI/background.png").convert()
design_image = pygame.image.load("Resources/Project - GUI/design.png").convert_alpha()

icon1_image = pygame.image.load("Resources/Project - GUI/icon1.png").convert_alpha()
icon2_image = pygame.image.load("Resources/Project - GUI/icon2.png").convert_alpha()
icon3_image = pygame.image.load("Resources/Project - GUI/icon3.png").convert_alpha()
icon4_image = pygame.image.load("Resources/Project - GUI/icon4.png").convert_alpha()
icon5_image = pygame.image.load("Resources/Project - GUI/icon5.png").convert_alpha()

shadow_image = pygame.image.load("Resources/Project - GUI/shadow.png").convert_alpha()

toggle_on_image = pygame.image.load("Resources/Project - GUI/toggleOn.png").convert_alpha()
toggle_off_image = pygame.image.load("Resources/Project - GUI/toggleOff.png").convert_alpha()

# Define pad properties
display_pads = [{"no": 1, "color": colors['lightGreen'], "text": "Original", "icon": icon2_image},
                {"no": 2, "color": colors['lightOrange'], "text": "Gray Scale", "icon": icon3_image},
                {"no": 3, "color": colors['lightPink'], "text": "Edges", "icon": icon4_image},
                {"no": 4, "color": colors['darkPink'], "text": "Contours", "icon": icon5_image}]

# Function to draw a single window pad (e.g., image display area)
def draw_window_pad(position, color, text, icon) :
    x_pos, y_pos, width_val, height_val = position
    game_window.blit(shadow_image, (x_pos, y_pos + height_val - 66))
    pygame.draw.rect(game_window, color, (x_pos, y_pos, width_val, 64),
                     border_top_left_radius=10,
                     border_top_right_radius=10)
    
    pygame.draw.rect(game_window, colors['white'], (x_pos, y_pos + 64, width_val, height_val - 87),
                     border_bottom_left_radius=10,
                     border_bottom_right_radius=10)
    
    game_window.blit(icon, (x_pos + 20, y_pos + 12))
    
    font = pygame.font.Font('Resources/Marcellus-Regular.ttf', 20)
    rendered_text = font.render(text, True, colors['darkBrown'])
    game_window.blit(rendered_text, (x_pos + 82, y_pos + 20))
    
# Function to draw the filter settings pad
def draw_filter_pad() :
    draw_window_pad((75, 57, 312, 602), colors['darkGreen'], "Filter", icon1_image)

    font = pygame.font.Font('Resources/Marcellus-Regular.ttf', 20)
    
    # Draw filter toggles
    text_grayscale = font.render("Gray Scale", True, colors['darkBrown'])
    game_window.blit(text_grayscale, (106, 165))
    game_window.blit(toggle_on_image, (283, 164))

    text_edges = font.render("Edges", True, colors['darkBrown'])
    game_window.blit(text_edges, (106, 165 + 60))
    game_window.blit(toggle_off_image, (283, 164 + 60))

    text_contours = font.render("Contours", True, colors['darkBrown'])
    game_window.blit(text_contours, (106, 165 + 60 * 2))
    game_window.blit(toggle_off_image, (283, 164 + 60 * 2))

    text_blur = font.render("Blur", True, colors['darkBrown'])
    game_window.blit(text_blur, (106, 165 + 60 * 3))
    game_window.blit(toggle_on_image, (283, 164 + 60 * 3))
    
    # Draw sliders
    font_slider = pygame.font.Font('Resources/Marcellus-Regular.ttf', 25)
    for y_idx in range(0, 3) :
        line_y = 447 + y_idx * 55
        slider_pos_x = 105 + 50 * y_idx + 30 # Example calculation for slider position
        pygame.draw.line(game_window, colors['lightGray'], (105, line_y), (105 + 155, line_y), 5)
        pygame.draw.line(game_window, colors['darkGray'], (105, line_y), (slider_pos_x, line_y), 5)
        pygame.draw.rect(game_window, colors['darkGray'], (slider_pos_x, line_y - 15, 12, 30))
        text_display = font_slider.render(str(y_idx * 50 + 30), True, colors['darkBrown'])
        game_window.blit(text_display, (286, line_y - 18))

# Function to draw all main GUI elements
def draw_all_gui_elements() :
    pad_width, pad_height = 312, 301
    gap_width, gap_height = 72, 25
    
    # Draw image display pads
    draw_window_pad((484, 57, pad_width, pad_height), display_pads[0]['color'], display_pads[0]['text'], display_pads[0]['icon'])
    draw_window_pad((484 + gap_width + pad_width, 57, pad_width, pad_height), display_pads[1]['color'], display_pads[1]['text'], display_pads[1]['icon'])
    draw_window_pad((484, 57 + gap_height + pad_height, pad_width, pad_height), display_pads[2]['color'], display_pads[2]['text'], display_pads[2]['icon'])
    draw_window_pad((484 + gap_width + pad_width, 57 + gap_height + pad_height, pad_width, pad_height), display_pads[3]['color'], display_pads[3]['text'], display_pads[3]['icon'])

    # Draw filter pad
    draw_filter_pad()
    
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

    # Blit background images
    game_window.blit(background_image, (0, 0))    
    # Design image is set to be fully transparent, so it won't be visible
    design_image.set_alpha(0) # Set alpha to 0 for full transparency
    game_window.blit(design_image, (0, 0))
    
    # Draw all GUI components
    draw_all_gui_elements()    
    
    # Update display
    pygame.display.update()
    # Control frame rate
    game_clock.tick(FPS)