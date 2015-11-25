from sikuli import *
import os
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Review_Bill(billName):
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Review_Bill')

    timeText = "For professional services rendered"
    expText = "Total additional charges"
    totalText = "Total amount of this bill"

    billName = Settings.repFolder + "\\" + billName + ".txt"

    if os.path.exists(billName):
    
        billFile = open(billName)
        billLines = billFile.read().splitlines()
        billFile.close()

        for billLine in billLines:
            if billLine.find(timeText) != -1:
                print(billLine)
                billLine = billLine.replace(timeText,"")
                billLine = billLine.replace("$","")                
                print(billLine)

    else:
        logging.debug(" - MISSING: " + billName)
