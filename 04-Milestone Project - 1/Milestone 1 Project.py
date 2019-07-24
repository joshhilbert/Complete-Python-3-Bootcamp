
import sys


# Print board
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
            # print(marker)
        else:
            # print(x)
            new_board.append(x)

    return new_board


def win_check(board):
    # horizontal wins
    if board[6] == board[7] == board[8] and board[7] != ' ':
        return True
    elif board[3] == board[4] == board[5] and board[4] != ' ':
        return True
    elif board[0] == board[1] == board[2] and board[2] != ' ':
        return True

    # vertical wins
    elif board[6] == board[3] == board[0] and board[3] != ' ':
        return True
    elif board[7] == board[4] == board[1] and board[4] != ' ':
        return True
    elif board[8] == board[5] == board[2] and board[5] != ' ':
        return True

    # diag wins
    elif board[6] == board[4] == board[2] and board[4] != ' ':
        return True
    elif board[0] == board[4] == board[8] and board[4] != ' ':
        return True
    else:
        return False


def space_check(board):  # COMPLETE
    # default variable to enter for user input
    free = 'dummy'
    position = False

    while position != free:
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
    space = ' '
    if [x for x in board if space in x]:
        return False
    else:
        return True


def replay():  # COMPLETE
    value = input("Play again? (Y\\N)")

    if value.lower() == 'y':
        return True
    else:
        print("Thanks for playing!")
        return False


# Game program
def main():
    while True:
        print("\n" * 50)

        # Use to show players cell selections
        print('Welcome to Tic Tac Toe!\nBelow is the board with the corresponding keypad markers.\n')

        sample_board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        display_board(sample_board)

        # Set game up here
        board = [' ' for x in sample_board]
        game_on = True

        while game_on:
            # Player 1 Turn
            print("Player 1's turn! (X)")
            # add full board check
            spot = space_check(board)
            board = place_marker(board, 'X', spot)
            winner = win_check(board)
            draw = full_board_check(board)
            display_board(board)
            if winner:
                print("X wins!")
                if replay():
                    main()
                else:
                    sys.exit()
            elif draw:
                print("Board full! Draw!")
                replay()
                if replay():
                    main()
                else:
                    sys.exit()

            # Player 2 Turn
            print("Player 2's turn! (O)")
            # add full board check
            spot = space_check(board)
            board = place_marker(board, 'O', spot)
            winner = win_check(board)
            draw = full_board_check(board)
            display_board(board)
            if winner:
                print("O wins!")
                replay()
                if not replay():
                    sys.exit()
            elif draw:
                print("Board full! Draw!")
                replay()
                if not replay():
                    sys.exit()


# Start game
main()