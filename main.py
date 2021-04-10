
# Connect4 Program

Board = [['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-']]

colCtr = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}


def DisplayBoard():
    for item in Board:
        print (item)
    return (True)


# def UpdateCell(tblrow, cellid, value):
#     tblrow[cellid] = value
#     return(tblrow)


DisplayBoard()

while (True):
    #Row = int(input("Enter row: "))
    Col = int(input("Enter col: "))
    Symbol = input("Enter symbol: ")

    if Symbol == 'Z':
        break

    # print (f'Row {Row} and Col {Col}') #Debugging
    # cell = Board[Row]
    # cell[Col] = Symbol

    Level = colCtr[Col]
    Row = Board[5 - Level]
    Row[Col] = Symbol

    Level += 1
    colCtr[Col] = Level

    print (colCtr)

    #Board[Row] = UpdateCell(Board[Row], Col, Symbol)

    DisplayBoard()
