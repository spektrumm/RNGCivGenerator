# RNG Civ Generator
# Author: Nathan "spekky" Hare
# Date: 08/21/2022
# Description: A random number generator that will select Civs at random and assign them to players.

from functions import fileIO
from functions import dataProcessing
from functions import logger
import logging

# Select the method in which the program will acquire the data needed


def chooseCivMethod(logName):
    try:
        method = int(input(
            "How would you like to load your list of civs? (type an integer)\n 1. Process a txt list\n 2. Open an existing json file\n "))
        if method == 1:
            saveDict = fileIO.processCivList()
            fileIO.saveCivList(saveDict, logName)
            return saveDict
        elif method == 2:
            civDict = fileIO.openCivList(logName)
            return civDict
        else:
            logger.printMsg("Invalid input.\nTry again.")
            chooseCivMethod()
    except ValueError:
        logger.logMsg(logging.exception("ValueError"), logName)
        logger.printMsg("ValueError.\nTry again.")
        chooseCivMethod()

# Define the main function


def main():
    log = logger.createLogFile()
    chooseCiv = chooseCivMethod(log)
    dataProcessing.getPlayers(chooseCiv, log)


# Run the main function

if __name__ == "__main__":
    main()
