import pygame
from os.path import join # importing necessary modules
from random import randint


# general setup
pygame.init() # We need to initialize the game
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720 # We make the game windows height and width by making them variables with values
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # we turn on display surface and call it display surface and give it width and height
pygame.display.set_caption('Thug shooter') # Here we give our display window a name
programIcon = pygame.image.load('possesed.png') # Here we give it an icon by using an image already in our files
pygame.display.set_icon(programIcon)  # This is how the image prints needs the 2
running = True # We make it true as long as the game is running and you haven't exited out

# plain surface
surf = pygame.Surface((100,200)) # Here we make our other surface and give it a range of how big it is
surf.fill('purple') # we can make it purple
x = 100 # This is its starting points
y = 100
# This is if you want to make a image in the python probably not the best option.

# importing an image
player_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\player.png')).convert_alpha() #  Here we import the image using pycharm method and convert alpha is so the frames run smoothly
star_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\star.png')).convert_alpha() # This is for the other image of the stars we join them to make it run smoother and neat code
star_positions = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT))for i in range(20)] # In star positions we want them to be random so we use randint to put them in random places
# then for everything in range of 0/20 runs
while running: # While running is true it runs everything down here
    # event loop
    for event in pygame.event.get(): # For anything that happens in the game it will run code below necessary
        if event.type == pygame.QUIT: # This is so it lets you quit and not crash the game
            running = False # End the game
    # draw the game make it look nice
    display_surface.fill('darkgrey') # We make the displays surface darkgrey by using fill if you remove this piece of code it will drag on 
    x += 0.1 # This is how fast it moves by x and y coordinates 
    y += 0.1 # Were also just defining them for use below
    display_surface.blit(player_surf, (x,y)) # The player image will (Block,Image,transport) from one surface on to another
    for pos in star_positions: # For the position in the variable star positions
        display_surface.blit(star_surf, pos) # We display the star position variables in the display surface
    pygame.display.update() # This is just so it updates after little things happen not crash the game
    # Make sure everything is in order you want like display surface should go first not last as it will cover everything else up
pygame.quit() # We need this and put everything between this and init()
