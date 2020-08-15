from blackboxgame import BlackBoxGame
import os

if __name__ == '__main__':
    ch = input("Start a game? (y/n) : ")
    if ch == 'y':
        print('\n')
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        game.print_board()
        row = col = 0
        while True:
            input_row = input("Enter a x-coordinate : ")
            if not input_row.isdigit():
                print("Invalid input. Try again!")
                continue
            else:
                row = int(input_row)
            input_col = input("Enter a y-coordinate : ")
            if not input_col.isdigit():
                print("Invalid input. Try again!")
                continue
            else:
                col = int(input_col)

            if 1 <= row <= 8 and 1 <= col <= 8:
                game.guess_atom(row, col)
            elif (row in [0, 9] and 1 <= col <= 8) or (col in [0, 9] and 1 <= row <= 8):
                game.shoot_ray(row, col)
            else:
                print("Invalid input. Try again!")
                continue

            game.print_board()
            print("Score :", game.get_score())
            print("Atoms Left :", game.atoms_left())
            print('\n')

            ch = input("Continue? (y/n) : ")
            if ch != 'y':
                break
    print("Goodbye!")