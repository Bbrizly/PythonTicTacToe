#❤ Daddy Bassam ❤️
import pickle, random
def Verify(list,a,ax,b,bx,c,cx):
    if list[a][ax] + list[b][bx] + list[c][cx] == "XXX": return 1
    elif list[a][ax] + list[b][bx] + list[c][cx] == "OOO": return 0
def Check(q,p):
    if Verify(rows, 0, 0, 1, 0, 2, 0) == q or Verify(rows, 0, 1, 1, 1, 2, 1) == q or Verify(rows, 0, 2, 1, 2, 2, 2) == q or Verify(rows, 0, 0, 1, 1, 2, 2) == q or Verify(rows, 0, 2, 1, 1, 2, 0) == q or rows[1] == p or rows[2] == p or rows[0] == p:
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
farags,milk,p1 = "wins","",True
soy = int(input("\nAt any time Type save to save or exit to exit.\nChoose: \n1. Play against Computer \n2. Play against yourself \n3. Load save\nChoose 1/2/3: "))
rows = [[e,e,e],[e,e,e],[e,e,e]]
if soy == 1:
    milk = input("Begin with X or O? ").upper()
    if milk == o:
        Computer(x,5)
        p1 = False
elif soy == 3:
    with open("board.pk", "rb") as pickle_file: ######LOAD
        soy = pickle.load(pickle_file)
        p1 = pickle.load(pickle_file)
        milk = pickle.load(pickle_file)
        rows = pickle.load(pickle_file)

while True:
    print("[y]\n 3 |{}|{}|{}|\n 2 |{}|{}|{}|\n 1 |{}|{}|{}|\n    1 2 3 [x]".format(rows[0][0], rows[0][1], rows[0][2], rows[1][0], rows[1][1], rows[1][2], rows[2][0], rows[2][1], rows[2][2]))
    ####### WIN CHECK #######
    boom = 0
    for i in rows:
        for j in i:
            if j == x:
                boom += 1
    if Check(1,m):
        print("Player 1",farags)
        break
    elif Check(0,n):
        print("Player 2",farags)
        break
    elif boom == 5:
        print("  Tie")
        break
    ####### inputs #######
    sushi = input("choose (x,y): ").upper().split(",")
    ## exit code ##
    if sushi[0] == "EXIT":
        exit()
    elif sushi[0] == "SAVE":
        with open("board.pk", "wb") as pickle_file:  #####SAVE
            pickle.dump(soy, pickle_file)
            pickle.dump(p1, pickle_file)
            pickle.dump(milk, pickle_file)
            pickle.dump(rows, pickle_file)
            print("\tGame Saved!")  # pickling code
            break
    a, b = (3 - int(sushi[1])), (int(sushi[0]) - 1)
    if rows[a][b] == e:
        if p1 == True:
            rows[a][b] = x
            if soy == 1 and milk == x:
                Computer(o,4)
            else:
                p1 = False
        elif p1 == False:
            rows[a][b] = o
            if soy == 1 and milk == o:
                Computer(x,5)
            else:
                p1 = True
        continue
    else:
        print("incorrect input try again")