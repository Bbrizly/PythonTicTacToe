#Daddy Bassam ❤️
def Verify(list,a,ax,b,bx,c,cx):
    if list[a][ax] + list[b][bx] + list[c][cx] == "XXX":
        return 1
    elif list[a][ax] + list[b][bx] + list[c][cx] == "OOO":
        return 0
def Check(x,a,b):
    win = False
    # TOP RIGHT
    if a > 1 and a < len(sushi[0]) and (b+1) > 0 and b < len(sushi):
        if rows[a - 1][b + 1] == x: #top right
            if a > 2 and a < len(sushi[0]) and (b+1) > 0 and b < len(sushi):
                if rows[a - 2][b + 2] == x:#more top right
                    win = True
                elif rows[a + 1][b - 1] == x:  # origin's bottom left
                    win = True
    # TOP LEFT
    if rows[a - 1][b - 1] == x:  # top left
        if rows[a - 2][b - 2] == x:  # more top left
            win = True
        elif rows[a + 1][b + 1] == x:  # origin's bottom right
            win = True
    # BOTTOM RIGHT
    if rows[a + 1][b + 1] == x:  # bottom right
        if rows[a + 2][b + 2] == x:  # more bottom right
            win = True
        elif rows[a - 1][b - 1] == x:  # origin's top left
            win = True
    # BOTTOM LEFT
    if rows[a + 1][b - 1] == x:  # bottom left
        if rows[a + 2][b - 2] == x:  # more bottom left
            win = True
        elif rows[a - 1][b + 1] == x:  # origin's top right
            win = True

    return (win)




    # if 1's top left same then check that's top left , if not then check bottom right of 1 if yes then check taht's bottom right
    # if 1's up same then check thats up, if not then check 1's down if yes then check that's down
    # if 1's right same then check that's right, if not then check 1's left if yes then check that's left


e = "_"
x = "X"
o = "O"
q = "Q"
m = ["X","X","X"]
n = ["O","O","O"]
rows = [[1,2,3],[4,5,6],[7,8,9]]
print("_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[0][0],rows[0][1],rows[0][2],rows[1][0],rows[1][1],rows[1][2],rows[2][0],rows[2][1],rows[2][2]))
rows = [[e,e,e],[e,e,e],[e,e,e]]
rows = [[q,q,q],[q,e,e,e,q],[q,e,e,e,q],[q,e,e,e,q],[q,q,q]] #TO PREVENT OUT OF INDEX INPUTS
#rows = [["X",e,"X"],[e,e,e],["X",e,"X"]]
#rows = [[1,2,3],[4,5,6],[7,8,9]]
p1 = True

print("_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[0][0],rows[0][1],rows[0][2],rows[1][0],rows[1][1],rows[1][2],rows[2][0],rows[2][1],rows[2][2]))

while True:
    print("_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[1][1],rows[1][2],rows[1][3],rows[2][1],rows[2][2],rows[2][3],rows[3][1],rows[3][2],rows[3][3]))

    '''
    if Verify(rows,0,0,1,0,2,0) == 1 or Verify(rows,0,1,1,1,2,1) == 1 or Verify(
        rows,0,2,1,2,2,2) == 1 or Verify(rows,0,0,1,1,2,2) == 1 or Verify(
        rows,0,2,1,1,2,0) == 1 or rows[1] == m or rows[2] == m or rows[0] == m:
        print("player 1 wins")
        break
    elif Verify(rows,0,0,1,0,2,0) == 0 or Verify(rows,0,1,1,1,2,1) == 0 or Verify(
        rows,0,2,1,2,2,2) == 0 or Verify(rows,0,0,1,1,2,2) == 0 or Verify(
        rows,0,2,1,1,2,0) == 0 or rows[1] == m or rows[2] == n or rows[0] == n:
        print("player 2 wins")
        break
    '''
    sushi = input("choose (x,y): ").split(",")
    a, b = (3 - int(sushi[1])), (int(sushi[0]) - 1)
    a, b = (4 - int(sushi[1])), (int(sushi[0]) - 0)

    Check("X",a,b)
    ## exit code ##
    if sushi[0] == "exit":
        print("pickle")
        exit()
    if rows[a][b] == e:
        if p1 == True:
            rows[a][b] = x
            p1 = False
        elif p1 == False:
            rows[a][b] = o
            p1 = True
        continue
    else:
        print("incorrect input try again")
