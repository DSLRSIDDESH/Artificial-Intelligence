# Here I am trying to maximise for computer which means trying to minimise for player
# Player plays with 'X' and computer plays with 'O'
board = {
    1: ' ', 2: ' ', 3: ' ',
    4: ' ', 5: ' ', 6: ' ',
    7: ' ', 8: ' ', 9: ' '
}
player = 'X'
computer = 'O'
inf = float('inf')

def print_board(board):
    print()
    print('   ',board[1] + '|' + board[2] + '|' + board[3])
    print('   -+-+-')
    print('   ',board[4] + '|' + board[5] + '|' + board[6])
    print('   -+-+-')
    print('   ',board[7] + '|' + board[8] + '|' + board[9])
    print()

def is_position_free(position):
    if board[position] == ' ':
        return True
    return False

def new_move(move, position):
    if is_position_free(position):
        board[position] = move
        print_board(board)
        if Draw():
            if not Wins():
                print("It's Draw!")
                exit()
        if Wins():
            if move == 'O':
                print("Computer Wins!")
                exit()
            if move == 'X':
                print("Player Wins!")
                exit()
        return
    else:
        print('Invalid position!')
        position = int(input("Enter the new position : "))
        new_move(move, position)

def Draw():
    for i in board.keys():
        if board[i] == ' ':
            return False
    return True

def Wins():
    if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] != ' ':
        return True
    else:
        return False
    
def check_who_won(symbol):
    if board[1] == board[2] and board[1] == board[3] and board[1] == symbol:
        return True
    elif board[4] == board[5] and board[4] == board[6] and board[4] == symbol:
        return True
    elif board[7] == board[8] and board[7] == board[9] and board[7] == symbol:
        return True
    elif board[1] == board[4] and board[1] == board[7] and board[1] == symbol:
        return True
    elif board[2] == board[5] and board[2] == board[8] and board[2] == symbol:
        return True
    elif board[3] == board[6] and board[3] == board[9] and board[3] == symbol:
        return True
    elif board[1] == board[5] and board[1] == board[9] and board[1] == symbol:
        return True
    elif board[3] == board[5] and board[3] == board[7] and board[3] == symbol:
        return True
    else:
        return False

def player_move():
    position = int(input("Enter the position for 'X' : "))
    new_move(player, position)
    return

def computer_move():
    print('Computers Move : ',end = '')
    best_score = -inf
    best_move = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer
            score = minimax(board, -inf, inf, True)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    print("'O' at position",best_move)
    new_move(computer, best_move)
    return

def minimax(board,alpha,beta,isMaximising):
    if check_who_won(computer):
        return 1        # returning score as 1 if computer wins
    elif check_who_won(player):
        return -1       # returning score as -1 if player wins
    elif Draw():
        return 0        # returning score as 0 if draw
    
    if isMaximising:
        best_score = -inf
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, alpha, beta, False)
                board[key] = ' '
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if alpha >= beta:
                    break
        return best_score
    else:
        best_score = inf
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer
                score = minimax(board, alpha, beta, True)
                board[key] = ' '
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
        return best_score

if __name__ == '__main__':
    while (not Draw()) or (not Wins()):
        player_move()
        computer_move()