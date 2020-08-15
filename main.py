from blackboxgame import BlackBoxGame

if __name__ == '__main__':
    ch = input("Start a game? (y/n) : ")
    if ch == 'y':
        game = BlackBoxGame([(3, 2), (3, 7), (6, 4), (8, 7)])
        game.print_board()
        row = col = 0
        while True:
            input_row = input("Enter a row : ")
            if not input_row.isdigit():
                print("Invalid row. Try again:")
            else:
                row = int(input_row)
            input_col = input("Enter a column : ")
            if not input_col.isdigit():
                print("Invalid column. Try again:")
            else:
                col = int(input_col)
            print(row, col)
            break