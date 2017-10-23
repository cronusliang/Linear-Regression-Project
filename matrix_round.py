#-*-coding:utf-8-*-



M = [[1.123456, 2.123456],
     [3.123456, 4.123456],
     [5.123456, 6.123456]]


for x in M:
    for y in range(len(x)):
        x[y] = round(x[y], 4)

#print M



def matxRound(M, decPts = 4):
    for x in M:
        for y in range(len(x)):
            x[y] = round(x[y], decPts)
    pass

print M