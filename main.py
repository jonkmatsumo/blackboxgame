from blackboxgame import BlackBoxGame

if __name__ == '__main__':
    ch = input("Start a game? (y/n) : ")
    if ch == 'y':
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        game.print_board()
        cont = 'y'
        while cont == 'y':
            cont = input("Enter a position (row, col) (y/n) : ")
