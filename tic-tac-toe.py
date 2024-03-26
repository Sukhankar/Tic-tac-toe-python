def print_board(board):
    print("Current State of the Board: \n\n")
    for i in range(0, 9):
        if (i > 0) and (i % 3) == 0:
            print("\n")
        if board[i] == 0:
            print("_ ", end=" ")
        elif board[i] == -1:
            print("X ", end=" ")
        elif board[i] == 1:
            print("O ", end=" ")
    print("\n\n")


def user1_turn(board):
    pos = int(input("Enter X's position from [1,2,3,4,....9]: "))
    if board[pos - 1] != 0:
        print("Wrong Move")
        return False
    board[pos - 1] = -1
    return True


def user2_turn(board):
    pos = int(input("Enter O's position from [1,2,3,4,....9]: "))
    if board[pos - 1] != 0:
        print("Wrong Move")
        return False
    board[pos - 1] = 1
    return True


def minmax(board, player):
    x = analyze_board(board)
    if x != 0:
        return x * player
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = player
            score = -minmax(board, player * -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    if pos == -1:
        return 0
    return value


def com_turn(board):
    pos = -1
    value = -2
    for i in range(0, 9):
        if board[i] == 0:
            board[i] = 1
            score = -minmax(board, -1)
            board[i] = 0
            if score > value:
                value = score
                pos = i
    board[pos] = 1


def analyze_board(board):
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for i in range(0, 8):
        if (board[cb[i][0]] != 0 and
                board[cb[i][0]] == board[cb[i][1]] and
                board[cb[i][0]] == board[cb[i][2]]):
            return board[cb[i][0]]
    return 0


def main():
    choice = int(input("Enter 1 for Single player, 2 for Multiplayer: "))
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    if choice == 1:
        print("Computer: O vs You: X")
        player = int(input("Enter to play 1(st) or 2(nd): "))
        for i in range(0, 9):
            if analyze_board(board) != 0:
                break
            if (i + player) % 2 == 0:
                com_turn(board)
            else:
                print_board(board)
                while not user1_turn(board):
                    pass
    else:
        for i in range(0, 9):
            if analyze_board(board) != 0:
                break
            if i % 2 == 0:
                print_board(board)
                while not user1_turn(board):
                    pass
            else:
                print_board(board)
                while not user2_turn(board):
                    pass
    x = analyze_board(board)
    print_board(board)
    if x == 0:
        print("Draw!!!")
    elif x == -1:
        print("Player X wins!!!  O Loses!!!")
    elif x == 1:
        print("Player O wins!!!  X Loses!!!")


main()
