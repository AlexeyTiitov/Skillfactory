board =[
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def show_board():
    print("  1 2 3")
    for i in range(len(board)):
        print(i + 1, end=" ")
        for j in board[i]:
            print(j, end=" ")
        print()

def win(player):
    for i in board:
        if i.count(player) == 3:
            return True
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
        if board[0][0] == player and  board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        else:
            return False
def is_draw():
    is_draw = True
    for i in board:
        for j in i:
            if j == "-":
                is_draw = False
    return is_draw
def IsInputCorrect(x1, x2):
    if 0 <= x1 < 3 and 0 <= x2 < 3:
        return True
    else:
        print("Введите число от 1 до 3")
        return False

def check_game_over(x):
    player_win = win(x)
    if player_win:
        print(f"Игрок {x} победил")
    return is_draw() or player_win

def play():
    show_board()
    is_x = True
    is_game_over = False
    x = 0
    while not is_game_over:
        i = int(input("Номер строки ")) - 1
        j = int(input("номер столбца ")) - 1
        if IsInputCorrect(i, j):
            if board[i][j] != "-":
                print("занято")
            else:
                board[i][j] = "X" if is_x else "O"
                is_game_over = check_game_over("X" if is_x else "O")
                is_x = not is_x
                show_board()

play()