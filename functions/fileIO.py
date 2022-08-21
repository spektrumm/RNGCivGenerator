# Boiler plate to deal with file processing and fileIO.


import json
from functions import logger
import logging

# process a text file and create a list of civs


def processCivList():
    civsList = {}
    n = 1
    txtFile = input("Enter the full name of the desired text file: ")
    with open(txtFile, 'r') as civListIn:
        for civs in civListIn:

            line = civListIn.readline()
            outLine = line.strip("\n")
            tempDict = {n: outLine}
            civsList.update(tempDict)
            n += 1
    return civsList

# write the civs list to a json file


def saveCivList(dict, logName):
    with open("data.json", 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)
        success = "data.json has been saved."
        logger.logMsg(success, logName)
        logger.printMsg(success)

# open an existing civ list json file to use


def openCivList(logName):
    civsList = {}
    jsonFile = input("Enter the full name of the desired json file: ")
    try:
        with open(jsonFile, 'r', encoding='utf-8') as f:
            civsList = json.load(f)
        return civsList
    except FileNotFoundError:
        logger.logMsg(logging.exception("FileNotFoundError"), logName)
        logger.printMsg("FileNotFoundError.\nTry a different file name")
        openCivList(logName)
