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

def getCSVList(csvFileName):

    currentList = []
    try:
        with open(csvFileName, "r") as csvFile:
            reader = csv.reader(csvFile)
            currentList = list(reader)
    except FileNotFoundError:
        print("File not Found")
        return None
    
    return currentList

def getListFromFile(txtFileName):

    listFromText = []
    try:
        with open(txtFileName, "r") as txtFile:
            for line in txtFile:
                listFromText.append(line.rstrip())

    except FileNotFoundError:
        print("File not Found for manufacturers.")
        return None

    return listFromText

def randomizeBeerManfTuples(beerList, manfList):

    beerManfTuples = []

    beerAttributes = beerList.pop(0)

    for beerTuple in beerList:
        while True:
            beerManfTuple = beerTuple.copy()
            manufacturer = random.choice(manfList)
            beerManfTuple.append(manufacturer)
            if beerManfTuple not in beerManfTuples:
                beerManfTuples.append(beerManfTuple)
                break

    beerAttributes.append("Manufacturer")
    beerManfTuples.insert(0, beerAttributes)
    return beerManfTuples

def beerAttributes():

    txtFileName = "Manufacturers.txt"
    manfList = getListFromFile(txtFileName)
    if(manfList == None or manfList == []):
        print("Manf list is empty")
        return

    csvFileName = "Beer.csv"
    beerList = getCSVList(csvFileName)
    if(beerList == None or beerList == []):
        print("Beer list is empty")
        return

    beerManfTuples = randomizeBeerManfTuples(beerList, manfList)
    if(beerManfTuples == None or beerManfTuples == []):
        print("BeerManfTuples is empty")
        return

    tableName = "Beer3.csv"

    populateTable(tableName, beerManfTuples)

def randomizeDrinkerTuples(drinkerList, fakeStreetAddresses, phoneNumbersList):

    drinkerTuples = []

    drinkerAttributes = drinkerList.pop(0)

    for drinkerTuple in drinkerList:
        while True:
            newDrinkerTuple = drinkerTuple.copy()
            fakeStreetAddress = random.choice(fakeStreetAddresses)
            phoneNumber = random.choice(phoneNumbersList)
            newDrinkerTuple.append(phoneNumber)
            newDrinkerTuple.append(fakeStreetAddress)
            if(newDrinkerTuple not in drinkerTuples):
                drinkerTuples.append(newDrinkerTuple)
                break

    drinkerAttributes.append("Phone Number")
    drinkerAttributes.append("Address")
    drinkerTuples.insert(0, drinkerAttributes)
    return drinkerTuples

def DrinkerAttributes():

    txtFileName = "phoneNumbers.txt"
    phoneNumbersList = getListFromFile(txtFileName)
    if(phoneNumbersList == None or phoneNumbersList == []):
        print("Phone number list is empty")
        return
    
    txtFileName = "fakeStreetAddresses.txt"
    fakeStreetsList = getListFromFile(txtFileName)
    if(fakeStreetsList == None or fakeStreetsList == []):
        print("Fake streets list is empty")
        return

    csvFileName = "Drinker.csv"
    drinkerList = getCSVList(csvFileName)
    if(drinkerList == None or drinkerList == []):
        print("Drinker list is empty")
        return

    drinkerTuples = randomizeDrinkerTuples(drinkerList, fakeStreetsList, phoneNumbersList)
    if(drinkerTuples == None or drinkerTuples == []):
        print("Drinker tuples is empty")
        return

    tableName = "Drinker3.csv"
    populateTable(tableName, drinkerTuples)

def randomizeBarTuples(barList, phoneNumbersList, fakeStreetAddresses):
    barTuples = []

    barAttributes = barList.pop(0)

    for barTuple in barList:
        while True:
            newBarTuple = barTuple.copy()
            barState = str(newBarTuple[2])
            licenseNumber = str(random.randint(10000, 99999))
            barLicense = barState + licenseNumber
            fakeStreetAddress = random.choice(fakeStreetAddresses)
            phoneNumber = random.choice(phoneNumbersList)
            newBarTuple.append(barLicense)
            newBarTuple.append(phoneNumber)
            newBarTuple.append(fakeStreetAddress)
            if(newBarTuple not in barTuples):
                barTuples.append(newBarTuple)
                break

    barAttributes.append("License")
    barAttributes.append("Phone Number")
    barAttributes.append("Address")
    barTuples.insert(0, barAttributes)
    return barTuples

def BarAttributes():
    
    txtFileName = "phoneNumbers.txt"
    phoneNumbersList = getListFromFile(txtFileName)
    if(phoneNumbersList == None or phoneNumbersList == []):
        print("Phone numbers list is empty")
        return

    txtFileName = "fakeStreetAddresses.txt"
    fakeStreetsList = getListFromFile(txtFileName)
    if(fakeStreetsList == None or fakeStreetsList == []):
        print("Fake streets list is empty")
        return
    
    csvFileName = "Bar.csv"
    barList = getCSVList(csvFileName)
    if(barList == None or barList == []):
        print("Bar list is empty")
        return

    barTuples = randomizeBarTuples(barList, phoneNumbersList, fakeStreetsList)

    tableName = "Bar3.csv"
    populateTable(tableName, barTuples)
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