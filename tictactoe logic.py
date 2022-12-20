e = "_"
x = "✖"
o = "⍜"
rows = [[e,e,e],[e,e,e],[e,e,e]]
p1= True
while True:
    print("_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[0][0],rows[0][1],rows[0][2],rows[1][0],rows[1][1],rows[1][2],rows[2][0],rows[2][1],rows[2][2]))
    sushi = input("choose (x,y): ").split(",")
    if sushi[0] == "exit":
        f = open("board_data.txt","w")
        f.write(rows)
        f.close()
        exit()
    elif p1 == True:
        rows[3-int(sushi[1])][int(sushi[0])-1] = x
        p1 = False
    elif p1 == False:
        rows[3-int(sushi[1])][int(sushi[0])-1] = o
        p1 = True











'''
from collections import Counter
import random

print("Welcome to Tic Tac Toe")
Number_Of_Players = input("Enter number of players: ")
Player_One = input("Choose x or o: ")
Player_Two = "undefined"

if Player_One == "x":
    Player_Two = "O"
    Player_One = "X"
elif Player_One == "o":
    Player_Two = "X"
    Player_One = "O"

board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']


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


print(board[2:8:2])


def man_vs_man(board):
    global counts
    if Number_Of_Players == "2":

        while Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
                board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(board[1:10:3]) == False and Verify(
                board[2:11:3]) == False and Verify(board[0:12:4]) == False and Verify(board[2:8:2]) == False:
            Player_One_Move_list = input("Enter Move: ").split(",")
            print(Player_One_Move_list)
            if Player_One_Move_list[0] == "exit":
                f = open("board_data.txt", "w")
                f.write(board)
                f.close()
                exit()
            elif Player_One_Move_list[0] == "1":
                board[-1 + int(Player_One_Move_list[1])] = Player_One
            elif Player_One_Move_list[0] == "2":
                board[2 + int(Player_One_Move_list[1])] = Player_One
            elif Player_One_Move_list[0] == "3":
                board[5 + int(Player_One_Move_list[1])] = Player_One
            BoardDisplay(board)
            print()

            if Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
                    board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(
                    board[1:10:3]) == False and Verify(board[2:11:3]) == False and Verify(
                    board[0:12:4]) == False and Verify(board[2:8:2]) == False:
                Player_Two_Move = input("Enter Move: ")
                Player_Two_Move_list = Player_Two_Move.split(",")
                print(Player_Two_Move_list)
                if Player_Two_Move_list[0] == "1":
                    board[-1 + int(Player_Two_Move_list[1])] = Player_Two
                elif Player_Two_Move_list[0] == "2":
                    board[2 + int(Player_Two_Move_list[1])] = Player_Two
                elif Player_Two_Move_list[0] == "3":
                    board[5 + int(Player_Two_Move_list[1])] = Player_Two
            BoardDisplay(board)
            print()

    counts = Counter(board)
    counts_x = counts["X"]
    counts_o = counts["O"]
    if (counts_x > counts_o and Player_One == "X") or (counts_x < counts_o and Player_One == "O"):
        print("Player one Wins")
    else:
        print("Player two wins")


def man_vs_machine(board):
    global counts
    while Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
            board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(board[1:10:3]) == False and Verify(
        board[2:11:3]) == False and Verify(board[0:12:4]) == False and Verify(board[2:8:2]) == False:
        Player_One_Move = input("Enter Move: ")
        Player_One_Move_list = Player_One_Move.split(",")
        print(Player_One_Move_list)
        if Player_One_Move_list[0] == "1":
            board[-1 + int(Player_One_Move_list[1])] = Player_One
        elif Player_One_Move_list[0] == "2":
            board[2 + int(Player_One_Move_list[1])] = Player_One
        elif Player_One_Move_list[0] == "3":
            board[5 + int(Player_One_Move_list[1])] = Player_One
        BoardDisplay(board)
        print()

        if Verify(board[0:3:1]) == False and Verify(board[3:6:1]) == False and Verify(
                board[6:9:1]) == False and Verify(board[0:9:3]) == False and Verify(
            board[1:10:3]) == False and Verify(board[2:11:3]) == False and Verify(
            board[0:12:4]) == False and Verify(board[2:8:2]) == False:
            index = random.randint(0, len(board))
            while board[index] != "X" and board[index] != "O":
                board[index] = Player_Two
        BoardDisplay(board)
        print()

    counts = Counter(board)
    counts_x = counts["X"]
    counts_o = counts["O"]
    if (counts_x > counts_o and Player_One == "X") or (counts_x < counts_o and Player_One == "O"):
        print("Player one Wins")
    else:
        print("Computer wins")


if (Number_Of_Players == "2"):
    man_vs_man(board)
else:
    man_vs_machine(board)
'''
