import webScraper
import sys
import csv
import random

# Get attributes from user
def getAttributes():

    attributes = []
    inputAttribute = None

    print()
    print("-----Input attributes of file-----")
    print("Type 'DONE' when finished")
    print("Type 'RESET' to start over")
    print("Type '-rm <attribute>' to remove an attribute")
    print("Type 'EXIT' to kill program")
    print()

    while True:
        
        message = "Input Attribute: "
        inputAttribute = input(message).rstrip()
        inputAttribute = inputAttribute.strip()

        # Check if we have more than one string
        if(len(inputAttribute.split()) >= 2):
            checkFlag = inputAttribute.split()[0]
            
            deleteAttribute = inputAttribute.split()[1]
            if(checkFlag == "-rm"):
                if(deleteAttribute in attributes):
                    attributes.remove(deleteAttribute)
                    print("Attribute removed!")
                    print(attributes)
                    continue
                else:
                    print("Attribute not in list!")
                    continue
       
        # Done inputting attributes
        if(inputAttribute == "DONE"):
            break
        
        # Just to start over
        if(inputAttribute == "RESET"):
            attributes = []
            print("Atributes cleared!")
            continue

        # Just to safely kill program
        if(inputAttribute == "EXIT"):
            exit()

        attributes.append(inputAttribute)

        print(attributes)

        # Just so we dont crash later on (can be removed if we want to)
        if (attributes == []):
            print("Empty list not valid")
            exit()

    return attributes

def getListOfValues(attributes):

    listOfTuples = list(range(len(attributes)))
    maxAttributes = len(attributes)
    attributeIndex = 0

    # Create list of lists of all values according to column attributes
    while attributeIndex < maxAttributes:
        
        # Take in files for each column
        inputMessage = "Enter file name of values for attribute: '{}'\n".format(attributes[attributeIndex])
        fileToExtract = input(inputMessage) 
        listToAppend = []

        # Ask how many values we should extract (Can be omitted)
        while True:
            try:
                message = "Enter how many values to enter: "
                limit = int(input(message), 10)
                if(limit <= 0):
                    print("Please enter a positive integer")
                    continue
                print(limit)
                break
            except KeyboardInterrupt as exception:
                print(exception)
                break
            except ValueError as exception:
                print("Please enter a valid integer")
                print(exception)
                continue
        
        # Attempt to open file and extract contexts
        try:
            with open(fileToExtract, "r") as valuesFile:
                limitCount = 0
                for line in valuesFile:
                    limitCount += 1
                    listToAppend.append(line.rstrip())
                    if(limitCount == limit):
                        break
        except FileNotFoundError as exception:
            print("File does not exist!")
            print("Try another")
            print(exception)
            continue

        #print(listToAppend)
        listOfTuples[attributeIndex] = listToAppend
        attributeIndex += 1

    return listOfTuples

# Function that produces random tuples of indicated amount
def randomizeTuples(listOfTuples):

    elementsCount = len(listOfTuples)

    # Get input on how many random tuples to make
    while True:
        try:
            message = "Enter how many random tuples to make: "
            randomTuplesCount = int(input(message), 10)
            if(randomTuplesCount <= 2):
                print("At least more than 2 tuples")
                continue
            else:
                break
        except ValueError as exception:
            print("Please enter a valid integer")
            print(exception)

    randomizedTuples = list(range(randomTuplesCount))

    tupleCount = 0

    # Create random (distinct) tuples and insert them into final list
    while tupleCount < randomTuplesCount:
        row = []
        for attributeCount in range(elementsCount):
            row.append(random.choice(listOfTuples[attributeCount]))
        
        # Avoid duplicate (redundant) data
        if(row not in randomizedTuples):
            randomizedTuples[tupleCount] = row  
            tupleCount += 1

    return  randomizedTuples  

