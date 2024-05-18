import random
import pygame.font
import constantes


def draw_screen(screen, board, game_won=False, game_over=False):
    screen.fill(constantes.WHITE)
    font = pygame.font.Font(None, 40)

    for i in range(4):
        for j in range(4):
            value = board[i][j]
            color = constantes.COLORS.get(value, constantes.COLORS[0])
            pygame.draw.rect(screen, color,
                             (j * constantes.CELL_SIZE,
                              i * constantes.CELL_SIZE,
                              constantes.CELL_SIZE,
                              constantes.CELL_SIZE), width=0)
            if value != 0:
                text = font.render(str(value), True, constantes.BLACK)
                text_rect = text.get_rect(center=(j * constantes.CELL_SIZE + constantes.CELL_SIZE // 2,
                                                  i * constantes.CELL_SIZE + constantes.CELL_SIZE // 2))
                screen.blit(text, text_rect)

    message = "{}!! Presiona 'R' para reiniciar"
    message_font = pygame.font.Font(None, 30)
    if game_won:
        text_result = message_font.render(message.format(constantes.WIN), True, constantes.GREEN)
        screen.blit(text_result, (20, constantes.SCREEN_HEIGHT // 2 - 20))

    if game_over:
        text_result = message_font.render(message.format(constantes.DEFEAT), True, constantes.RED)
        screen.blit(text_result, (20, constantes.SCREEN_HEIGHT // 2 - 20))


def generate_new_number(board):
    empty = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if empty:
        i, j = (random.choice(empty))
        board[i][j] = random.choice([2, 4])


def compress(nums):
    new_nums = [num for num in nums if num != 0]
    nums[:] = new_nums + [0] * (4 - len(new_nums))


def merge(nums):
    for i in range(3):
        if nums[i] == nums[i + 1] and nums[i] != 0:
            nums[i] *= 2
            nums[i + 1] = 0


def move_left(board):
    moved = False
    for i in range(4):
        original = board[i][:]
        compress(board[i])
        merge(board[i])
        compress(board[i])
        if original != board[i]:
            moved = True
    return moved


def move_right(board):
    moved = False
    for i in range(4):
        original = board[i][:]
        board[i].reverse()
        compress(board[i])
        merge(board[i])
        compress(board[i])
        board[i].reverse()
        if original != board[i]:
            moved = True
    return moved


def move_up(board):
    moved = False
    for j in range(4):
        column = [board[i][j] for i in range(4)]
        original = column[:]
        compress(column)
        merge(column)
        compress(column)
        for i in range(4):
            board[i][j] = column[i]
        if original != column:
            moved = True
    return moved


def move_down(board):
    moved = False
    for j in range(4):
        column = [board[i][j] for i in range(4)]
        original = column[:]
        column.reverse()
        compress(column)
        merge(column)
        compress(column)
        column.reverse()
        for i in range(4):
            board[i][j] = column[i]
        if original != column:
            moved = True
    return moved


def check_win(board):
    return any(2048 in row for row in board)


def check_loss(board):
    if any(0 in row for row in board):
        return False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j + 1] or board[j][i] == board[j + 1][i]:
                return False
    return True


def reset_game():
    board = [[0] * 4 for _ in range(4)]
    game_won = False
    game_over = False
    generate_new_number(board)
    generate_new_number(board)
    return board, game_over, game_won
