

import random

# get user input to select number of civs to generate


def getPlayers(civsList):
    usedValues = []
    playerList = []
    numPlayers = int(input("How many players are there?\n"))
    for i in range(numPlayers):
        player = input("Enter the name of each player one at a time.\n")
        playerList.append(player)

    for people in range(numPlayers):
        # print(f'this is the length of the dict at line 52 {len(civsList)}') debug

        value = random.randint(0, len(civsList))
        # print(value) debug
        if value in usedValues:
            print("Caught a duplicate, trying again.")
            newValue = random.randint(0, len(civsList))
            usedValues.append(newValue)
            try:
                civ = civsList[str(newValue)]
            except KeyError:
                print(KeyError)
                civ = civsList.get(str(newValue))
            print(f'{playerList[people]} is civ: {civ}')
        else:
            usedValues.append(value)
            # print(value) debug
            try:
                civ = civsList[str(value)]
            except KeyError:
                print(KeyError)
                civ = civsList.get(str(value))
            # print(civ) debug
            print(f'{playerList[people]} is civ: {civ}')
