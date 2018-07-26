import random
import os

tableIsFull = False

table_Coor = []
for i in range(9):
    x = i + 1
    for j in range(9):
        y = j + 1
        xy = [x, y]
        table_Coor.append(xy)

random.shuffle(table_Coor)

# table
table = {
    'x1y1': ' ', 'x2y1': ' ', 'x3y1': ' ', 'x4y1': ' ', 'x5y1': ' ', 'x6y1': ' ', 'x7y1': ' ', 'x8y1': ' ', 'x9y1': ' ',
    'x1y2': ' ', 'x2y2': ' ', 'x3y2': ' ', 'x4y2': ' ', 'x5y2': ' ', 'x6y2': ' ', 'x7y2': ' ', 'x8y2': ' ', 'x9y2': ' ',
    'x1y3': ' ', 'x2y3': ' ', 'x3y3': ' ', 'x4y3': ' ', 'x5y3': ' ', 'x6y3': ' ', 'x7y3': ' ', 'x8y3': ' ', 'x9y3': ' ',
    'x1y4': ' ', 'x2y4': ' ', 'x3y4': ' ', 'x4y4': ' ', 'x5y4': ' ', 'x6y4': ' ', 'x7y4': ' ', 'x8y4': ' ', 'x9y4': ' ',
    'x1y5': ' ', 'x2y5': ' ', 'x3y5': ' ', 'x4y5': ' ', 'x5y5': ' ', 'x6y5': ' ', 'x7y5': ' ', 'x8y5': ' ', 'x9y5': ' ',
    'x1y6': ' ', 'x2y6': ' ', 'x3y6': ' ', 'x4y6': ' ', 'x5y6': ' ', 'x6y6': ' ', 'x7y6': ' ', 'x8y6': ' ', 'x9y6': ' ',
    'x1y7': ' ', 'x2y7': ' ', 'x3y7': ' ', 'x4y7': ' ', 'x5y7': ' ', 'x6y7': ' ', 'x7y7': ' ', 'x8y7': ' ', 'x9y7': ' ',
    'x1y8': ' ', 'x2y8': ' ', 'x3y8': ' ', 'x4y8': ' ', 'x5y8': ' ', 'x6y8': ' ', 'x7y8': ' ', 'x8y8': ' ', 'x9y8': ' ',
    'x1y9': ' ', 'x2y9': ' ', 'x3y9': ' ', 'x4y9': ' ', 'x5y9': ' ', 'x6y9': ' ', 'x7y9': ' ', 'x8y9': ' ', 'x9y9': ' '}

# game 1
'''table['x4y1'] = 7
table['x5y1'] = 3
table['x7y1'] = 8
table['x8y1'] = 9
table['x9y1'] = 1
table['x1y2'] = 2
table['x2y2'] = 8
table['x3y3'] = 7
table['x8y3'] = 2
table['x9y3'] = 5
table['x1y4'] = 1
table['x4y4'] = 8
table['x5y4'] = 5
table['x7y4'] = 4
table['x8y4'] = 3
table['x2y6'] = 9
table['x3y6'] = 3
table['x5y6'] = 1
table['x6y6'] = 6
table['x9y6'] = 7
table['x1y7'] = 9
table['x2y7'] = 6
table['x7y7'] = 2
table['x8y8'] = 5
table['x9y8'] = 3
table['x1y9'] = 8
table['x2y9'] = 3
table['x3y9'] = 2
table['x5y9'] = 9
table['x6y9'] = 4'''