def randomizeRelationTuples(relationShipTuples):

    # Get input on how many random tuples to make
    while True:
        try:
            message = "Enter how many random tuples to make: "
            randomTuplesCount = int(input(message), 10)
            if(randomTuplesCount <= 2):
                print("At least more than 2 tuples")
                continue
            else:
                break
        except ValueError as exception:
            print("Please enter a valid integer")
            print(exception)

    tupleCount = 0

    randomizedRelationTuples = []

    while tupleCount < randomTuplesCount:
        row = []
        for keysCount in range(len(relationShipTuples)):
            row.append(random.choice(relationShipTuples[keysCount]))

        #print("Before flatten")
        #print(row)
        #print()
        #print("After flatten")
        flattenRow = [item for sublist in row for item in sublist]
        #print(flattenRow)

        if(flattenRow not in randomizedRelationTuples):
            randomizedRelationTuples.append(flattenRow)
            tupleCount += 1

    return randomizedRelationTuples

def randomizeFrequentsTuples(relationShipTuples):
    
    # Get input on how many random tuples to make
    while True:
        try:
            message = "Enter how many random tuples to make: "
            randomTuplesCount = int(input(message), 10)
            if(randomTuplesCount <= 2):
                print("At least more than 2 tuples")
                continue
            else:
                break
        except ValueError as exception:
            print("Please enter a valid integer")
            print(exception)

    tupleCount = 0

    randomizedRelationTuples = []

    # Check logic for states

    while tupleCount < randomTuplesCount:
        row = []
        for keysCount in range(len(relationShipTuples)):
            row.append(random.choice(relationShipTuples[keysCount]))

        #print("Before flatten")
        #print(row)
        #print()
        #print("After flatten")
        flattenRow = [item for sublist in row for item in sublist]
        #print(flattenRow)

        if(flattenRow[2] != flattenRow[4]):
            #print("{} != {}".format(flattenRow[2], flattenRow[4]))
            continue

        if(flattenRow not in randomizedRelationTuples):
            flattenRow.pop(4)
            randomizedRelationTuples.append(flattenRow)
            tupleCount += 1

    return randomizedRelationTuples

def randomizeSellsTuples(relationShipTuples):
     # Get input on how many random tuples to make
    while True:
        try:
            message = "Enter how many random tuples to make: "
            randomTuplesCount = int(input(message), 10)
            if(randomTuplesCount <= 2):
                print("At least more than 2 tuples")
                continue
            else:
                break
        except ValueError as exception:
            print("Please enter a valid integer")
            print(exception)


    # Dictionary of beers at a certain price
    beerPricesDict = {2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : [], 10 : [], 11 : [], 12 : []}
    for beer in relationShipTuples[1]:
        if(beer not in beerPricesDict.values()):
            randomPrice = random.randint(2, 12)
            print("Appended!")
            beerPricesDict[randomPrice].append(beer)
        else:
            print("This means that beer is already included which shouldnt really be the case")

    print(beerPricesDict)

    tupleCount = 0

    randomizedRelationTuples = []
    barSellsBeer = []

    # Check logic for item/beer prices
    while tupleCount < randomTuplesCount:
        row = []
        for keysCount in range(len(relationShipTuples)):
            row.append(random.choice(relationShipTuples[keysCount]))

        #print("Before flatten")
        #print(row)
        #print()
        #print("After flatten")
        flattenRow = [item for sublist in row for item in sublist]
        #print(flattenRow)

        if(flattenRow not in barSellsBeer):
            beerToAdd = flattenRow[2]

            for iterator in range(2, 12):
                listOfBeer = [item for sublist in beerPricesDict[iterator] for item in sublist]
                if(beerToAdd in listOfBeer):
                    priceSold = random.uniform(iterator, iterator + 1)
                    priceSold = round(priceSold, 2)
                    break
            barSellsBeer.append(flattenRow)
            flattenRow.append(priceSold)
            randomizedRelationTuples.append(flattenRow)
            tupleCount += 1

    return randomizedRelationTuples
                    
def populateTable(tableName, attributes, randomizedTuplesList):
    
    with open(tableName, "w") as file:
        csvfile = csv.writer(file, delimiter=',')
        attributes.insert(0, "Id")
        csvfile.writerow(attributes)
        idIndex = 0
        idNum = 1
        for row in randomizedTuplesList:
            randomizedTuplesList[idIndex].insert(0, idNum)
            csvfile.writerow(row)
            idNum += 1
            idIndex += 1

