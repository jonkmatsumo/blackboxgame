from blackboxgame import BlackBoxGame


def get_next_move():
    while True:
        input_row = input("Enter a x-coordinate : ")
        if not input_row.isdigit():
            print("Invalid input. Try again!")
            continue
        row = int(input_row)
        input_col = input("Enter a y-coordinate : ")
        if not input_col.isdigit():
            print("Invalid input. Try again!")
            continue
        col = int(input_col)
        return row, col


def move():
    row, col = get_next_move()
    if 1 <= row <= 8 and 1 <= col <= 8:
        if game.guess_atom(row, col):
            print("Atom found at ({},{})!".format(row, col))
        else:
            print("No Atom found at ({},{})".format(row, col))
    elif (row in [0, 9] and 1 <= col <= 8) or (col in [0, 9] and 1 <= row <= 8):
        ray = game.shoot_ray(row, col)
        if ray is None:
            print("Hit!")
        elif ray is False:
            print("Invalid starting position. Try again!")
        else:
            print("Ray entered at ({},{}) and exited at ({},{})!".format(row, col, ray[0], ray[1]))
    else:
        print("Invalid input. Try again!")
        move()


if __name__ == '__main__':
    ch = input("Start a game? (y/n) : ")

    if ch == 'y':
        print('\n')
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        game.print_board()

        score = game.get_score()
        atoms_left = game.atoms_left()

        while True:
            # print board and score
            game.print_board()
            print("Score :", score)
            print("Atoms Left :", atoms_left)

            move()

            # update score and atoms left
            score = game.get_score()
            atoms_left = game.atoms_left()

            # check if game is over
            if not score > 0 or atoms_left > 0:
                break

            # see if user wants to terminate game early
            ch = input("Continue? (y/n) : ")
            if ch != 'y':
                break

    print("Goodbye!")