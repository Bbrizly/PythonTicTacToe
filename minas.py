from collections import Counter
import random
import pickle

print("Welcome to Tic Tac Toe")
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']
Game_Choice = input("new game or old game (n,o): ")
Player_One = ""
Player_Two = ""
Number_Of_Players = 0
if Game_Choice == "n":
    Number_Of_Players = input("Enter number of players (1 or 2): ")
    Player_One = input("Choose x or o: ")
    Player_Two = "undefined"
    if Player_One == "x" or "X":
        Player_Two = "O"
        Player_One = "X"
    elif Player_One == "o" or "O":
        Player_Two = "X"
        Player_One = "O"
else:
    game = input("which game? ")
    with open(game, "rb") as pickle_file:
        board = pickle.load(pickle_file)
        Player_One = pickle.load(pickle_file)
        Player_Two = pickle.load(pickle_file)
        Number_Of_Players = pickle.load(pickle_file)

def BoardDisplay(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("-" * 9)
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("-" * 9)
    print(board[6] + " | " + board[7] + " | " + board[8])

def Verify(list):
    if list[0] + list[1] + list[2] == "XXX" or list[0] + list[1] + list[2] == "OOO":
        return True
    else:
        return False

def man_vs_man(board):
    global Player_One, Player_Two
    Save_For_Later = ""

    BoardDisplay(board)
    if Number_Of_Players == "2":
        Moves = []
        count = 0
        i = 0
        y = 0
        z = 0

        for e in board:
            if count < 3:
                i += 1
                if e != '-':
                    Moves.append("1," + str(i))
            if 2 < count < 6:
                y += 1
                if e != '-':
                    Moves.append("2," + str(y))
            if 5 < count < 9:
                z += 1
                if e != '-':
                    Moves.append("3," + str(z))
            count += 1

        while Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
                board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(board[1:8:3]) == False and Verify(
            board[2:9:3]) == False and Verify(board[0:9:4]) == False and Verify(
            board[2:8:2]) == False and Save_For_Later != "y":

            if (len(Moves) % 2 == 0 or len(Moves) == 0):

                Player_One_Move = input("Enter Move player 1: ")
                Player_One_Move_list = Player_One_Move.split(",")

                while Player_One_Move in Moves:
                    Player_One_Move = input("Enter Move player 1: ")
                    Player_One_Move_list = Player_One_Move.split(",")

                Save_For_Later = input("Save Everything after those changes (y,n): ")
                Moves.append(Player_One_Move)
                print(Player_One_Move_list)

                if Player_One_Move_list[0] == "1":
                    board[-1 + int(Player_One_Move_list[1])] = Player_One
                    BoardDisplay(board)
                elif Player_One_Move_list[0] == "2":
                    board[2 + int(Player_One_Move_list[1])] = Player_One
                    BoardDisplay(board)
                elif Player_One_Move_list[0] == "3":
                    board[5 + int(Player_One_Move_list[1])] = Player_One
                    BoardDisplay(board)
                    print()


            elif Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
                    board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(
                board[1:10:3]) == False and Verify(board[2:11:3]) == False and Verify(
                board[0:12:4]) == False and Verify(board[2:8:2]) == False and Save_For_Later != "y":

                Player_Two_Move = input("Enter Move Player 2: ")
                Player_Two_Move_list = Player_Two_Move.split(",")

                while Player_Two_Move in Moves:
                    Player_Two_Move = input("Enter Move player 2: ")
                    Player_Two_Move_list = Player_Two_Move.split(",")

                Save_For_Later = input("Save Everything after those changes (y,n): ")
                Moves.append(Player_Two_Move)
                print(Player_Two_Move_list)
                if Player_Two_Move_list[0] == "1":
                    board[-1 + int(Player_Two_Move_list[1])] = Player_Two
                    BoardDisplay(board)
                elif Player_Two_Move_list[0] == "2":
                    board[2 + int(Player_Two_Move_list[1])] = Player_Two
                    BoardDisplay(board)
                elif Player_Two_Move_list[0] == "3":
                    board[5 + int(Player_Two_Move_list[1])] = Player_Two
                    BoardDisplay(board)

    counts = Counter(board)
    counts_x = counts["X"]
    counts_o = counts["O"]
    if Save_For_Later == "n":
        if (counts_x > counts_o and Player_One == "X") or (counts_x and Player_One == "O"):
            print("Player one Wins")
        elif (counts_x + counts_o) == 9:
            print("Tie")
        else:
            print("Player Two wins")
    else:
        file_name = input("file name ending with (.pk)")
        with open(file_name, "wb") as pickle_file:
            pickle.dump(board, pickle_file)
            pickle.dump(Player_One, pickle_file)
            pickle.dump(Player_Two, pickle_file)
            pickle.dump(Number_Of_Players, pickle_file)
            print("game saved")  # pickling code
    '''
    with open(game, "rb") as pickle_file:
        board = pickle.load(pickle_file)
        Player_One = pickle.load(pickle_file)
        Player_Two = pickle.load(pickle_file)
        Number_Of_Players = pickle.load(pickle_file)
    '''

def man_vs_machine(board):
    global counts
    Save_For_Later = ""

    while Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
            board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(board[1:10:3]) == False and Verify(
        board[2:11:3]) == False and Verify(board[0:12:4]) == False and Verify(board[2:8:2]) == False and Save_For_Later !="y":

        Moves = []
        count = 0
        i = 0
        y = 0
        z = 0

        for e in board:
            if count < 3:
                i += 1
                if e != '-':
                    Moves.append("1," + str(i))
            if 2 < count < 6:
                y += 1
                if e != '-':
                    Moves.append("2," + str(y))
            if 5 < count < 9:
                z += 1
                if e != '-':
                    Moves.append("3," + str(z))
            count += 1
        print()
        if (len(Moves) % 2 == 0 or len(Moves) == 0):

            Player_One_Move = input("Enter Move player 1: ")
            Player_One_Move_list = Player_One_Move.split(",")

            while Player_One_Move in Moves or str(int(Player_One_Move_list[1])-1) in Moves:
                Player_One_Move = input("Enter Move player 1: ")
                Player_One_Move_list = Player_One_Move.split(",")

            Save_For_Later = input("Save Everything after those changes (y,n): ")
            Moves.append(Player_One_Move)
            print(Player_One_Move_list)

            if Player_One_Move_list[0] == "1":
                board[-1 + int(Player_One_Move_list[1])] = Player_One
                BoardDisplay(board)
            elif Player_One_Move_list[0] == "2":
                board[2 + int(Player_One_Move_list[1])] = Player_One
                BoardDisplay(board)
            elif Player_One_Move_list[0] == "3":
                board[5 + int(Player_One_Move_list[1])] = Player_One
                BoardDisplay(board)
                print()

        elif Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
                board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(
            board[1:10:3]) == False and Verify(board[2:11:3]) == False and Verify(
            board[0:12:4]) == False and Verify(board[2:8:2]) == False:

            index = random.randint(0, len(board))
            while board[index] != "-":
             index = random.randint(0, len(board))

            board[index] = Player_Two
            BoardDisplay(board)
            print("\n\n")

    counts = Counter(board)
    counts_x = counts["X"]
    counts_o = counts["O"]
    if Save_For_Later == "n":
        if (counts_x > counts_o and Player_One == "X") or (counts_x and Player_One == "O"): print("Player one Wins")
        elif (counts_x + counts_o) == 9: print("Tie")
        else: print("Player Two wins")
    else:
        file_name = input("file name ending with (.pk)")
        with open(file_name, "wb") as pickle_file:
            pickle.dump(board, pickle_file)
            pickle.dump(Player_One, pickle_file)
            pickle.dump(Player_Two, pickle_file)
            pickle.dump(Number_Of_Players, pickle_file)
            print("game saved")  # pickling code


if Number_Of_Players == "2": man_vs_man(board)
else: man_vs_machine(board)