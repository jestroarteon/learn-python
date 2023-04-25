board = [["*","*","*"],
         ["*","*","*"],
         ["*","*","*"]]

def pretty_print(board):
    print("---------------------")
    for i in board:
        print('|', i[0], '|', ' ', '|',i[1], '|', ' ', '|', i[2], '|',)
        print("---------------------")
def take_input(player_token):
    row = int(input(f"Stroka, v kotoroy budet stoyat '{player_token}':"))
    column = int(input(f"Stolbets, v kotoroy budet stoyat '{player_token}':"))
    if row in range(1, 4) and column in range(1, 4):
        if board[row - 1][column - 1] == "*":
            board[row - 1][column - 1] = player_token
        else:
            print("NO!")
            take_input(player_token)
    else:
        print("WHAT?")
        take_input(player_token)

def check_win_in_rows(board, token):
    for row in board:
        check_row = True
        for element in row:
            if element != token:
                check_row = False
        if check_row:
            return True
    return False

def check_win_in_columns(board,token):
    for column in range(len(board)):
        check_column = True
        for row in range(len(board)):
            if board[row][column] != token:
                check_column = False
        if check_column:
            return True
    return False
        
def check_win_in_diagonal(board,token):
    main_diagonal = True
    for i in range(len(board)):
        if board[i][i] != token:
            main_diagonal = False
    if main_diagonal:
        return True
    side_diagonal = True
    for j in range(len(board)):
        if board[j][3 - j - 1] != token:
            side_diagonal = False
    if side_diagonal:
        return True
    return False

steps = 0
while True:
    if steps % 2 == 0:
        take_input("x")
    else:
        take_input("o")
    steps += 1
    pretty_print(board)
    if steps >= 4:
        if check_win_in_columns(board,'x')  or check_win_in_rows(board, "x") or check_win_in_diagonal(board, "x"):
            print("X wins")
            break
        if check_win_in_columns(board,'o')  or check_win_in_rows(board, "o") or check_win_in_diagonal(board, "o"):
            print("O wins")
            break
    if steps >= 9:
      print("you draw")
      break