# table test
'''table = {
    'x1y1': 7,
    'x2y1': 5,
    'x3y1': 4,
    'x4y1': 8,
    'x5y1': 9,
    'x6y1': 1,
    'x7y1': 6,
    'x8y1': 2,
    'x9y1': 3,
    'x1y2': 3,
    'x2y2': 6,
    'x3y2': 1,
    'x4y2': 2,
    'x5y2': 7,
    'x6y2': 4,
    'x7y2': 5,
    'x8y2': 8,
    'x9y2': 9,
    'x1y3': 8,
    'x2y3': 2,
    'x3y3': 9,
    'x4y3': 3,
    'x5y3': 5,
    'x6y3': 6,
    'x7y3': 1,
    'x8y3': 4,
    'x9y3': 7,
    'x1y4': 6,
    'x2y4': 7,
    'x3y4': 3,
    'x4y4': 1,
    'x5y4': 4,
    'x6y4': 5,
    'x7y4': 2,
    'x8y4': 9,
    'x9y4': 8,
    'x1y5': 9,
    'x2y5': 8,
    'x3y5': 2,
    'x4y5': 7,
    'x5y5': 6,
    'x6y5': 3,
    'x7y5': 4,
    'x8y5': 1,
    'x9y5': 5,
    'x1y6': 1,
    'x2y6': 4,
    'x3y6': 5,
    'x4y6': 9,
    'x5y6': 2,
    'x6y6': 8,
    'x7y6': 3,
    'x8y6': 7,
    'x9y6': 6,
    'x1y7': 5,
    'x2y7': 1,
    'x3y7': 7,
    'x4y7': 4,
    'x5y7': 3,
    'x6y7': 9,
    'x7y7': 8,
    'x8y7': 6,
    'x9y7': 2,
    'x1y8': 4,
    'x2y8': 9,
    'x3y8': 6,
    'x4y8': 5,
    'x5y8': 8,
    'x6y8': 2,
    'x7y8': 7,
    'x8y8': 3,
    'x9y8': 1,
    'x1y9': 2,
    'x2y9': 3,
    'x3y9': 8,
    'x4y9': 6,
    'x5y9': 1,
    'x6y9': 7,
    'x7y9': 9,
    'x8y9': 5,
    'x9y9': 4}'''

'''table = {
    'x1y1': 1, 'x2y1': 7, 'x3y1': 4, 'x4y1': 6, 'x5y1': 2, 'x6y1': 8, 'x7y1': 5, 'x8y1': 3, 'x9y1': 9,
    'x1y2': 3, 'x2y2': 5, 'x3y2': 9, 'x4y2': 7, 'x5y2': 1, 'x6y2': 4, 'x7y2': 2, 'x8y2': 8, 'x9y2': 6,
    'x1y3': 8, 'x2y3': 2, 'x3y3': 6, 'x4y3': 5, 'x5y3': 3, 'x6y3': 9, 'x7y3': 4, 'x8y3': 7, 'x9y3': 1,
    'x1y4': 4, 'x2y4': 1, 'x3y4': 8, 'x4y4': 3, 'x5y4': 6, 'x6y4': 7, 'x7y4': 9, 'x8y4': 5, 'x9y4': 2,
    'x1y5': 2, 'x2y5': 6, 'x3y5': 7, 'x4y5': 1, 'x5y5': 9, 'x6y5': 5, 'x7y5': 3, 'x8y5': 4, 'x9y5': 8,
    'x1y6': 9, 'x2y6': 3, 'x3y6': 5, 'x4y6': 4, 'x5y6': 8, 'x6y6': 2, 'x7y6': 1, 'x8y6': 6, 'x9y6': 7,
    'x1y7': 5, 'x2y7': 9, 'x3y7': 1, 'x4y7': 8, 'x5y7': 4, 'x6y7': 6, 'x7y7': 7, 'x8y7': 2, 'x9y7': 3,
    'x1y8': 6, 'x2y8': 4, 'x3y8': 3, 'x4y8': 2, 'x5y8': 7, 'x6y8': 1, 'x7y8': 8, 'x8y8': 9, 'x9y8': 5,
    'x1y9': 7, 'x2y9': 8, 'x3y9': 2, 'x4y9': 9, 'x5y9': 5, 'x6y9': 3, 'x7y9': 6, 'x8y9': 1, 'x9y9': 4}
'''


def cell_value_checking(key):
    try:
        int(table[key])
        if table[key] < 9:
            return True
        else:
            return False
    except ValueError:
        table[key] = 0
        return True


def number_checking(key, x_coor, y_coor):
    table[key] += 1
    row = 1
    while row < 10:
        checking_key = 'x' + str(x_coor) + 'y' + str(row)
        if key == checking_key:
            row += 1
        elif table[key] == table[checking_key]:
            return False
        else:
            row += 1
        column = 1
        while column < 10:
            checking_key = 'x' + str(column) + 'y' + str(y_coor)
            if key == checking_key:
                column += 1
            elif table[key] == table[checking_key]:
                return False
            else:
                column += 1
    return block_checking(key, x_coor, y_coor)


