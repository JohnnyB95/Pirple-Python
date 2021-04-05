

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

favoriteSong = {'Title': 'Chances Are', 'Artist': 'Side A', 'Genre': 'Ballad', 'Duration': 328, 'Year': '1987'}

# print (favoriteSong)
# print (favoriteSong['Title'])
# print (favoriteSong['Artist'])
# print (favoriteSong['Genre'])
# print (favoriteSong['Title'])
# print (favoriteSong['Duration'])
# print (favoriteSong['Year'])

for attribute in favoriteSong:
    print (attribute, favoriteSong[attribute])
