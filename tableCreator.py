import webScraper
import sys

def createTable(tableName, attributes):
    #TODO
    # Get all lists needed to populate the table (how?)
    # Create .csv file with attributes at top
    # Populate the columns with corresponding names/elements

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
                limit = int(input("Enter how many values to enter: "), 10)
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
        print()
        print()
        print()
        listOfTuples[attributeIndex] = listToAppend
        print(listOfTuples)
        attributeIndex += 1

            


def main():

    tableName = sys.argv[1]

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

        inputAttribute = input("Input Attribute: ")

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

    print(tableName)
    print(attributes)

    createTable(tableName, attributes)

if __name__ == "__main__":
    main()