def populateRelationTable(tableName, attributes, randomizedTuplesList):
    
    with open(tableName, "w") as file:
        csvfile = csv.writer(file, delimiter=',')
        csvfile.writerow(attributes)
        idIndex = 0
        for row in randomizedTuplesList:
            randomizedTuplesList[idIndex]
            csvfile.writerow(row)
            idIndex += 1

def extractCSVTuples():

    while True:
        message = "How many tables to read from: "
        numTables = int(input(message))

        if(numTables < 2):
            print("Must be 2 or more tables to read")
            continue
        else:
            break

    relationShipTuple = []
    attributeTuples = []
    counter = 0
    while counter < numTables:
        counter += 1
        message = "Enter csv file to read keys from: "

        csvFileName = input(message).rstrip()

        if(csvFileName == "DONE"):
            break

        currentFileTuple = []
        try:
            with open(csvFileName, "r") as csvFile:
                reader = csv.DictReader(csvFile)
                data = {}

                for row in reader:
                    for header, value in row.items():
                        data.setdefault(header, list()).append(value)

                fileTuple = []
                while True:
                    message = "Enter key to include to relation table (Enter 'DONE' when done): "
                    attribute = input(message)
                    if(attribute == "DONE"):
                        break
                    try:
                        if (fileTuple == []):
                            dataList = data[attribute]
                            for element in range(len(dataList)):
                                fileTuple.append([dataList[element]])
                        else:
                            tempList = data[attribute]
                            for element in range(len(fileTuple)):
                                fileTuple[element].append(tempList[element])
                        attributeTuples.append(attribute)
                    except KeyError:
                        counter -=1
                        print("No attribute found with: '{}'".format(attribute))
                    
                    currentFileTuple = fileTuple

                relationShipTuple.append(currentFileTuple)
        except FileNotFoundError:
            counter -= 1
            print("File not found")

    relationShipTuple.append(attributeTuples)
    return relationShipTuple

def createRelationTable(tableName):

    if (tableName == "SellsBeers.csv") or tableName == "--testFile.csv":
        print("Must create table with beer price logic.")
        relationShipTuples = extractCSVTuples()

        relationAttributes = relationShipTuples.pop()
        relationAttributes.append("Price")
        relationAttributes[1] = "BarName"
        print(relationAttributes)
        print (relationShipTuples)

        randomizedRelationShipTuples = randomizeSellsTuples(relationShipTuples)    

        populateRelationTable(tableName, relationAttributes, randomizedRelationShipTuples)    
        return
    elif (tableName == "Frequents.csv" or tableName == "--testFile.csv"):
        #print("Must create table with frequents logic")
        relationShipTuples = extractCSVTuples()

        relationAttributes = relationShipTuples.pop()
        # This is so that the Drinker's state show up as an attribute name
        checkStates = relationAttributes.pop(4)
        #print(relationAttributes)
        #print(checkStates)
        #print(relationAttributes)
        #print (relationShipTuples)
        randomizedRelationShipTuples = randomizeFrequentsTuples(relationShipTuples)
        #print()
        #print(randomizedRelationShipTuples)

        populateRelationTable(tableName, relationAttributes, randomizedRelationShipTuples)
        return
    elif (tableName == "Make Transaction" or tableName == "--testFile.csv"):
        print("Must create relation table with hours & price logic.")
        return

    relationShipTuples = extractCSVTuples()

    relationAttributes = relationShipTuples.pop()
    #print(relationAttributes)
    #print (relationShipTuples)
    randomizedRelationShipTuples = randomizeRelationTuples(relationShipTuples)
    #print()
    #print(randomizedRelationShipTuples)

    populateRelationTable(tableName, relationAttributes, randomizedRelationShipTuples)

    

def main():

    tableName = sys.argv[1]

    message = "Creating a relation table? (y/n) "
    response = input(message).rstrip()
    
    if(response == "y" or response == "yes"):  
        createRelationTable(tableName)
        return

    attributes = getAttributes()

    listOfTuples = getListOfValues(attributes)

    # print()
    # print(listOfTuples)

    randomizedTuplesList = randomizeTuples(listOfTuples)

    populateTable(tableName, attributes, randomizedTuplesList)

    # print(randomizedTuplesList)

if __name__ == "__main__":
    main()