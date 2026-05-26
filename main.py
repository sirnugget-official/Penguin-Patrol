# setting canvas
import pygame
import sys
# https://www.pygame.org/docs/
pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Penguin Patrol")

# colours :)
blue = (30, 144, 255)
yellow = (238, 214, 175)
grey = (80, 80, 80)
green = (46, 139, 87)

clock = pygame.time.Clock()
running_fps = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #ocean
    pygame.draw.rect(screen, blue, (0, 450, width, 150))
    #beach
    pygame.draw.rect(screen, yellow, (0, 250, width, 200))
    #road
    pygame.draw.rect(screen, grey, (0, 150, width, 100))
    #dune/penguin burrow things
    pygame.draw.rect(screen, green, (0, 0, width, 150))

    pygame.display.flip()
    clock.tick(running_fps)

pygame.quit()
sys.exit()