def block_checking(key, x_coor, y_coor):
    check_list = []
    if x_coor < 4:
        block_column_multiplier = 0
    elif x_coor < 7:
        block_column_multiplier = 1
    else:
        block_column_multiplier = 2
    if y_coor < 4:
        block_row_multiplier = 0
    elif y_coor < 7:
        block_row_multiplier = 1
    else:
        block_row_multiplier = 2
    y_coor_block = 1 + 3 * block_row_multiplier
    while y_coor_block < 4 + 3 * block_row_multiplier:
        x_coor_block = 1 + 3 * block_column_multiplier
        while x_coor_block < 4 + 3 * block_column_multiplier:
            checking_key = 'x' + str(x_coor_block) + 'y' + str(y_coor_block)
            if checking_key == key:
                x_coor_block += 1
            else:
                check_list.append(table[checking_key])
                x_coor_block += 1
        y_coor_block += 1
    for i in range(8):
        if table[key] == check_list[i]:
            return False
    return True


def table_generator():
    key = ' '
    first_row = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(first_row)
    for x_coor in range(1, 10):
        key = 'x' + str(x_coor) + 'y1'
        table[key] = first_row[x_coor-1]
    n = 0
    while n < 72:
        y_coor = 2
        while y_coor < 10:
            x_coor = 1
            while x_coor < 10:
                key = 'x' + str(x_coor) + 'y' + str(y_coor)
                if cell_value_checking(key):
                    if number_checking(key, x_coor, y_coor):
                        n += 1
                        x_coor += 1
                else:
                    table[key] = ' '
                    if x_coor > 1:
                        x_coor -= 1
                    else:
                        x_coor = 9
                        y_coor -= 1
                    n -= 1
            y_coor += 1
        n += 1


def randomize():
    i = 1
    while i < 1001:
        block_row = random.randint(1, 3)
        block_column = random.randint(1, 3)
        if block_row == 1:
            row = random.randint(2, 3)
            block_row_multiplier = 0
        elif block_row == 2:
            row = random.randint(5, 6)
            block_row_multiplier = 1
        else:
            row = random.randint(8, 9)
            block_row_multiplier = 2

        if block_column == 1:
            column = random.randint(2, 3)
            block_column_multiplier = 0
        elif block_column == 2:
            column = random.randint(5, 6)
            block_column_multiplier = 1
        else:
            column = random.randint(8, 9)
            block_column_multiplier = 2
        row_changing(block_row, block_row_multiplier, row)
        column_changing(block_column, block_column_multiplier, column)
        i += 1


def row_changing(block_row, block_row_multiplier, row):
    reserve_1 = []
    reserve_2 = []
    for x_coor in range(1, 10):
        x_str = str(x_coor)
        y_str = str(block_row + 3 * block_row_multiplier)
        y_str_moving = str(row)
        block_row_key = 'x' + x_str + 'y' + y_str
        moving_key = 'x' + x_str + 'y' + y_str_moving
        reserve_1.append(table[block_row_key])
        reserve_2.append(table[moving_key])

    for x_coor in range(1, 10):
        x_str = str(x_coor)
        y_str = str(block_row + 3 * block_row_multiplier)
        block_row_key = 'x' + x_str + 'y' + y_str
        table[block_row_key] = reserve_2[x_coor-1]
    reserve_2 = []
    for x_coor in range(1, 10):
        x_str = str(x_coor)
        y_str_moving = str(row)
        moving_key = 'x' + x_str + 'y' + y_str_moving
        table[moving_key] = reserve_1[x_coor-1]
    reserve_1 = []


def column_changing(block_column, block_column_multiplier, column):
    reserve_1 = []
    reserve_2 = []
    for y_coor in range(1, 10):
        y_str = str(y_coor)
        x_str = str(block_column + 3 * block_column_multiplier)
        x_str_moving = str(column)
        block_column_key = 'x' + x_str + 'y' + y_str
        moving_key = 'x' + x_str_moving + 'y' + y_str
        reserve_1.append(table[block_column_key])
        reserve_2.append(table[moving_key])

    for y_coor in range(1, 10):
        y_str = str(y_coor)
        x_str = str(block_column + 3 * block_column_multiplier)
        block_column_key = 'x' + x_str + 'y' + y_str
        table[block_column_key] = reserve_2[y_coor-1]

    for y_coor in range(1, 10):
        y_str = str(y_coor)
        x_str_moving = str(column)
        moving_key = 'x' + x_str_moving + 'y' + y_str
        table[moving_key] = reserve_1[y_coor-1]


