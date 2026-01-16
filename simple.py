"""
How to run this:

VS Code
->
Open this directory by dragging it from Windows into VS Code
->
Control ` (to open shell)
->
cd Downloads/ally-pygame/ally-pygame
->
python simple.py
"""

import pygame

pygame.init()

screen_with = 1080
screen_height = 640
screen = pygame.display.set_mode((screen_with, screen_height))
# smiley = pygame.image.load("emoji.png").convert()
smiley = pygame.image.load("smiley.png").convert_alpha()

running = True
x = 0.0
y = 0.0
clock = pygame.time.Clock()

# time between frames in seconds: initialize to 60fps
delta_time_in_seconds = 1 / 60

# to track keyboard events
w_down = False
a_down = False
s_down = False
d_down = False 

collided_already = False
num_collided = 0
    
while running:
    # red, green, blue: between 0 and 255
    screen.fill((255, 0, 255))

    smiley_x = int(x) % (screen_with - 110 )
    smiley_y = int(y) % (screen_height - 110)

    # This is why it's diagonal: x is mod 400, y is mod 300.
    screen.blit(smiley, (smiley_x, smiley_y))
    # intiially: x = x + 1, i.e., 1 pixel per frame

    hitbox = pygame.Rect(smiley_x, smiley_y, smiley.get_width(), smiley.get_height())
    target = pygame.Rect(600, 200, 50, 50)
    collision = hitbox.colliderect(target)

    if collision:
        if not collided_already :
            num_collided = num_collided + 1
        collided_already = True
    else: collided_already = False 


    if num_collided == 1:
        # draw yellow
        pygame.draw.rect(screen, ( 255, 200, 25), target)
    elif num_collided == 2:
        # draw red
        pygame.draw.rect(screen, ( 255, 25, 25), target)
    elif num_collided == 3:
        pygame.quit()
    else: 
        # draw green
        pygame.draw.rect(screen, ( 50, 255, 25), target)

    # x = x + 100 * delta_time_in_seconds
    if w_down == True : 
        y = y - 500 * delta_time_in_seconds
 
 
    if s_down == True : 
        y = y + 500 * delta_time_in_seconds 
 
    if a_down == True : 
        x = x - 500 * delta_time_in_seconds

    if d_down == True : 
        x = x + 500 * delta_time_in_seconds

    for event in pygame.event.get():
        # print('Got an event:', event)
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # print('Key down:', event)
            if event.unicode == 'w':
                w_down = True

            if event.unicode == 's':
                s_down = True


            if event.unicode == 'a':
                a_down = True

            if event.unicode == 'd':
                d_down = True


        elif event.type == pygame.KEYUP:
            # print('Key up:', event)
            if event.unicode == 'w':
                w_down = False

            if event.unicode == 's':
                s_down = False

            if event.unicode == 'a':
                a_down = False

            if event.unicode == 'd':
                d_down = False

    pygame.display.flip()

    delta_time_in_seconds = clock.tick(60) / 1000
    delta_time_in_seconds = max(0.001, min(delta_time_in_seconds, 0.1))

pygame.quit()
