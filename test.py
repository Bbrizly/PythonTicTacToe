#❤ Daddy Bassam ❤️
import pickle, random
def Board():
    print(
        "\n[y]\n 3 |{}|{}|{}|\n 2 |{}|{}|{}|\n 1 |{}|{}|{}|\n    1 2 3 [x]\n".format(rows[0][0], rows[0][1], rows[0][2],
                                                                                     rows[1][0], rows[1][1], rows[1][2],
                                                                                     rows[2][0], rows[2][1],
                                                                                     rows[2][2]))
def Verify(list,a,ax,b,bx,c,cx):
    if list[a][ax] + list[b][bx] + list[c][cx] == "XXX": return 1
    elif list[a][ax] + list[b][bx] + list[c][cx] == "OOO": return 0
def Check(q,p):
    if Verify(rows, 0, 0, 1, 0, 2, 0) == q or Verify(rows, 0, 1, 1, 1, 2, 1) == q or Verify(rows, 0, 2, 1, 2, 2, 2) == q or Verify(rows, 0, 0, 1, 1, 2, 2) == q or Verify(rows, 0, 2, 1, 1, 2, 0) == q or rows[1] == p or rows[2] == p or rows[0] == p:
        return True
def Wincheck():
    Board()
    b,z = 0,0
    for i in rows:
        for j in i:
            if j == x: b += 1
            if j == o: z += 1
    if Check(1, m):
        if soy == 1:
            if milk == o:   print("=-=-[Computer Won in {} moves]-=-=\n".format(b))
            else:   print("=-=-[You Won in {} moves]-=-=\n".format(b))
        else:   print("=-=-[x Won in {} moves]-=-=\n".format(b))
        return True
    elif Check(0, n):
        if soy == 1 and milk == x:
            if milk == x:   print("=-=-[Computer Won in {} moves]-=-=\n".format(z))
            else:   print("=-=-[You Won in {} moves]-=-=\n".format(z))
        else:   print("=-=-[o Won in {} moves]-=-=\n".format(z))
        return True
    elif b == 5:
        print("  Tie\n")
        return True
def Computer(salmon,max):
    while True:
        q = random.randrange(0, 3)
        m = random.randrange(0, 3)
        if rows[q][m] == e:
            rows[q][m] = salmon
            break
        else:# preventing infinite loop once ai has no moves
            boom = 0
            for i in rows:
                for j in i:
                    if j == salmon:
                        boom += 1
            if boom == max:
                break
e,x,o,m,n = "_","X","O", ["X","X","X"], ["O","O","O"]
milk,p1 = "",True
soy = int(input("\nWelcome to TicTacToe,\nAt any time Type stop to save and exit.\nChoose: \n1. User Vs Computer \n2. User Vs User \n3. Resume Old Game\nChoose 1/2/3: "))
rows = [[e,e,e],[e,e,e],[e,e,e]]
while True:
    p1 = True
    if soy == 1:
        milk = input("Begin with X or O? ").upper()
        if milk == o:
            Computer(x, 5)
            p1 = False
    elif soy == 3:
        with open("board.pk", "rb") as pickle_file:  ######LOAD
            soy = pickle.load(pickle_file)
            p1 = pickle.load(pickle_file)
            milk = pickle.load(pickle_file)
            rows = pickle.load(pickle_file)
    Board()
    while True:
        sushi = input("choose (x,y): ").upper().split(",")
        if sushi[0] == "STOP": #EXIT CODE
            with open("board.pk", "wb") as pickle_file:  #####SAVE
                pickle.dump(soy, pickle_file)
                pickle.dump(p1, pickle_file)
                pickle.dump(milk, pickle_file)
                pickle.dump(rows, pickle_file)
                print("\tGame Saved!")  # pickling code
                exit()
        a, b = (3 - int(sushi[1])), (int(sushi[0]) - 1)
        if rows[a][b] == e:
            if p1 == True:
                rows[a][b] = x
                if soy == 1 and milk == x:
                    Computer(o,4)
                else:
                    p1 = False
                if Wincheck():
                    break
            elif p1 == False:
                rows[a][b] = o
                if soy == 1 and milk == o: Computer(x,5)
                else: p1 = True
                if Wincheck(): break
            continue
        else:
            print("Unfortunately, the ({},{}) move you entered is already occupied, please try again".format(sushi[0],sushi[1]))
    rows = [[e, e, e], [e, e, e], [e, e, e]]
    if input("Would you like to play again? (Y/N)").upper() == "N":
        print("Thank you for playing!")
        break