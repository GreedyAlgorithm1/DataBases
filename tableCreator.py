import webScraper
import sys

def createTable(tableName, attributes):
    #TODO
    # Get all lists needed to populate the table (how?)
    # Create .csv file with attributes at top
    # Populate the columns with corresponding names/elements
    pass


def main():

    tableName = sys.argv[1]

    attributes = []
    inputAttribute = None

    print()
    print("-----Input attributes of file-----")
    print("Type 'DONE' when finished")
    print("Type 'RESET' to start over")
    print("Type 'EXIT' to kill program")
    print()

    while True:

        inputAttribute = input("Input Attribute: ")
       
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

    print(tableName)
    print(attributes)

if __name__ == "__main__":
    main()