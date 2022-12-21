#Daddy Bassam ❤️
def Verify(list,a,ax,b,bx,c,cx):
    if list[a][ax] + list[b][bx] + list[c][cx] == "XXX":
        return 1
    elif list[a][ax] + list[b][bx] + list[c][cx] == "OOO":
        return 0
e= "_"
x = "X"
o = "O"
rows = [[e,e,e],[e,e,e],[e,e,e]]
p1 = True
while True:
    print("_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[0][0],rows[0][1],rows[0][2],rows[1][0],rows[1][1],rows[1][2],rows[2][0],rows[2][1],rows[2][2]))

    if Verify(rows,0,0,1,0,2,0) == 1 or Verify(rows,0,1,1,1,2,1) == 1 or Verify(
        rows,0,2,1,2,2,2) == 1 or Verify(rows,0,0,1,1,2,2) == 1 or Verify(
        rows,0,2,1,1,2,0) == 1 or Verify(rows,0,0,0,1,0,2) == 1 or Verify(
        rows,1,0,1,1,1,2) == 1 or Verify(rows,2,0,2,1,2,2) == 1:
        print("player 1 wins")
        break
    elif Verify(rows,0,0,1,0,2,0) == 0 or Verify(rows,0,1,1,1,2,1) == 0 or Verify(
        rows,0,2,1,2,2,2) == 0 or Verify(rows,0,0,1,1,2,2) == 0 or Verify(
        rows,0,2,1,1,2,0) == 0 or Verify(rows,0,0,0,1,0,2) == 0 or Verify(
        rows,1,0,1,1,1,2) == 0 or Verify(rows,2,0,2,1,2,2) == 0:
        print("player 2 wins")
        break

    sushi = input("choose (x,y): ").split(",")
    ## exit code ##
    if sushi[0] == "exit":
        print("pickle")
        exit()
    a,b = (3-int(sushi[1])),(int(sushi[0])-1)
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