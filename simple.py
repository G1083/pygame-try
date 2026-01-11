import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

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

while running:
    # red, green, blue: between 0 and 255
    screen.fill((255, 255, 255))

    # This is why it's diagonal: x is mod 400, y is mod 300.
    screen.blit(smiley, (int(x) % 400, int(y) % 300))
    # intiially: x = x + 1, i.e., 1 pixel per frame
    # now: 100 pixels per second

    # x = x + 100 * delta_time_in_seconds
    if w_down == True : 
        y = y - 50 * delta_time_in_seconds
 
 
    if s_down == True : 
        y = y + 50 * delta_time_in_seconds 
 
    if a_down == True : 
        x = x - 50 * delta_time_in_seconds

    if d_down == True : 
        x = x + 50 * delta_time_in_seconds

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
