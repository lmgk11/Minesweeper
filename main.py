import pygame
import game

CELL_SIZE, HEIGHT, WIDTH = 60, 10, 10

pygame.init()


screen = pygame.display.set_mode((CELL_SIZE * WIDTH, CELL_SIZE * HEIGHT), pygame.RESIZABLE)

clock = pygame.time.Clock()

pygame.display.set_caption("Physics")

font = pygame.font.Font('assets/fonts/mine-sweeper.ttf', CELL_SIZE - 15)

g = game.Game(WIDTH, HEIGHT)
#print(g.tiles)

def draw_board():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            # draw the grid
            pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            #check if it is revealed
            if g.tiles[row][col].revealed:
                pygame.draw.rect(screen, (128, 128, 128), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
            else: 
                pygame.draw.rect(screen, (192, 192, 192), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                number_surface = font.render(f'{g.tiles[row][col]}', True, (0, 0, 0))
                number_rect = number_surface.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(number_surface, number_rect)
            pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255, 255, 255))
    draw_board()
    pygame.display.flip()

