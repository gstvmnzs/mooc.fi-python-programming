# Write your solution here

def play_turn(game_board: list, x: int, y: int, piece: str):
    if x < 3 and x >= 0 and y < 3 and y >= 0 and game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False

