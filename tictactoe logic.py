import random
#Daddy Bassam ❤️
'''
TO DO:
- pickling the 2D List
- Give option to start with x or o
Only if free:
- give user grid size freedom
- modular win check
'''
def Verify(list,a,ax,b,bx,c,cx):
    if list[a][ax] + list[b][bx] + list[c][cx] == "XXX":
        return 1
    elif list[a][ax] + list[b][bx] + list[c][cx] == "OOO":
        return 0
def Check(q,m):
    if Verify(rows, 0, 0, 1, 0, 2, 0) == 1 or Verify(rows, 0, 1, 1, 1, 2, 1) == 1 or Verify(rows, 0, 2, 1, 2, 2, 2) == 1 or Verify(rows, 0, 0, 1, 1, 2, 2) == 1 or Verify(rows, 0, 2, 1, 1, 2, 0) == 1 or rows[1] == m or rows[2] == m or rows[0] == m:
        return(q)
e = "_"
x = "X"
o = "O"
q = "Q"
m = ["X","X","X"]
n = ["O","O","O"]
soy = int(input("Choose: \n1. Play against Computer \n2. Play against yourself \n3. Load save\nChoose 1/2/3: "))
milk = input("Begin with X or O? ").upper()
rows = [[e,e,e],[e,e,e],[e,e,e]]

p1 = True
while True:
    print("_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[0][0], rows[0][1], rows[0][2], rows[1][0], rows[1][1],
                                                             rows[1][2], rows[2][0], rows[2][1], rows[2][2]))
    ####### WIN CHECK #######
    if Check(1,m):
        print("player 1 wins")
        break
    elif Check(0,n):
        if soy == 1:
            print("Computer wins")
        else:
            print("player 2 wins")
        break
    boom = 0
    for i in rows:
        for j in i:
            if j == x:
                boom += 1
    if boom == 5:
        print("Tie")
        break

    ####### inputs #######

    sushi = input("choose (x,y): ").split(",")
    ## exit code ##
    if sushi[0] == "exit":
        print("pickle")
        exit()

    a, b = (3 - int(sushi[1])), (int(sushi[0]) - 1)
    if rows[a][b] == e:
        if p1 == True:
            rows[a][b] = x
            # Computer
            if soy == 1:
                boom = 0
                while True:
                    q,m = random.randrange(0, 3),random.randrange(0, 3)
                    if rows[q][m] == e:
                        rows[q][m] = o
                        break
                    else:
                        #preventing infinite loop once ai has no moves
                        for i in rows:
                            for j in i:
                                if j == o:
                                    boom += 1
                        if boom == 4:
                            break
            else:
                p1 = False
        elif p1 == False:
            rows[a][b] = o
            p1 = True
        continue
    else:
        print("incorrect input try again")