
import random
import os

table = {'x1y1' : 7, 'x2y1' : 5, 'x3y1' : 4, 'x4y1' : 8, 'x5y1' : 9, 'x6y1' : 1, 'x7y1' : 6, 'x8y1' : 2, 'x9y1' : 3, 'x1y2' : 3, 'x2y2' : 6, 'x3y2' : 1, 'x4y2' : 2, 'x5y2' : 7, 'x6y2' : 4, 'x7y2' : 5, 'x8y2' : 8, 'x9y2' : 9, 'x1y3' : 8, 'x2y3' : 2, 'x3y3' : 9, 'x4y3' : 3, 'x5y3' : 5, 'x6y3' : 6, 'x7y3' : 1, 'x8y3' : 4, 'x9y3' : 7, 'x1y4' : 6, 'x2y4' : 7, 'x3y4' : 3, 'x4y4' : 1, 'x5y4' : 4, 'x6y4' : 5, 'x7y4' : 2, 'x8y4' : 9, 'x9y4' : 8, 'x1y5' : 9, 'x2y5' : 8, 'x3y5' : 2, 'x4y5' : 7, 'x5y5' : 6, 'x6y5' : 3, 'x7y5' : 4, 'x8y5' : 1, 'x9y5' : 5, 'x1y6' : 1, 'x2y6' : 4, 'x3y6' : 5, 'x4y6' : 9, 'x5y6' : 2, 'x6y6' : 8, 'x7y6' : 3, 'x8y6' : 7, 'x9y6' : 6, 'x1y7' : 5, 'x2y7' : 1, 'x3y7' : 7, 'x4y7' : 4, 'x5y7' : 3, 'x6y7' : 9, 'x7y7' : 8, 'x8y7' : 6, 'x9y7' : 2, 'x1y8' : 4, 'x2y8' : 9, 'x3y8' : 6, 'x4y8' : 5, 'x5y8' : 8, 'x6y8' : 2, 'x7y8' : 7, 'x8y8' : 3, 'x9y8' : 1, 'x1y9' : 2, 'x2y9' : 3, 'x3y9' : 8, 'x4y9' : 6, 'x5y9' : 1, 'x6y9' : 7, 'x7y9' : 9, 'x8y9' : 5, 'x9y9' : 4}

