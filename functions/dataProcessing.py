

import random
import json

# get user input to select number of civs to generate


def getPlayers(civsList):
    usedValues = []
    playerList = []
    outDict = {}
    numPlayers = int(input("How many players are there?\n"))
    for i in range(numPlayers):
        player = input("Enter the name of each player one at a time.\n")
        playerList.append(player)

    with open("selectedCivs.json", 'w', encoding='utf-8') as outJson:

        for people in range(numPlayers):

            value = random.randint(0, len(civsList))
            if value in usedValues:
                print("Caught a duplicate, new number will be generated")
                newValue = random.randint(0, len(civsList))
                usedValues.append(newValue)
                try:
                    newKey = {playerList[people]: civsList[str(newValue)]}
                    outDict.update(newKey)
                except KeyError:
                    print(KeyError)
            else:
                usedValues.append(value)
                try:
                    newKey = {playerList[people]: civsList[str(value)]}
                    outDict.update(newKey)
                except KeyError:
                    print(KeyError)

        json.dump(outDict, outJson, ensure_ascii=False, indent=4)
        print("selectedCivs.json has been saved.")
