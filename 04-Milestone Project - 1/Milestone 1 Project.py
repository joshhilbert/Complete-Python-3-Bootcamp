
import sys


def display_board(board):
    print(board[6] + '|' + board[7] + '|' + board[8])
    print('------')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('------')
    print(board[0] + '|' + board[1] + '|' + board[2])


def place_marker(board, marker, position):
    new_board = []

    for num, x in enumerate(board):
        if num == position:
            new_board.append(marker)
        else:
            new_board.append(x)

    return new_board


def win_check(board):
    return ((board[6] == board[7] == board[8] and board[7] != ' ') or
            (board[3] == board[4] == board[5] and board[4] != ' ') or
            (board[0] == board[1] == board[2] and board[2] != ' ') or
            (board[6] == board[3] == board[0] and board[3] != ' ') or
            (board[7] == board[4] == board[1] and board[4] != ' ') or
            (board[8] == board[5] == board[2] and board[5] != ' ') or
            (board[6] == board[4] == board[2] and board[4] != ' ') or
            (board[0] == board[4] == board[8] and board[4] != ' '))


def space_check(board):
    free = 'dummy'
    position = False

    while not (position == free):
        position = input("Pick cell: ")
        try:
            i = int(position) - 1
            if i > len(board):
                print("Pick a number 9 or lower!")
                continue
            elif i < 0:
                print("Pick a number 1 or higher!")
                continue
            elif board[i] == ' ':
                return i
            else:
                print("That cell is taken..")
        except ValueError:
            print('Not a number! Try again..')
            position = False

    return position


def full_board_check(board):
    if [x for x in board if ' ' in x]:
        return False
    else:
        return True


def replay():
    value = input("Play again? (Y\\N)")

    if value.lower() == 'y':
        main()
    else:
        print("Thanks for playing!")
        sys.exit()


def main():
    # Game set up
    print("\n" * 50)
    print('Welcome to Tic Tac Toe!\nBelow is the board with the corresponding keypad markers.\n')
    sample_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    display_board(sample_board)

    board = [' '] * 9

    while True:
        # Player 1 Turn
        print("Player 1's turn! (X)")
        spot = space_check(board)
        board = place_marker(board, 'X', spot)

        winner = win_check(board)
        draw = full_board_check(board)

        display_board(board)
        if winner:
            print("\nX wins!")
            replay()
        elif draw:
            print("\nBoard full! Draw!")
            replay()

        # Player 2 Turn
        print("Player 2's turn! (O)")
        spot = space_check(board)
        board = place_marker(board, 'O', spot)

        winner = win_check(board)
        draw = full_board_check(board)

        display_board(board)
        if winner:
            print("\nO wins!")
            replay()
        elif draw:
            print("\nBoard full! Draw!")
            replay()


# Start game
main()
