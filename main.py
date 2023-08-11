import pygame
import game

pygame.init()
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

screen = pygame.display.set_mode((600, 400))

clock = pygame.time.Clock()

pygame.display.set_caption("Physics")

g = game.Game(10, 10)
#print(g.tiles)

while True:
    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill(green)

    pygame.display.flip()