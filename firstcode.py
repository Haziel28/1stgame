import pygame
from os.path import join
from random import randint


# general setup
pygame.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Thug shooter')
programIcon = pygame.image.load('possesed.png')
pygame.display.set_icon(programIcon)
running = True

# plain surface
surf = pygame.Surface((100,200))
surf.fill('purple')
x = 100
y = 100


# importing an image
player_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\player.png')).convert_alpha()
player_rect = player_surf.get_frect(center = (WINDOW_WIDTH / 2,WINDOW_HEIGHT / 2))
player_direction = -1
# rect = pygame.FRect(100,200,200,620)

star_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\star.png')).convert_alpha()
star_positions = [(randint(0,WINDOW_WIDTH),randint(0,WINDOW_HEIGHT))for i in range(20)]

meteor_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\meteor.png')).convert_alpha()
meteor_position = meteor_surf.get_frect(bottomright = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surf = pygame.image.load(join('C:\\Space shooter\\space 7 time\\code\\laser.png')).convert_alpha()
laser_position = laser_surf.get_frect(bottomleft = (20,WINDOW_HEIGHT-20))

# rect
# plain_rect = pygame.frect(pos, height)# If you want to make one from scratch

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    display_surface.fill('darkgrey')
    for pos in star_positions:
        display_surface.blit(star_surf, pos)

    display_surface.blit(meteor_surf,meteor_position)
    display_surface.blit(laser_surf,laser_position)
    # player movement
    player_rect.x += player_direction * 0.4
    if player_rect.right > WINDOW_WIDTH or player_rect.left < 0:
        player_direction *= -1
    display_surface.blit(player_surf, player_rect)

    pygame.display.update()

pygame.quit()