def printTable():
    print(u"\u250F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u2513")
    print(u"\u2503", table['x1y1'], u"\u2502", table['x2y1'], u"\u2502", table['x3y1'], u"\u2503", table['x4y1'], u"\u2502", table['x5y1'], u"\u2502", table['x6y1'], u"\u2503", table['x7y1'], u"\u2502", table['x8y1'], u"\u2502", table['x9y1'], u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(u"\u2503", table['x1y2'], u"\u2502", table['x2y2'], u"\u2502", table['x3y2'], u"\u2503", table['x4y2'], u"\u2502", table['x5y2'], u"\u2502", table['x6y2'], u"\u2503", table['x7y2'], u"\u2502", table['x8y2'], u"\u2502", table['x9y2'], u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(u"\u2503", table['x1y3'], u"\u2502", table['x2y3'], u"\u2502", table['x3y3'], u"\u2503", table['x4y3'], u"\u2502", table['x5y3'], u"\u2502", table['x6y3'], u"\u2503", table['x7y3'], u"\u2502", table['x8y3'], u"\u2502", table['x9y3'], u"\u2503")
    print(u"\u2523\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u252B")
    print(u"\u2503", table['x1y4'], u"\u2502", table['x2y4'], u"\u2502", table['x3y4'], u"\u2503", table['x4y4'], u"\u2502", table['x5y4'], u"\u2502", table['x6y4'], u"\u2503", table['x7y4'], u"\u2502", table['x8y4'], u"\u2502", table['x9y4'], u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(u"\u2503", table['x1y5'], u"\u2502", table['x2y5'], u"\u2502", table['x3y5'], u"\u2503", table['x4y5'], u"\u2502", table['x5y5'], u"\u2502", table['x6y5'], u"\u2503", table['x7y5'], u"\u2502", table['x8y5'], u"\u2502", table['x9y5'], u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(u"\u2503", table['x1y6'], u"\u2502", table['x2y6'], u"\u2502", table['x3y6'], u"\u2503", table['x4y6'], u"\u2502", table['x5y6'], u"\u2502", table['x6y6'], u"\u2503", table['x7y6'], u"\u2502", table['x8y6'], u"\u2502", table['x9y6'], u"\u2503")
    print(u"\u2523\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u252B")
    print(u"\u2503", table['x1y7'], u"\u2502", table['x2y7'], u"\u2502", table['x3y7'], u"\u2503", table['x4y7'], u"\u2502", table['x5y7'], u"\u2502", table['x6y7'], u"\u2503", table['x7y7'], u"\u2502", table['x8y7'], u"\u2502", table['x9y7'], u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(u"\u2503", table['x1y8'], u"\u2502", table['x2y8'], u"\u2502", table['x3y8'], u"\u2503", table['x4y8'], u"\u2502", table['x5y8'], u"\u2502", table['x6y8'], u"\u2503", table['x7y8'], u"\u2502", table['x8y8'], u"\u2502", table['x9y8'], u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(u"\u2503", table['x1y9'], u"\u2502", table['x2y9'], u"\u2502", table['x3y9'], u"\u2503", table['x4y9'], u"\u2502", table['x5y9'], u"\u2502", table['x6y9'], u"\u2503", table['x7y9'], u"\u2502", table['x8y9'], u"\u2502", table['x9y9'], u"\u2503")
    print(u"\u2517\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u251B")

table_Coor = []
for i in range(9):
    x = i + 1
    for j in range(9):
        y = j + 1
        xy = [x, y]
        table_Coor.append(xy)

random.shuffle(table_Coor)



def check_num(coord_x, coord_y):
    coord = "x"+str(coord_x)+"y"+str(coord_y)
    insertSuccess = True
    solutions = []
    #number = table[coord]
    row = 1
    while row < 10:
        #os.system('cls||clear')
        #printTable()
        checkCoordinate = 'x'+str(coord_x)+'y'+str(row)
        if checkCoordinate == coord:
            row = 1 + row
            pass
        elif table[coord] == table[checkCoordinate]:
            row = 1 + row
            insertSuccess = False
            solutions.append(insertSuccess)
            pass
        else:
            row = 1 + row
        column = 1
        while column < 10:
            #os.system('cls||clear')
            #printTable()
            checkCoordinate = 'x'+str(column)+'y'+str(coord_y)
            #print(checkCoordinate)
            if checkCoordinate == coord:
                column = 1 + column
                pass
            elif table[coord] == table[checkCoordinate]:
                #table[coordinate] = ' '
                insertSuccess = False
                solutions.append(insertSuccess)
                column = 1 + column
                pass
            else:
                column = 1 + column
    if solutions.count(False) == 10:
        print('True')
        return True
    else:
        print('False')
        return False
    print(solutions)

    if coord[0] <4 and coord[1] < 4:
        check_list = [table['x1y1'], table['x2y1'], table['x3y1'], table['x1y2'], table['x2y2'], table['x3y2'], table['x1y3'], table['x2y3'], table['x3y3']]
        ii = 1
        for ii in range(1, 4):
            jj = 1
            for jj in range(1, 4):
                checkCoordinate = 'x'+str(ii)+'y'+str(jj)
                print(checkCoordinate)
                if number in check_list:
                    
                    if checkCoordinate == coordinate:
                        input('i')
                        pass
                    else:
                        coordinate = True    
                    

                    insertSuccess = False
                else:
                    insertSuccess = True
                   
    return insertSuccess

def check_solvability(coord_x, coord_y):
    coord = "x"+str(coord_x)+"y"+str(coord_y)
    solvability = []
    for i in range(9):
        table[coord] = i+1
        solvability.append(check_num(coord_x, coord_y))
    table[coord] = ' '
    if solvability.count(False) == 9:
        return False
    else:
        return True

#printTable()

def game_generator():
    no_more_to_delete = False
    n = -1
    while not no_more_to_delete:
        n += 1
        coord_x = table_Coor[n][0]
        coord_y = table_Coor[n][1]
        coord = "x"+str(coord_x)+"y"+str(coord_y)
        coord_mirror_x = abs(10 - coord_x)
        coord_mirror_y = abs(10 - coord_y)
        coord_mirror = "x"+str(coord_mirror_x)+"y"+str(coord_mirror_y)
        table[coord] = ' '
        table[coord_mirror] = ' '
        solvability = check_solvability(coord_x, coord_y)
        if not solvability:
            no_more_to_delete = True
        if n == 79:
            break
        #printTable()

game_generator()

printTable()


