
def PrintFile(filename):
    # file = open(filename, 'r')
    # print (file.read())
    with open(filename, 'r') as file:
        print (file.read())
    return True


scores = []
ScoreDB = open("scoredb.csv", 'w')

while (True):

    for i in range(3):
        score = input(f" Item {i} - Input your score: ")
        scores.append(score)
        ScoreDB.write(score + ',')

    ScoreDB.write('\n')
    print ('Your scores are \n', scores, '!')

    proceed = input("Do you want to add new set? Y/N :")

    if proceed == 'N':
        break

ScoreDB.close()

ScoreDB = open('scoredb.csv', 'a')
ScoreDB.write('100,200,300')
ScoreDB.close()


print ('DONE')

print('=' * 10)
PrintFile('scoredb.csv')
