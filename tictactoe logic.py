e = "_"
x = "✖"
o = "⍜"
rows = [[e,e,e],[e,e,e],[e,e,e]]
p1= True
while True:
    print("_______\n|{}|{}|{}|\n|{}|{}|{}|\n|{}|{}|{}|".format(rows[0][0],rows[0][1],rows[0][2],rows[1][0],rows[1][1],rows[1][2],rows[2][0],rows[2][1],rows[2][2]))
    sushi = input("choose (x,y): ").split(",")
    if p1 == True:
        rows[3-int(sushi[1])][int(sushi[0])-1] = x
        p1 = False
    elif p1 == False:
        rows[3-int(sushi[1])][int(sushi[0])-1] = o
        p1 = True
