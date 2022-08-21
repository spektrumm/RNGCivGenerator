# Process the user input gathered, and produce an output file.

import random
import json
import logging
from functions import logger

# get user input to select number of civs to generate


def getPlayers(civsList, logName):
    usedValues = []
    playerList = []
    outDict = {}
    try:
        numPlayers = int(input("How many players are there?\n"))
    except ValueError:
        logger.logMsg(logging.exception("ValueError"), logName)
        getPlayers(civsList, logName)

    for players in range(numPlayers):
        playerName = input("Enter the name of each player one at a time.\n")
        playerList.append(playerName)

    with open("selectedCivs.json", 'w', encoding='utf-8') as outJson:

        for people in range(numPlayers):

            value = random.randint(1, len(civsList))
            logger.logMsg(
                f'Length of civsList for index {people}: {len(civsList)}', logName)
            if value in usedValues:
                duplicateValMsg = f'{value} is a duplicate value.  Selecting a new value.'
                logger.logMsg(duplicateValMsg, logName)
                logger.printMsg(duplicateValMsg)
                newValue = random.randint(1, len(civsList))
                usedValues.append(newValue)
                try:
                    newKey = {playerList[people]: civsList[str(newValue)]}
                    outDict.update(newKey)
                except KeyError:
                    logger.logMsg(logging.exception("KeyError"), logName)
                    logger.printMsg("KeyError, trying new value")

                    # try to generate a new value, despite the KeyError
                    exceptVal = random.randint(1, len(civsList))
                    exceptKey = {playerList[people]: civsList[str(exceptVal)]}
                    outDict.update(exceptKey)
            else:
                usedValues.append(value)
                try:
                    newKey = {playerList[people]: civsList[str(value)]}
                    outDict.update(newKey)
                except KeyError:
                    logger.logMsg(logging.exception("KeyError"), logName)
                    logger.printMsg("KeyError, trying new value")

                    # try to generate a new value, despite the KeyError
                    exceptVal = random.randint(1, len(civsList))
                    exceptKey = {playerList[people]: civsList[str(exceptVal)]}
                    outDict.update(exceptKey)
        if outDict != {}:
            json.dump(outDict, outJson, ensure_ascii=False, indent=4)
            success = "selectedCivs.json has been saved."
            logger.logMsg(success, logName)
            logger.printMsg(success)
        else:
            fail = "output dictionary is empty, no final selection has been generated.\n Check the log file."
            logger.logMsg(fail, logName)
            logger.printMsg(fail)
