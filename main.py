import sys
import pygame
import constantes
import metodos_del_juego as m

# Inicializar Pygame
pygame.init()

# Crear pantalla
screen = pygame.display.set_mode((constantes.SCREEN_WIDTH, constantes.SCREEN_HEIGHT))

# titulo del juego
pygame.display.set_caption("2048")

# Crear un tablero basandose en una matriz y obtiene estados del juego
board, game_over, game_won = m.reset_game()


running = True
moved = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                board, game_over, game_won = m.reset_game()
            if not game_over and not game_won:
                moved = False
                if event.key == pygame.K_DOWN:
                    moved = m.move_down(board)
                if event.key == pygame.K_UP:
                    moved = m.move_up(board)
                if event.key == pygame.K_RIGHT:
                    moved = m.move_right(board)
                if event.key == pygame.K_LEFT:
                    moved = m.move_left(board)

            if moved:
                m.generate_new_number(board)
                if m.check_win(board):
                    game_won = True
                elif m.check_loss(board):
                    game_over = True

    m.draw_screen(screen, board, game_won, game_over)
    pygame.display.flip()
