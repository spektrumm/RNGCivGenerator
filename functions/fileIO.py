
import json

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


def saveCivList(dict):
    with open("data.json", 'w', encoding='utf-8') as f:
        json.dump(dict, f, ensure_ascii=False, indent=4)
        print("data.json has been saved.")

# open an existing civ list json file to use


def openCivList():
    jsonFile = input("Enter the full name of the desired json file: ")
    with open(jsonFile, 'r', encoding='utf-8') as f:
        civsList = json.load(f)
        # print(len(civsList)) debug
        # print(type(civsList)) debug
    return civsList
