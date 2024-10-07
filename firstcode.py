import pygame
from os.path import join
from random import randint

import pygame.sprite  # Importing necessary modules for pygame and sprite handling


class Player(pygame.sprite.Sprite):  # Defining the Player class, inheriting from pygame's Sprite
    def __init__(self, groups):
        super().__init__(groups)  # Calling the parent class (Sprite) initializer
        # Loading the player image and setting its rectangular boundaries
        self.image = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\player.png')).convert_alpha()
        self.rect = self.image.get_frect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))  # Centering the player on screen
        self.direction = pygame.Vector2()  # Vector to store the player's movement direction
        self.speed = 300  # Setting the player's movement speed
    
    def update(self, dt):
        keys = pygame.key.get_pressed()  # Checking for keyboard inputs
        # Adjusting the direction vector based on arrow key inputs
        self.direction.x = int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT])
        self.direction.y = int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP])
        # Normalizing direction vector to ensure consistent speed in all directions
        self.direction = self.direction.normalize() if self.direction else self.direction
        # Updating the player's position based on direction, speed, and delta time
        self.rect.center += self.direction * self.speed * dt

        # Checking if the space bar was just pressed to "fire"
        recent_keys = pygame.key.get_just_pressed()
        if recent_keys[pygame.K_SPACE]:
            print('FIRE THEM HOES')  # Placeholder action for firing

class Star(pygame.sprite.Sprite):  # Defining the Star class, also inheriting from Sprite
    def __init__(self, groups, surf):
        super().__init__(groups)  # Calling parent class initializer
        # Setting star image and its position randomly within the screen bounds
        self.image = surf
        self.rect = self.image.get_frect(center=(randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)))

# General setup for the game
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720  # Setting up the window size
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))  # Creating the display surface
pygame.display.set_caption('Thug shooter')  # Setting the window title
programIcon = pygame.image.load('possesed.png')  # Loading an icon for the game window
pygame.display.set_icon(programIcon)  # Setting the window icon
running = True  # Control variable for the game loop
clock = pygame.time.Clock()  # Clock object to manage time in the game

# Creating a surface object and filling it with purple color
surf = pygame.Surface((100, 200))
surf.fill('purple')
x = 100  # X position for something that’s not yet used

# Creating a group to manage all sprite objects
all_sprites = pygame.sprite.Group()
star_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\star.png')).convert_alpha()  # Loading star image
# Creating 20 Star objects and adding them to the sprite group
for i in range(20):
    Star(all_sprites, star_surf)
player = Player(all_sprites)  # Creating a Player object and adding it to the sprite group

# Loading other game assets (commented out for now)
#star_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\star.png')).convert_alpha()
# star_rect = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT))for i in range(20)]

meteor_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\meteor.png')).convert_alpha()  # Loading meteor image
meteor_position = meteor_surf.get_frect(bottomright=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))  # Setting meteor position

laser_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\laser.png')).convert_alpha()  # Loading laser image
laser_rect = laser_surf.get_frect(bottomleft=(20, WINDOW_HEIGHT-20))  # Setting laser position

# rect (commented out for now)
# plain_rect = pygame.frect(pos, height) # If you want to make one from scratch

# Game loop to keep the game running
while running:
    dt = clock.tick() / 1000  # Getting delta time (time between frames)
    
    # Handling events (like closing the game window)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # If the quit event occurs, stop the game loop

    all_sprites.update(dt)  # Updating all sprites based on delta time
    
    # Drawing the game
    display_surface.fill('darkgrey')  # Filling the screen with a background color
#    for pos in star_rect:
#        display_surface.blit(star_surf, pos)  # Drawing stars (commented out for now)

    # Drawing all sprite objects on the display surface
    all_sprites.draw(display_surface)

    pygame.display.update()  # Updating the display

pygame.quit()  # Exiting the game when the loop finishes


