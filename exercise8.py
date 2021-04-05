

# Artist = "Dave Brubeck"
# Genre = "Jazz"
# DurationInSeconds = 328
# Year = "1994"

# print(Artist)
# print(Genre)
# print(DurationInSeconds)
# print(Year)


# Artist = "Side A"
# Genre = "Pop"
# DurationInSeconds = 60
# Year = "1994"

# print(Artist)
# print(Genre)
# print(DurationInSeconds)
# print(Year)

# Artist = "Gary V"
# Genre = "Christian"
# DurationInSeconds = 100
# Year = "1980"

# print(Artist)
# print(Genre)
# print(DurationInSeconds)
# print(Year)

# Artist = "Martin Nivera"
# Genre = "Ballad"
# DurationInSeconds = 200
# Year = "1990"

# print(Artist)
# print(Genre)
# print(DurationInSeconds)
# print(Year)

# Exercise6

# Blackshoes = {42: 2, 41: 3, 40: 4, 39: 1, 38: 0}
# print (Blackshoes)
# while (True):
#     purchaseSize = int(input("Which shoe size do you want to buy?\n"))
#     if purchaseSize < 0:
#         break
#     if Blackshoes[purchaseSize] > 0:
#         Blackshoes[purchaseSize] -= 1
#     else:
#         print ("Shoes are no longer in stock")
#         break
#     print (Blackshoes)

# favoriteSongs = {1: {'Title': 'Chances Are', 'Artist': 'Side A', 'Genre': 'Ballad', 'Duration': 328, 'Year': '1987'}, 2: {'Title': 'Salamat', 'Artist': 'The Dawn', 'Genre': 'Rock', 'Duration': 300, 'Year': '1980'}}

# # for SongID in favoriteSongs:
#     print (f'Song {SongID} is {favoriteSongs[SongID]} ')
#     Song = favoriteSongs[SongID]
#     for Attribute in Song:
#         print (Attribute, Song[Attribute])

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

# OutputScoreDB = open('scoredb.csv', 'r')
# print (OutputScoreDB.read())
# OutputScoreDB.close()
