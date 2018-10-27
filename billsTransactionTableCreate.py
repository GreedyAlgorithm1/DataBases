import tableCreator
import random
import sys
import csv

def populateTable(tableName, tuplesList, amountPerDrinker):

    if(tableName == "Bills.csv"):
        attributes = ["BillId", "BarId", "DrinkerId", "TimeIssued", "Item", "Quantity", "Price"]
    else:
        attributes = ["tid", "BarId", "DrinkerId", "SubTotal", "Tax", "Tip", "Total"]

    if(amountPerDrinker != None):
        with open(tableName, "w") as file:
            csvfile = csv.writer(file, delimiter=',')
            csvfile.writerow(attributes)
            billID = 1
            relationsTupleIndex = 0
            for orderAmount in amountPerDrinker:
                ordersPrinted = 0

                while ordersPrinted < orderAmount:
                    tuplesList[relationsTupleIndex].insert(0, billID)
                    csvfile.writerow(tuplesList[relationsTupleIndex])
                    relationsTupleIndex += 1
                    ordersPrinted += 1
                
                billID += 1
    else:
        with open(tableName, "w") as file:
            csvFile = csv.writer(file, delimiter=',')
            csvFile.writerow(attributes)
            transactionID = 1
            for row in tuplesList:
                row.insert(0, transactionID)
                csvFile.writerow(row)
                transactionID += 1


def getRandomTuplesCount():
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

    return randomTuplesCount


def getBillsLists():
    numOfFiles = 4
    fileCount = 0
    orderOfFilesToEnter = ["Bar.csv", "Drinker.csv", "SellsItems.csv", "SellsBeers.csv"]
    listOfLists = []
    while fileCount < numOfFiles:
        
        csvFileName = orderOfFilesToEnter[fileCount]

        try:
            with open(csvFileName, "r") as csvFile:
                reader = csv.reader(csvFile)
                currentList = list(reader)
                currentList.pop(0)
                listOfLists.append(currentList)
        except FileNotFoundError:
            print("File '{}' not found!".format(csvFileName))
            break

        fileCount += 1

    return listOfLists

def getBarSellsList(barID, barsSellingList):

    barSellsList = []

    for sellTuple in barsSellingList:
        if(sellTuple[0] == barID):
            barSellsList.append(sellTuple)

    return barSellsList


def randomizeBillsList(barsList, drinkersList, sellsItemList, sellsBeerList):

    randomTuplesCount = getRandomTuplesCount()
    randomizedTupleList = []
    amountPerDrinker = []

    tupleCount = 1

    while tupleCount < randomTuplesCount:

        drinkerOrderTuple = []

        pickedBarTuple = random.choice(barsList)
        pickedDrinkerTuple = random.choice(drinkersList)
        barID = pickedBarTuple[0]
        drinkerID = pickedDrinkerTuple[0]

        barSellsItemList = getBarSellsList(barID, sellsItemList)
        barSellsBeerList = getBarSellsList(barID, sellsBeerList)

        openTime = int(pickedBarTuple[3])
        closeTime = int(pickedBarTuple[4])

        timeBilled = random.randint(830, 2230)

        while timeBilled < openTime or timeBilled > closeTime:
            #print("Open time: {}".format(openTime))
            #print("Close Time: {}".format(closeTime))
            timeBilled = random.randint(830, 2230)
            #print("Selected time: {}".format(timeBilled))

        dupeItemCheck = []

        amountBarSells = len(barSellsBeerList) + len(barSellsItemList)
        randomOrderAmount = random.randint(1, 5)

        #while(tupleCount + randomOrderAmount > randomTuplesCount):
        #    randomOrderAmount = random.randint(1, 5)

        validTuples = 0

        drinkerOrderTuple.append(barID)
        drinkerOrderTuple.append(drinkerID)
        drinkerOrderTuple.append(timeBilled)


        if(amountBarSells < randomOrderAmount):
            amountGotten = amountBarSells
        else:
            amountGotten = randomOrderAmount

        while validTuples < amountGotten:

            #print("Valid tuple: {}".format(validTuples))
            #print("Amount gotten {}".format(amountGotten))

            foodOrBeer = random.randint(1,2)
            if(foodOrBeer == 1):
                # THIS ERROR IndexError: Cannot choose from an empty sequence
                if(barSellsItemList != []):
                    pickedItemTuple = random.choice(barSellsItemList)
                else:
                    pickedItemTuple = random.choice(barSellsBeerList)
            else:
                if(barSellsBeerList != []):
                    pickedItemTuple = random.choice(barSellsBeerList)
                else:
                    pickedItemTuple = random.choice(barSellsItemList)

            item = pickedItemTuple[2]
            itemPrice = pickedItemTuple[3]

            if(item in dupeItemCheck):
                continue
            
            dupeItemCheck.append(item)

            randomQuantity = random.randint(1, 3)

            totalPrice = round(float(randomQuantity) * float(itemPrice), 2)

            drinkerOrderTuple.append(item)
            drinkerOrderTuple.append(randomQuantity)
            drinkerOrderTuple.append(totalPrice)

            completeOrderList = drinkerOrderTuple.copy()

            randomizedTupleList.append(completeOrderList)

            drinkerOrderTuple.remove(item)
            drinkerOrderTuple.remove(randomQuantity)
            drinkerOrderTuple.remove(totalPrice)
            validTuples += 1

        amountPerDrinker.append(amountGotten)
        tupleCount += amountGotten

    randomizedTupleList.append(amountPerDrinker)
    return randomizedTupleList

