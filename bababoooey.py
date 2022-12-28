#Daddy Bassam ❤
'''
TO DO:
- pickling the 2D List
- add random AI
- Menu screen: 1-1v1 2-AI 3-Retrieve save
Only if free:
- give user grid size freedom
- modular win check
'''
import random

def Verify(list,a,ax,b,bx,c,cx):
    if list[a][ax] + list[b][bx] + list[c][cx] == "XXX":
        return 1
    elif list[a][ax] + list[b][bx] + list[c][cx] == "OOO":
        return 0

def Check(q, row):
    if Verify(area, 0, 0, 1, 0, 2, 0) == q or Verify(area, 0, 1, 1, 1, 2, 1) == q or Verify(area, 0, 2, 1, 2, 2, 2) == q or Verify(area, 0, 0, 1, 1, 2, 2) == q or\
            Verify(area, 0, 2, 1, 1, 2, 0) == q or area[1] == row or area[2] == row or area[0] == row:
        return(1)

def save(location, area):
    if location[0] == "stop":
        gameState = open("game_state.txt", "w")
        gridArea = str(len(area)) + "\n"
        gameState.write(str(gridArea))
        gameState.write(mode)
        for i in range(len(area)):
            # area2 = str(area[i]) +"\n"
            gameState.writelines(area[i])
        gameState.close()

e = "_"
x = "X"
o = "O"
q = "Q"
m = ["X","X","X"]
n = ["O","O","O"]

#by changing the rows and columns we will change the grid area
# rows, columns = 3, 3
# area = [[e]* columns] * rows
area = [[e,e,e],[e,e,e],[e,e,e]]

def userVsuser(area, m, n, mode):
    p1 = True
    while True:
    #this will print the grid if it's of any area
        print("___")
        for i in range(len(area)):
            for k in range(len(area[0])):
                print("|{}".format(area[i][k]) ,end = "")
                if k == len(area[0]) -1:
                    print("|")
        print("___")

        if Check(1,m):
            print("player 1 wins")
            break
        elif Check(0,n):
            print("player 2 wins")
            break

        location = input("choose (x,y): ").split(",")
        ## exit code ##
        if location[0] == "stop":
            save(location, area)
            break

        a, b = (int(location[0]) -1), (int(location[1]) -1)
        if area[a][b] == e:
            if p1 == True:
                area[a][b] = x
                p1 = False
            elif p1 == False:
                area[a][b] = o
                p1 = True
            continue
        else:
            print("incorrect input try again")

def userVsComputer(area, m, n):
    counter = 1
    while True:
        # this will print the grid if it's of any area
        print("___")
        for i in range(len(area)):
            for k in range(len(area[0])):
                print("|{}".format(area[i][k]), end="")
                if k == len(area[0]) - 1:
                    print("|")
        print("___")
        #the user input
        if counter % 2 == 1:
            if Check(1,m):
                print("player 1 wins")
                break
            elif Check(0,n):
                print("player 2 wins")
                break

            location = input("choose (x,y): ").split(",")
            ## exit code ##
            if location[0] == "stop":
                print("pickle")
                exit()

            a, b = (int(location[0]) -1), (int(location[1]) -1)
            #check the input
            while area[a][b] in [x, o]:
                print("incorrect input try again")
                location = input("choose (x,y): ").split(",")
                ## exit code ##
                if location[0] == "exit":
                    print("pickle")
                    exit()

                a, b = (int(location[0]) - 1), (int(location[1]) - 1)

            area[a][b] = x
        #the computer
        else:
            if Check(1, m):
                print("player 1 wins")
                break
            elif Check(0, n):
                print("computer wins")
                break

            #for if the grid is not 3 by 3
            #the ai choses a place at random
            rowIndex, columnIndex = [], []
            for i in range(len(area)):
                rowIndex.append(i)
            for i in range(len(area[0])):
                columnIndex.append(i)
            a, b = random.choice(rowIndex), random.choice(columnIndex)

            # check the move
            while area[a][b] in [x, o]:
                a, b = random.choice(rowIndex), random.choice(columnIndex)

            area[a][b] = o

        counter += 1

def resume(area, x, o):
    area = [[e,e,e],[e,e,e],[e,e,e]]

    gameState = open("game_state.txt", "r")
    gridArea = gameState.readline().strip("\n")
    mode = gameState.readline().strip("\n")
    for i in range(int(gridArea)):
        row = gameState.read(int(gridArea))
        for n in range(int(gridArea)):
            if row[n] == "X":
                area[i][n] = x
            elif row[n] == "O":
                area[i][n] = o
    gameState.close()
    print(mode)
    if mode == "1v1":
        userVsuser(area, m, n, mode)
    else:
        userVsComputer(area, m, n)


mode= input("1v1 or cpu or continue: ")
if mode == "1v1":
    userVsuser(area, m, n, mode)
elif mode == "cpu":
    userVsComputer(area, m, n)
elif mode == "continue":
    resume(area, x, o)