def check_num(coord_x, coord_y):
    coord = "x" + str(coord_x) + "y" + str(coord_y)
    insertSuccess = True
    solutions = []
    row = 1
    while row < 10:
        checkCoordinate = 'x' + str(coord_x) + 'y' + str(row)
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
            checkCoordinate = 'x' + str(column) + 'y' + str(coord_y)
            if checkCoordinate == coord:
                column = 1 + column
                pass
            elif table[coord] == table[checkCoordinate]:
                insertSuccess = False
                solutions.append(insertSuccess)
                column = 1 + column
                pass
            else:
                column = 1 + column
    if solutions.count(False) == 10:
        return True
    else:
        return False
    return insertSuccess


def check_solvability(coord_x, coord_y):
    coord = "x" + str(coord_x) + "y" + str(coord_y)
    solvability = []
    for i in range(9):
        table[coord] = i + 1
        solvability.append(check_num(coord_x, coord_y))
    table[coord] = ' '
    if solvability.count(False) == 9:
        return False
    else:
        return True


def game_generator():
    no_more_to_delete = False
    n = -1
    while not no_more_to_delete:
        n += 1
        coord_x = table_Coor[n][0]
        coord_y = table_Coor[n][1]
        coord = "x" + str(coord_x) + "y" + str(coord_y)
        coord_mirror_x = abs(10 - coord_x)
        coord_mirror_y = abs(10 - coord_y)
        coord_mirror = "x" + str(coord_mirror_x) + "y" + str(coord_mirror_y)
        table[coord] = ' '
        table[coord_mirror] = ' '
        solvability = check_solvability(coord_x, coord_y)
        if not solvability:
            no_more_to_delete = True
        if n == 79:
            break
        # printTable()


# empty
table_E = {}


def sign_empty():
    for i in table:
        try:
            int(table[i])
            table_E[i] = True
        except BaseException:
            table_E[i] = False


# colour
Color_fix = "\x1B[1;32;40m"
Color_added = "\x1B[0m"

table_C = {}


def coloring():
    for i in table_E:
        if table_E[i] is False:
            table_C[i] = str(table[i])
        else:
            table_C[i] = Color_fix + str(table[i]) + Color_added + ""


# print