def createBillsTable(tableName):

    billsLists = getBillsLists()
    if(len(billsLists) < 4):
        print("List not long enough to continue")
        return

    sellsBeerList = billsLists.pop()
    sellsItemList = billsLists.pop()
    drinkersList = billsLists.pop()
    barsList = billsLists.pop()

    randomizedTupleList = randomizeBillsList(barsList, drinkersList, sellsItemList, sellsBeerList)
    amounterPerDrinker = randomizedTupleList.pop()

    populateTable(tableName, randomizedTupleList, amounterPerDrinker)

def extractBillsCSVTuples():
    csvFileName = "Bills.csv"
    billsTuplesList = []

    try:
        with open(csvFileName, "r") as csvFile:
            reader = csv.reader(csvFile)
            currentList = list(reader)
            currentList.pop(0)
            billsTuplesList.append(currentList)
    except FileNotFoundError:
        print("File '{}' not found!".format(csvFileName))
        return None
    
    return billsTuplesList

def getTransactionsFromBills(billsTuplesLists):

    amountOfBills = len(billsTuplesLists)
    billIndex = 0
    tipRate = 0.2
    taxRate = 0.07

    transactionTuples = []

    while billIndex < amountOfBills:
        subtotal = 0
        if(billIndex + 1 != amountOfBills):
           while billsTuplesLists[billIndex][0] == billsTuplesLists[billIndex + 1][0]:
               billOrderTuple = billsTuplesLists[billIndex]
               subtotal += float(billOrderTuple[6])
               billIndex += 1
        
        billOrderTuple = billsTuplesLists[billIndex]
        barID = billOrderTuple[1]
        drinkeriD = billOrderTuple[2]
        subtotal = float(billOrderTuple[6])
        round(subtotal, 2)
        tax = round(float(subtotal) * float(taxRate), 2)
        tip = round(float(subtotal) * float(tipRate), 2)
        total = round(subtotal + tax + tip, 2)
        transactionTuples.append([barID, drinkeriD, subtotal, tax, tip, total])
        billIndex += 1

    return transactionTuples


def createTransactionsTable(tableName):
    
    billsTuplesLists2 = extractBillsCSVTuples()
    billsTuplesLists = billsTuplesLists2.pop()

    if(billsTuplesLists == None):
        print("No element ins Bills List")
        return

    transactionTuples = getTransactionsFromBills(billsTuplesLists)    
    populateTable(tableName, transactionTuples, None)

def main():
    
    tableName = sys.argv[1]

    if(tableName == "Bills.csv"):
        createBillsTable(tableName)
        return
    if(tableName == "Transactions.csv"):
        createTransactionsTable(tableName)
        return
    
    print("Wrong table name")

if __name__ == "__main__":
    main()