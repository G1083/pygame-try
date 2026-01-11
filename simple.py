import pygame

pygame.init()

screen = pygame.display.set_mode((400, 300))

# smiley = pygame.image.load("emoji.png").convert()
smiley = pygame.image.load("smiley.png").convert_alpha()

running = True
x = 0.0
clock = pygame.time.Clock()

# time between frames in seconds: initialize to 60fps
delta_time_in_seconds = 1 / 60

while running:
    # red, green, blue: between 0 and 255
    screen.fill((255, 255, 255))

    screen.blit(smiley, (int(x) % 400, int(x) % 300))
    # intiially: x = x + 1, i.e., 1 pixel per frame
    # now: 100 pixels per second
    x = x + 100 * delta_time_in_seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

    delta_time_in_seconds = clock.tick(60) / 1000
    delta_time_in_seconds = max(0.001, min(delta_time_in_seconds, 0.1))

pygame.quit()
