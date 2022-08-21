from functions import fileIO
from functions import dataProcessing
from functions import logger

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
            print("Invalid Input")
            chooseCivMethod()
    except ValueError:
        print(ValueError)
        chooseCivMethod()

# Define the main function


def main():
    log = logger.createLogFile()
    chooseCiv = chooseCivMethod(log)
    dataProcessing.getPlayers(chooseCiv, log)


# Run the main function

if __name__ == "__main__":
    main()
