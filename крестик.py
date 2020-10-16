X = 'X'
O = 'O'
TIE = 'Ничья'
EMPTY = ' '
NUM_SQUARES = 9


def instructions():
    print (
'''Добро пожаловать в величайшую игру всех времён и народов
    на ринг выйдет человек и компьютер.
    Сможет ли этот человечек победить умнейшего компьютера ?
    правила:
    чтобы сделать ход введи число , соответствующее полю
                    0 | 1 | 2
                    ---------
                    3 | 4 | 5
                    ---------
                    6 | 7 | 8
    Игра начинается
    '''
    )
def ask_yes_no(question):
    response = None
    while response not in ('y', 'n'):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None 
    while response not in range(low, high):
        response = int(input(question))
    return response

def pieces():
    go_first = ask_yes_no('Пойдёшь первым? (y/n):')
    if go_first == 'y':
        print('Что же - да будет так')
        human = X
        comp = O
    else:
        print('Да Ты смельчак')
        comp = X
        human = O
    return comp, human

def new_board():
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board

def display_board(board):
    print('\t', board[0], '|', board[1], '|', board[2])
    print('\t', '------------')
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '------------')
    print('\t', board[6], '|', board[7], '|', board[8])

def legal_moves(board):
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 4, 8),
                   (2, 4, 6),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8))
    
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner

    if EMPTY not in board:
        return TIE

    return None

def human_move(board, human):
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number('куда же ты пойдешь, человек? ', 0, NUM_SQUARES)
        if move not in legal : 
            print ('Глупый человечек, это место уже занято')
    print ('ok')
    return move

def comp_move(board, comp, human):
    board = board[:]
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)
    print('Пожалуй, Я займу ячейку ', end= ' ')

    for move in legal_moves(board):
        board[move] = comp
        if winner(board) == comp:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] == human
        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, comp, human):
    if the_winner != TIE:
        print(the_winner, 'выиграл')
    else:
        print('ничья')

    if the_winner == comp:
        print('Глупый человечек, Я снова победил!')

    elif the_winner == human:
        print ('твой разум оказался умнее моего')

    elif the_winner == TIE:
        print ('Это была прекрасная игра, наши разумы умны')
def main():
    instructions()
    comp, human = pieces()
    turn = X
    board = new_board()
    display_board(board)
    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = comp_move(board, comp, human)
            board[move] = comp
        display_board(board)
        turn = next_turn(turn)
    the_winner = winner(board)
    congrat_winner(the_winner, comp, human)

main()
input('enter to exit')