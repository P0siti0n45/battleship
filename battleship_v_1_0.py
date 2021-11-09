clearConsole = lambda: print('\n' * 50)
from termcolor import colored




def is_full(board):
    for i in board:
        for j in i:
            if j == "0":
                return False
    return True

def get_move(board,difficulty):
    row = 0
    col = 0
    coords = input("Choose a field  ")
    if coords.lower() == "quit":
        sys.exit("Thanks for playing, Goodbye!")
    if len(coords) < 2 or len(coords) > 10:
        print("Invalid coordinates entered, please try again!")
        get_move(board, difficulty)
  

    row = coords[:len(coords) // 2]
    col = coords[len(coords) // 2:]

    if difficulty == 1 and int(col) > 5:
        print("Invalid coordinates entered, please try again!")
        get_move(board, difficulty)
    if difficulty == 2 and int(col) > 7:
        print("Invalid coordinates entered, please try again!")
        get_move(board, difficulty)
    if difficulty == 3 and int(col) > 10:
        print("Invalid coordinates entered, please try again!")
        get_move(board, difficulty)

    if row.lower() == "a":
        x = 0
    elif row.lower() == "b":
        x = 1
    elif row.lower() == "c":
        x = 2
    elif row.lower() == "d":
        x = 3
    elif row.lower() == "e":
        x = 4
    else:
        x = 0
        y = 0
        print("Invalid coordinates entered, please try again!")
        get_move(board, difficulty)

    if col == "1":
        y = 0
    elif col == "2":
        y = 1
    elif col == "3":
        y = 2
    elif col == "4":
        y = 3
    elif col == "5":
        y = 4
    elif col == "6":
        y = 5
    elif col == "7":
        y = 6
    elif col == "8":
        y = 7
    elif col == "9":
        y = 8
    elif col == "10":
        y = 9
    else:
        x = 0
        y = 0
        print("Invalid coordinates entered, please try again!")
        get_move(board, difficulty)
       
    if board[y][x] == "X":
        x = 0
        y = 0
        print("Position already occupied!")
        get_move(board, difficulty)
        
    return x, y

def check_shooting(board1,board2,y,x,cols,turns):
    if board1[y][x] == board2[y][x]:
        print("You've hit a ship!")
    elif board1[y][x] != board2[y][x]:
        clearConsole()
        print(f"Turns taken so far: {turns}")
        print_board(board,rows,cols)
        print("You missed!")
        input("Press Enter to continue...")
        board[y1][x1] = "0"
        board[y2][x2] = "0"
        clearConsole()
    else:
        clearConsole()
        print(f"Turns taken so far: {turns}")
        print_board(board,rows,cols)
        print("You already hit that spot!")
        input("Press Enter to continue...")
        board[y1][x1] = "0"
        board[y2][x2] = "0"
        clearConsole()

def place_ship(board,y,x):
    if board[y][x] == "X":
        print("Position already occupied!")
    else:
        clearConsole()
        board[y][x] = ("X")
        #print_board(board,rows,cols)
        #clearConsole() 

def main_menu():
    print(colored("Welcome to Battleship!", 'red'))
    print("1. Player vs Player")
    print("2. Player vs Ai")
    print("3. Ai vs Player")
    gamemode = input("Please select a gamemode: ")
    if gamemode == "1":
        clearConsole()
        print("Player vs Player is selected.")
    if gamemode == "2":
        clearConsole()
        print("Player vs Ai is selected.")  
    if gamemode == "3":
        clearConsole()
        print("Ai vs Player is selected.")

def difficulty_menu():
    print(colored("1. Easy   -> 5x5"), 'green')
    print(colored("2. Medium -> 5x7"), 'yellow')
    print(colored("3. Hard   -> 5x10"), 'red')
    difficulty = input("Please select the desired difficulty: ")
    if difficulty == "1":
        rows = 5
        cols = 5
        difficulty = 1
        return rows, cols, difficulty
    if difficulty == "2":
        rows = 7
        cols = 5
        difficulty = 2
        return rows, cols, difficulty
    if difficulty == "3":
        rows = 10
        cols = 5
        difficulty = 3
        return rows, cols, difficulty
    else:
        clearConsole()
        print("Invalid selection:")
        difficulty_menu()

def generate_board(rows, cols):
    player1_board = []
    player2_board = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("0")
        player1_board.append(row)

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append("0")
        player2_board.append(row)

    return player1_board, player2_board

def print_board(board,rows,cols):
    i = 0
    j = 0
    letters = ["A","B","C","D","E"]
    numbers = ["1","2","3","4","5","6","7","8","9","10"]
    print("     ", end = '')
    for x in range(rows):
        print(f"{numbers[x]}", end=' ')
    print("")
    if rows == 5:
        print("     ", end = '')
        print("-" * (x+rows))
        while i in range(cols):
            j = 0
            print(f"{letters[i]}   |", end = "")
            while j in range(rows):
                print(f"{board[j][i]} ",end = "")
                j += 1
            print("")
            i += 1
            
    if rows == 7:
        print("     ", end = '')
        print("-" * (x+rows))
        while i in range(cols):
            j = 0
            print(f"{letters[i]}   |", end = "")
            while j in range(rows):
                print(f"{board[j][i]} ",end = "")
                j += 1
            print("")
            i += 1
    if rows == 10:
        print("     ", end = '')
        print("-" * (x+rows))
        while i in range(cols):
            j = 0
            print(f"{letters[i]}   |", end = "")
            while j in range(rows):
                print(f"{board[j][i]} ",end = "")
                j += 1
            print("")
            i += 1
    return

def main():
    turns_taken = 0
    player1_ships = 5
    player2_ships = 5
    clearConsole()
    main_menu()
    rows,cols,difficulty = difficulty_menu()
    player1_board, player2_board = generate_board(rows,cols)
    while True:
        if player1_ships >= 1:
            clearConsole()
            print(f"Player 1: {player1_ships} ships remaining.\n")
            print_board(player1_board,rows,cols)
            y, x = get_move(player1_board,difficulty)
            place_ship(player1_board,x,y)
            player1_ships = player1_ships - 1
            clearConsole()
            print_board(player1_board,rows,cols)
        elif player2_ships >= 1:
            clearConsole()
            print(f"Player 2: {player2_ships} ships remaining.\n")
            print_board(player2_board,rows,cols)
            y, x = get_move(player2_board,difficulty)
            clearConsole()
            place_ship(player2_board,x,y)
            player2_ships = player2_ships - 1
            clearConsole()
            print_board(player2_board,rows,cols)
        if player1_ships == 0 and player2_ships == 0:
            #Shooting
            pass
        
        
        
    
main()
