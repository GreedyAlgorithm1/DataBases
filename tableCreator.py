import webScraper
import sys
import csv
import random

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

        print(listToAppend)
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
        
        if(row in randomizedTuples):
            print("Duplicte random tuple...")
            print(row)
            print()
        else:
            randomizedTuples[tupleCount] = row  
            tupleCount += 1

    return  randomizedTuples  

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
        if attributes == []:
            print("Empty list not valid")
            exit()

    return attributes

def populateTable(tableName, attributes, randomizedTuplesList):
    
    with open(tableName, "w") as file:
        csvfile = csv.writer(file, delimiter=',')
        csvfile.writerow(attributes)
        tupleRow = 0
        for row in randomizedTuplesList:
            csvfile.writerow(row)
            tupleRow += 1

def main():

    tableName = sys.argv[1]

    attributes = getAttributes()

    listOfTuples = getListOfValues(attributes)

    print()
    print(listOfTuples)

    randomizedTuplesList = randomizeTuples(listOfTuples)

    populateTable(tableName, attributes, randomizedTuplesList)

    print(randomizedTuplesList)

    # Create .csv file with attributes at top
    # Populate the columns with corresponding names/elements

if __name__ == "__main__":
    main()