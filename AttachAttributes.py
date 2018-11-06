import csv
import random

def populateTable(csvFileName, csvTuples):

    try:
        with open(csvFileName, "w") as csvFile:
            csvWriteFile = csv.writer(csvFile)
            for tuple in csvTuples:
                csvWriteFile.writerow(tuple)
    except FileNotFoundError:
        print("I shouldnt really print but whatver")
        return

def beerAttributes():

    manfList = getManfList()
    if(manfList == None or manfList == []):
        print("Manf list is empty")
        return

    beerList = getBeerCSVList(manfList)
    if(beerList == None or beerList == []):
        print("Beer list is empty")
        return

    beerManfTuples = randomizeBeerManfTuples(beerList, manfList)
    if(beerManfTuples == None or beerManfTuples == []):
        print("BeerManfTuples is empty")
        return

    tableName = "Beer2.csv"

    populateTable(tableName, beerManfTuples)

def randomizeBeerManfTuples(beerList, manfList):

    beerManfTuples = []

    beerCSVAttributes = beerList.pop(0)

    for beerTuple in beerList:
        while True:
            beerManfTuple = beerTuple.copy()
            manufacturer = random.choice(manfList)
            beerManfTuple.append(manufacturer)
            if beerManfTuple not in beerManfTuples:
                beerManfTuples.append(beerManfTuple)
                break

    beerCSVAttributes.append("Manufacturer")
    beerManfTuples.insert(0, beerCSVAttributes)
    return beerManfTuples

def getBeerCSVList(listOfManf):

    currentList = []
    try:
        with open("Beer.csv", "r") as csvFile:
            reader = csv.reader(csvFile)
            currentList = list(reader)
    except FileNotFoundError:
        print("File not Found")
        return None
    
    return currentList

def getManfList():

    listOfManf = []
    try:
        with open("Manufacturers.txt", "r") as manfFile:
            for manfName in manfFile:
                manfString = manfName.strip()
                listOfManf.append(manfString)

    except FileNotFoundError:
        print("File not Found for manufacturers.")
        return None

    return listOfManf

def DrinkerAttributes():
    pass

def BarAttributes():
    pass

def main():
    userInput = -1
    while True:
        try:
            message = "Enter 1 for beer\nEnter 2 for Drinker\nEnter 3 for Bar\nInput: "
            userInput = int(input(message))
            if userInput < 1 or userInput > 3:
                print("Try again\n")
                continue
            else:
                break
        except ValueError:
            print("Try again\n")
            continue
        
    if userInput == 1:
        beerAttributes()
    elif userInput == 2:
        DrinkerAttributes()
    else:
        BarAttributes()

if __name__ == "__main__":
    main()