def printTable():
    print(u"\u250F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u2533\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u252F\u2501\u2501\u2501\u2513")
    print(
        u"\u2503",
        table_C['x1y1'],
        u"\u2502",
        table_C['x2y1'],
        u"\u2502",
        table_C['x3y1'],
        u"\u2503",
        table_C['x4y1'],
        u"\u2502",
        table_C['x5y1'],
        u"\u2502",
        table_C['x6y1'],
        u"\u2503",
        table_C['x7y1'],
        u"\u2502",
        table_C['x8y1'],
        u"\u2502",
        table_C['x9y1'],
        u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(
        u"\u2503",
        table_C['x1y2'],
        u"\u2502",
        table_C['x2y2'],
        u"\u2502",
        table_C['x3y2'],
        u"\u2503",
        table_C['x4y2'],
        u"\u2502",
        table_C['x5y2'],
        u"\u2502",
        table_C['x6y2'],
        u"\u2503",
        table_C['x7y2'],
        u"\u2502",
        table_C['x8y2'],
        u"\u2502",
        table_C['x9y2'],
        u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(
        u"\u2503",
        table_C['x1y3'],
        u"\u2502",
        table_C['x2y3'],
        u"\u2502",
        table_C['x3y3'],
        u"\u2503",
        table_C['x4y3'],
        u"\u2502",
        table_C['x5y3'],
        u"\u2502",
        table_C['x6y3'],
        u"\u2503",
        table_C['x7y3'],
        u"\u2502",
        table_C['x8y3'],
        u"\u2502",
        table_C['x9y3'],
        u"\u2503")
    print(u"\u2523\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u252B")
    print(
        u"\u2503",
        table_C['x1y4'],
        u"\u2502",
        table_C['x2y4'],
        u"\u2502",
        table_C['x3y4'],
        u"\u2503",
        table_C['x4y4'],
        u"\u2502",
        table_C['x5y4'],
        u"\u2502",
        table_C['x6y4'],
        u"\u2503",
        table_C['x7y4'],
        u"\u2502",
        table_C['x8y4'],
        u"\u2502",
        table_C['x9y4'],
        u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(
        u"\u2503",
        table_C['x1y5'],
        u"\u2502",
        table_C['x2y5'],
        u"\u2502",
        table_C['x3y5'],
        u"\u2503",
        table_C['x4y5'],
        u"\u2502",
        table_C['x5y5'],
        u"\u2502",
        table_C['x6y5'],
        u"\u2503",
        table_C['x7y5'],
        u"\u2502",
        table_C['x8y5'],
        u"\u2502",
        table_C['x9y5'],
        u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(
        u"\u2503",
        table_C['x1y6'],
        u"\u2502",
        table_C['x2y6'],
        u"\u2502",
        table_C['x3y6'],
        u"\u2503",
        table_C['x4y6'],
        u"\u2502",
        table_C['x5y6'],
        u"\u2502",
        table_C['x6y6'],
        u"\u2503",
        table_C['x7y6'],
        u"\u2502",
        table_C['x8y6'],
        u"\u2502",
        table_C['x9y6'],
        u"\u2503")
    print(u"\u2523\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u254B\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u253F\u2501\u2501\u2501\u252B")
    print(
        u"\u2503",
        table_C['x1y7'],
        u"\u2502",
        table_C['x2y7'],
        u"\u2502",
        table_C['x3y7'],
        u"\u2503",
        table_C['x4y7'],
        u"\u2502",
        table_C['x5y7'],
        u"\u2502",
        table_C['x6y7'],
        u"\u2503",
        table_C['x7y7'],
        u"\u2502",
        table_C['x8y7'],
        u"\u2502",
        table_C['x9y7'],
        u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(
        u"\u2503",
        table_C['x1y8'],
        u"\u2502",
        table_C['x2y8'],
        u"\u2502",
        table_C['x3y8'],
        u"\u2503",
        table_C['x4y8'],
        u"\u2502",
        table_C['x5y8'],
        u"\u2502",
        table_C['x6y8'],
        u"\u2503",
        table_C['x7y8'],
        u"\u2502",
        table_C['x8y8'],
        u"\u2502",
        table_C['x9y8'],
        u"\u2503")
    print(u"\u2520\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2542\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u253C\u2500\u2500\u2500\u2528")
    print(
        u"\u2503",
        table_C['x1y9'],
        u"\u2502",
        table_C['x2y9'],
        u"\u2502",
        table_C['x3y9'],
        u"\u2503",
        table_C['x4y9'],
        u"\u2502",
        table_C['x5y9'],
        u"\u2502",
        table_C['x6y9'],
        u"\u2503",
        table_C['x7y9'],
        u"\u2502",
        table_C['x8y9'],
        u"\u2502",
        table_C['x9y9'],
        u"\u2503")
    print(u"\u2517\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u253B\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u2537\u2501\u2501\u2501\u251B")

# user input


def userInput(TrOrFa):
    userInputyOK = False
    userInputxOK = False
    userInputmOK = False
    userInputx = 0
    userInputy = 0
    userInputn = 0
    userInputm = ""
    tableIsFullInput = TrOrFa
    if tableIsFullInput is False:
        while not userInputyOK:
            userInputy_str = input("Which row: ")
            try:
                userInputy = int(userInputy_str)
            except ValueError:
                pass
            if userInputy < 10 and userInputy > 0:
                userInputyOK = True
            else:
                print("please enter a number between 1 and 9")
        userInputxOK = False
        while not userInputxOK:
            userInputx_str = input("Which column: ")
            try:
                userInputx = int(userInputx_str)
            except ValueError:
                pass
            if userInputx < 10 and userInputx > 0:
                userInputxOK = True
            else:
                print("please enter a number between 1 and 9")
        userInputnOK = False
        while not userInputnOK:
            userInputn_str = input("Which number: ")
            try:
                userInputn = int(userInputn_str)
            except ValueError:
                pass
            if userInputn < 10 and userInputn > 0:
                userInputnOK = True
            else:
                print("please enter a number between 1 and 9")
        coordinate = "x" + str(userInputx) + "y" + str(userInputy)
        if table_E[coordinate] is True:
            print("You can't overwrite base numbers")
        else:
            table[coordinate] = userInputn
    else:
        while not userInputmOK:
            userInputm = input("Do you want to modify a cell? y/n ")
            os.system('cls||clear')
            printTable()
            if userInputm == "y":
                userInput(False)
                userInputmOK = True
            elif userInputm == "n":
                userInputmOK = True
                tableIsFullInput = True
                return tableIsFullInput
            else:
                print("please enter y/n")
        tableIsFullInput = False
        return tableIsFullInput
        pass


def checkingIfFull():
    tableIsFull = True
    coordEmptyx = 1
    coordEmptyy = 1
    isEmpty = 0
    isEmptyOK = True
    coordEmpty = "x" + str(coordEmptyx) + "y" + str(coordEmptyy)
    coordEmptyEnd = "x9y9"
    for i in range(9):
        coordEmptyy = 1
        coordEmpty = "x" + str(coordEmptyx) + "y" + str(coordEmptyy)
        try:
            isEmpty = int(table[coordEmpty])
            for j in range(9):
                try:
                    isEmpty = int(table[coordEmpty])
                    if coordEmptyy < 9:
                        coordEmptyy += 1
                        coordEmpty = "x" + \
                            str(coordEmptyx) + "y" + str(coordEmptyy)
                    else:
                        coordEmpty = "x" + \
                            str(coordEmptyx) + "y" + str(coordEmptyy)
                except ValueError:
                    tableIsFull = False
                    return tableIsFull
                    break
            if coordEmptyx < 9:
                coordEmptyx += 1
                coordEmpty = "x" + str(coordEmptyx) + "y" + str(coordEmptyy)
            else:
                coordEmpty = "x" + str(coordEmptyx) + "y" + str(coordEmptyy)
        except ValueError:
            tableIsFull = False
            return tableIsFull
            break
    return tableIsFull


def exitProgram():
    userInputeOK = False
    if not tableIsFull:
        pass
    else:
        while not userInputeOK:
            userInpute = input("Do you want to exit game? ")
            if userInpute == "y":
                tableIsFullExit = True
                return tableIsFullExit
            elif userInpute == "n":
                userInputeOK = True
                tableIsFullExit = False
                return tableIsFullExit
            else:
                print("please enter y/n")


def checking():
    check_list = []
    mistake = 0
    check = True
    # rows
    y = 1
    while y < 10:
        y_str = str(y)
        x = 1
        while x < 10:
            x_str = str(x)
            key = 'x' + x_str + 'y' + y_str
            check_list.append(table[key])
            x += 1

        i = 1
        while i < 10:
            try:
                check == check_list.index(i)
                i += 1
            except BaseException:
                mistake += 1
                i += 1

        check_list = []
        y += 1

    # columns
    x = 1
    while x < 10:
        x_str = str(x)
        y = 1
        while y < 10:
            y_str = str(y)
            key = 'x' + x_str + 'y' + y_str
            check_list.append(table[key])
            y += 1

        i = 1
        while i < 10:
            try:
                check == check_list.index(i)
                i += 1
            except BaseException:
                mistake += 1
                i += 1

        check_list = []
        x += 1

    # 3x3 blocks
    block_row_multiplier = 0
    while block_row_multiplier < 3:

        block_column_multiplier = 0
        while block_column_multiplier < 3:

            y = 1 + (3 * block_row_multiplier)
            while y < 4 + (3 * block_row_multiplier):
                y_str = str(y)
                x = 1 + (3 * block_column_multiplier)
                while x < 4 + (3 * block_column_multiplier):
                    x_str = str(x)
                    key = 'x' + x_str + 'y' + y_str
                    check_list.append(table[key])
                    x += 1

                y += 1
            block_column_multiplier += 1

            i = 1
            while i < 10:
                try:
                    check == check_list.index(i)
                    i += 1
                except BaseException:
                    mistake += 1
                    i += 1

            check_list = []
            y += 1

        block_row_multiplier += 1

    if mistake == 0:
        return print("Your solution is good.")
    else:
        return print('There is (are)', int(mistake / 3),
                     'mistake(s) in the table.')


# actual program
table_generator()
randomize()
game_generator()
sign_empty()
coloring()
printTable()
while not tableIsFull:
    checkingIfFull()
    tableIsFull = checkingIfFull()
    tableIsFull = userInput(tableIsFull)
    os.system('cls||clear')
    coloring()
    printTable()
    if tableIsFull is True:
        checking()
    tableIsFull = exitProgram()
