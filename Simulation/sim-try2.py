import pandas as pd 
import math 
import pygame
import numpy as np
import random
import cv2


data = {
    "sun": {
        "col": (255, 255, 0),
        "rad": 50,
        "grav": 30,
        "pos": [800, 450],
        "vel": [0, 0],
        "type": 2
    },
    "earth": {
        "col": (100, 100, 255),
        "rad": 5,
        "grav": 1,
        "pos": [1100, 450],
        "vel": [0, -8],
        "type": 0
    },
    "venus": {
        "col": (255, 50, 50),
        "rad": 5,
        "grav": 0.9,
        "pos": [1000, 450],
        "vel": [0, -6],
        "type": 0
    },
    "mars": {
        "col": (255, 0, 0),
        "rad": 3,
        "grav": 0.4,
        "pos": [1200, 450],
        "vel": [0, -10],
        "type": 0
    },
    "jupiter": {
        "col": (255, 150, 150),
        "rad": 12,
        "grav": 2.4,
        "pos": [300, 450],
        "vel": [0, 12],
        "type": 1
    },
  
  
}
# Constants
AVG_VEL = 7.616  # arcsec/s
RA_VEL = -1e-06  # hour/s
DEC_VEL = -3.12e-05  # degrees/s
ROL_VEL = -4.96e-05  # degrees/s

# Initial position and velocities
initial_RA = 15 * 3600 + 51 * 60 + 16.2  # in seconds
initial_DEC = -20 * 3600 - 9 * 60 - 10.4  # in seconds
initial_ROL = 0  # Assuming initial roll velocity is 0

# Pygame initialization
pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

# Debris class
class Debris:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ra = initial_RA
        self.dec = initial_DEC
        self.rol = initial_ROL
        self.vel_ra = RA_VEL + random.uniform(-0.5, 0.5) * AVG_VEL
        self.vel_dec = DEC_VEL + random.uniform(-0.5, 0.5) * AVG_VEL
        self.vel_rol = ROL_VEL + random.uniform(-0.5, 0.5) * AVG_VEL

    def update(self):
        self.ra += self.vel_ra
        self.dec += self.vel_dec
        self.rol += self.vel_rol
        self.x = int(self.ra * screen_width / (3600 * 24))  # Convert RA to pixels
        self.y = int(self.dec * screen_height / 360)  # Convert DEC to pixels

    def draw(self):
        pygame.draw.circle(screen, (255, 255, 255), (self.x, self.y), 2)



def extract_debris_count(image_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Unable to load image.")
        return -1

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to obtain binary image
    _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Count the number of contours (debris)
    num_debris = len(contours)
    
    return num_debris

def draw_planets():
#     for planet in data:
         pygame.draw.circle(display, data[planet]['col'], data[planet]['pos'], data[planet]['rad'])



# Function to extract initial positions from image (not implemented)

# Main function
def main():
    debris_list = []  # List to store debris objects
    # Example usage
    image_path = r"C:\Users\USER\Desktop\TechnicalGP\images_Preprocessing\iter_images\NEOS_SCI_2024001000312.png"  
    num_debris = extract_debris_count(image_path)
    

    # Code to extract number of debris and initial positions from image

    # Creating debris objects with random initial velocities
    for i in range(num_debris):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        debris_list.append(Debris(x, y))

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update and draw debris
        for debris in debris_list:
            debris.update()
            debris.draw()

        pygame.display.flip()
        clock.tick(30)  # Limit to 30 frames per second

    pygame.quit()

if __name__ == "__main__":
    main()
