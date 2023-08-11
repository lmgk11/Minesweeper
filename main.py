import pygame
import game
import easygui

CELL_SIZE, HEIGHT, WIDTH = 60, 15, 20

pygame.init()


screen = pygame.display.set_mode((CELL_SIZE * WIDTH, CELL_SIZE * HEIGHT), pygame.RESIZABLE)

clock = pygame.time.Clock()

pygame.display.set_caption("Physics")

font = pygame.font.Font('assets/fonts/mine-sweeper.ttf', CELL_SIZE - 20)

g = game.Game(WIDTH, HEIGHT)

flag_image = pygame.transform.scale(pygame.image.load('assets/images/flag.png'), (round(CELL_SIZE*0.6), round(CELL_SIZE*0.6)))
running = True
first_game = True

def draw_board():
    for row in range(HEIGHT):
        for col in range(WIDTH):
            # draw the grid
            pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
            #check if it is revealed
            if not g.tiles[row][col].revealed:
                if g.tiles[row][col].flagged:
                    pygame.draw.rect(screen, (128, 128, 128), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    number_surface = font.render(chr(0x0060), True, (92, 0, 0))
                    number_rect = number_surface.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                    screen.blit(number_surface, number_rect)
                    
                    pygame.draw.rect(screen, (60, 60, 60), (col * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2), 2)
                    pygame.draw.rect(screen, (100, 100, 100), (col * CELL_SIZE + 3, row * CELL_SIZE + 3, CELL_SIZE - 6, CELL_SIZE - 6), 3)
                    
                else:
                    pygame.draw.rect(screen, (128, 128, 128), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                    pygame.draw.rect(screen, (60, 60, 60), (col * CELL_SIZE + 1, row * CELL_SIZE + 1, CELL_SIZE - 2, CELL_SIZE - 2), 2)
                    pygame.draw.rect(screen, (100, 100, 100), (col * CELL_SIZE + 3, row * CELL_SIZE + 3, CELL_SIZE - 6, CELL_SIZE - 6), 3)

            elif g.tiles[row][col].number != 0: 
                pygame.draw.rect(screen, (192, 192, 192), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                number_surface = font.render(f'{g.tiles[row][col]}', True, (0, 0, 0))
                number_rect = number_surface.get_rect(center=(col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2))
                screen.blit(number_surface, number_rect)
                pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
            else:
                pygame.draw.rect(screen, (192, 192, 192), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2)
            pygame.draw.rect(screen, (0, 0, 0), (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)

def display_msg(msg):
    
    msg_text = font.render(msg, True, (0, 0, 0))
    msg_rect = msg_text.get_rect(center=(CELL_SIZE * (WIDTH) // 2, CELL_SIZE * (HEIGHT) // 2))
    screen.blit(msg_text, msg_rect)

    continue_button_text = font.render('Continue', True, (0, 92, 0))
    continue_button = continue_button_text.get_rect(center=(CELL_SIZE * (WIDTH) // 2, CELL_SIZE * (HEIGHT + 2) // 2))
    screen.blit(continue_button_text, continue_button)

    quit_button_text = font.render('Quit', True, (92, 0, 0))
    quit_button = quit_button_text.get_rect(center=(CELL_SIZE * (WIDTH) // 2, CELL_SIZE * (HEIGHT + 4) // 2))
    screen.blit(quit_button_text, quit_button)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if continue_button.collidepoint(event.pos[0], event.pos[1]):
                return False
            if quit_button.collidepoint(event.pos[0], event.pos[1]):
                pygame.quit()
                exit()
            
    return True



while running:
    screen.fill((255, 255, 255))
    
    if first_game:
        first_game = display_msg('welcome')
    else:
        status = g.game_status()
        if not status[0]:
            replay = not display_msg('You Win!' if status[1] else 'Game Over!')
            if replay:
                g = game.Game(WIDTH, HEIGHT)
                status[0] = True
        else:
            draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                left_click, middle_click, right_click = pygame.mouse.get_pressed()
                if left_click:
                    g.reveal(event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE)
                elif right_click:
                    g.flag(event.pos[1] // CELL_SIZE, event.pos[0] // CELL_SIZE)
    
        
            

    
    
    pygame.display.flip()

