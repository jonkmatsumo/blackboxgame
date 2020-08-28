from blackboxgame import BlackBoxGame
from random import randint


def get_atoms():
    while True:
        num_atoms = input("Enter the number of Atoms : ")
        if not num_atoms.isdigit():
            print("Invalid input. Try again!")
            continue

        num_atoms = int(num_atoms)
        if num_atoms <= 0 or num_atoms > 64:
            print("Invalid input. Try again!")
            continue

        gen_random = input("Enter '1' to generate Atoms randomly or '2' to set up Custom game: ")

        if gen_random == '1':
            atoms = get_atoms_randomly(num_atoms)
        elif gen_random == '2':
            atoms = get_atoms_from_user(num_atoms)
        else:
            print("Invalid input. Try again!")
            continue

        return atoms


def get_atoms_randomly(num_atoms):
    atoms = set()

    while len(atoms) < num_atoms:
        row = randint(1, 8)
        col = randint(1, 8)
        position = (row, col)
        atoms.add(position)

    return atoms


def get_atoms_from_user(num_atoms):
    while True:
        atoms = set()
        while len(atoms) < num_atoms:
            # get x-coordinate
            print('\nProcessing Atom #{}'.format(len(atoms)+1))
            row = input("Enter a x-coordinate : ")
            if not row.isdigit():
                print("Invalid input. Try again!")
                continue
            row = int(row)

            # get y-coordinate
            col = input("Enter a y-coordinate : ")
            if not col.isdigit():
                print("Invalid input. Try again!")
                continue
            col = int(col)

            if not (1 <= row <= 8 and 1 <= col <= 8):
                print("Invalid input. Try again!")
                continue

            position = (row, col)
            if position in atoms:
                print("Already entered this position. Try again!")
                continue

            atoms.add(position)
            print("Added an Atom at ({},{})".format(row, col))

        return atoms


def move():
    while True:
        row = input("Enter a x-coordinate : ")
        if not row.isdigit():
            print("Invalid input. Try again!")
            continue
        row = int(row)
        col = input("Enter a y-coordinate : ")
        if not col.isdigit():
            print("Invalid input. Try again!")
            continue
        col = int(col)
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
            continue
        return


if __name__ == '__main__':
    print("Welcome to Black Box Game!")
    ch = input("Start a game? (y/n) : ")
    print('\n')

    if ch == 'y':
        # get atoms
        atoms = get_atoms()

        # set up game
        game = BlackBoxGame(atoms)
        atoms_left = game.atoms_left()
        score = game.get_score()

        while True:
            print('\n')
            # print board and score
            game.print_board()
            print("Score :", score)
            print("Atoms Left :", atoms_left)

            move()

            # update score and atoms left
            score = game.get_score()
            atoms_left = game.atoms_left()

            # check if game is over
            if score <= 0 or atoms_left <= 0:
                break

            # see if user wants to terminate game early
            ch = input("Continue? (y/n) : ")
            if ch != 'y':
                break

        print('\n')

        # TO-DO: Multi-Player Mode

        if atoms_left <= 0 and score > 0:
            print("Congratulations! You won!")
        else:
            print("Game Over. Better luck next time!")
        print("Final Score :", score)
    else:
        print("No game started.")

    print("\nGoodbye!")