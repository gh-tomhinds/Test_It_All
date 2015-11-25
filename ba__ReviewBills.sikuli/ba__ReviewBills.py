from sikuli import *
import os
import logging
import csv
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fGet_BillValues(pBillType,pFullBill,pPhrase):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # searches the bill text file for a phrase and returns the value associated with it

    logging.debug('- Get_BillValues: ' + pBillType)

    for billLine in pFullBill:
        if billLine.find(pPhrase) != -1:
            # after finding the line, remove the phrase, $, commas, and trailing spaces
            billLine = billLine.replace(pPhrase,"")
            billLine = billLine.replace("$","")
            billLine = billLine.replace(",","")
            billLine = billLine.strip()            
            return(billLine)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fCompare_Results(pBillName,pValueType,pSavedValue,pBillValue):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug("- Compare_Results: " + pBillName + ": " + pValueType)

    outFile = Settings.BALogFile
    billLog = open(outFile, "a")

    print(pSavedValue)
    print(pBillValue)

    if float(pSavedValue) == float(pBillValue):
        billLog.write(" " + pValueType + " matches.\n")
    else:
        billLog.write(" !!!" + pValueType + " does not match.")
        billLog.write(" Expected: " + pSavedValue + ", ")        
        billLog.write(" Actual: " + pBillValue + "\n")        

    billLog.close()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fReview_BABill(pBillName):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba review bill")
    logging.debug('Review_Bill: ' + pBillName)

    # open the file that contain bill data
    baDataFile = Settings.dataFolder + "\\baData.csv"
    allBills = csv.DictReader(open(baDataFile))

    # pull the values from the csv to compare to the values in the txt

    stopLooking = False

    for oneBill in allBills:
        if stopLooking == False:
            if oneBill["name"] == pBillName:
                savedFeesValue = oneBill["fees"]
                savedCostsValue = oneBill["costs"]
                savedTotalValue = oneBill["total"]
                stopLooking = True

    billPath = Settings.repFolder + "\\" + pBillName + ".txt"

    if os.path.exists(billPath):

        # set up default strings used to identify specific lines on the bill
        if "Progress" in pBillName and "3" in pBillName:
            timeText = "Net Time Charges"
        elif "Progress" in pBillName:
            timeText = "Progress billing amount"
        else:            
            timeText = "For professional services rendered"

        print(timeText)

        expText = "Total additional charges"
        totalText = "Balance due"

        # open txt file of printed bill
        billFile = open(billPath)
        # read in file and break it up into lines
        billLines = billFile.read().splitlines()            
        billFile.close()

        # read values from printed bill
        billFeesValue = fGet_BillValues("Fees",billLines,timeText)
        print("* * *")        
        print(billFeesValue)
        billCostsValue = fGet_BillValues("Costs",billLines,expText)
        billTotalValue = fGet_BillValues("Total",billLines,totalText)

        # open log file
        outFile = Settings.BALogFile
        billLog = open(outFile, "a")
        
        # print results      
        billLog.write("\nBill: " +  pBillName)
        for dashes in range(50-len(pBillName)):
            billLog.write("-")
        billLog.write("\n")
        billLog.close()

        fCompare_Results(pBillName,"Fees",savedFeesValue,billFeesValue)
        fCompare_Results(pBillName,"Costs",savedCostsValue,billCostsValue)
        fCompare_Results(pBillName,"Total",savedTotalValue,billTotalValue)

    else:
        logging.debug(" - MISSING: " + pBillName)

    myTools.sectionEndTimeStamp()