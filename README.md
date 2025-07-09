# Pygame & OpenCV: Learning Journey for Computer Vision and Hand Tracking Games

This repository showcases my journey in developing **motion-controlled applications/games** using Python's popular game library Pygame and the powerful computer vision library OpenCV. The project demonstrates a step-by-step progression from basic Pygame concepts to camera integration, hand detection, and finally, a full-fledged balloon pop game.

My goal was to grasp the fundamental principles in this field through practical application and integrate computer vision capabilities into game development.

---

## Project Structure and Learning Stages

This repository contains a series of small exercise files and the final game code. Each file aims to explore a specific concept or functionality related to Pygame or OpenCV:

### 1. Pygame Fundamentals and Visual Elements

Files in this section demonstrate the basic setup of Pygame and how to manage visual elements.

* `PygameTemplate.py`:
    * **Purpose:** Shows initial setup for creating a basic window, setting up the game loop, and controlling FPS (Frames Per Second) in Pygame.
* `AddText.py`:
    * **Purpose:** Demonstrates practical methods for adding and displaying text (using both custom and default fonts) in a Pygame window.
* `DrawHapes.py`:
    * **Purpose:** Develops skills in drawing and coloring basic geometric shapes (polygons, circles, lines, rectangles) using Pygame.
* `AddImage.py`:
    * **Purpose:** Explains the fundamentals of loading external image files (PNG, JPG, etc.) into Pygame and blitting them onto the window.
* `AddRect.py`:
    * **Purpose:** Clarifies the use of `pygame.Rect` objects, their movement, and the principle of collision detection (`colliderect`) between two rectangles. This is a critical step for game mechanics.
* `ImageTransformations.py`:
    * **Purpose:** Shows how to perform transformations (rotation, scaling, flipping) on loaded images within Pygame.

### 2. OpenCV Integration and GUI Design

These files cover camera integration and drawing more complex interfaces.

* `OpenCVIntegration.py`:
    * **Purpose:** Provides a basic integration example demonstrating how to capture a live video feed from the computer's camera (using OpenCV) and display it within a Pygame window.
* `A. Project - GUI.py`:
    * **Purpose:** This is a separate Pygame project exploring general user interface (GUI) design and manually drawing custom UI components (like panels, toggle-like elements, and sliders) in Pygame. It focuses on color palette usage and layout.

### 3. Main Game Project

* `BalloonPop.py` - **Main Game Code**
    * **Purpose:** This file is the culminating project that brings together all the learned concepts. It integrates live camera feed, advanced hand tracking with the `cvzone` library, and balloon popping game mechanics to offer an interactive experience.

---

## Key Features of `BalloonPop.py` Game

* **Live Camera Integration:** Real-time webcam footage is streamed into the game interface.
* **Hand Detection & Tracking:** Utilizes the `cvzone` library to detect and track the player's hand and the tip of their index finger.
* **Interactive Gameplay:** Balloons are popped upon contact with the player's index finger.
* **Dynamic Game Experience:** The game speed increases with every popped balloon, raising the difficulty.
* **Score and Time Tracking:** Features a basic user interface displaying the player's current score and remaining game time.
* **Easy Exit:** Players can terminate the game at any time by pressing the 'Q' key.

---

## How to Run

To run the projects on your computer, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/Pygame-OpenCV-HandTracking-Games.git](https://github.com/YOUR_USERNAME/Pygame-OpenCV-HandTracking-Games.git)
    ```
    (Please replace `YOUR_USERNAME` with your actual GitHub username.)

2.  **Navigate to the project folder:**
    ```bash
    cd Pygame-OpenCV-HandTracking-Games
    ```

3.  **Install Necessary Libraries:**
    ```bash
    pip install pygame opencv-python cvzone numpy
    ```

4.  **Run a Game or Example Code:**
    For example, to run the main Balloon Pop game:
    ```bash
    python BalloonPop.py
    ```
    To run other examples, use the respective file name:
    ```bash
    python PygameTemplate.py
    python AddText.py
    # ... and so on
    ```

---

## Feedback

This repository serves as my personal learning and practice space. Feel free to open an issue for any feedback, suggestions, or ideas!
