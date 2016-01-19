from sikuli import *
import logging
import myTools
import names_Init

#---------------------------------------------------#
def fCreate_OneFinanceCharge(pClient,pCliNum,pMonth,pAmount):
#---------------------------------------------------#

    logging.debug('- Create_OneFinance: ' + str(pMonth) + "-" + pClient + " = " + str(pAmount))
    time.sleep(1)

    # choose client
    type(pClient)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    # switch page
    if Settings.tsVersion > "2014":
        myTools.pressF6(7)
    else:
        myTools.pressF6(4)
    time.sleep(1)

    # go to field
    if Settings.tsVersion > "2014":
        myTools.pressSHIFTTAB(4)
    else:    
        myTools.pressSHIFTTAB(3)
    time.sleep(1)

    # set "next bill"
    type("ne")
    time.sleep(1)
    
    myTools.pressTAB(1)
    time.sleep(1)

    # enter finance charge   
    type(pAmount)
    time.sleep(1)
    myTools.pressTAB(1)

    # description
    type("a",KeyModifier.CTRL)
    financeText = "Finance charge for: " + pClient + ": Month: " + str(pMonth)
    time.sleep(1)
    type(financeText)
    time.sleep(1)

    # save
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    # close client info
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 

#---------------------------------------------------#
def fCreate_FinanceCharges(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("finance" + str(pMonth))
    logging.debug('Create_FinanceCharges: ' + str(pMonth))

    allClients = names_Init.fInit_Clients()
    count = 0

    myTools.getFocus()

    # client list
    type("i",KeyModifier.CTRL)

    for oneClient in allClients:
        count += 1
        
        # always create finance charge for first 5 clients 
        # then create finance charge for 1 out of 35 next clients
        
        if (count in range(6)) or ((count + pMonth) % 35 == 0):
            financeCharge = str(count) + ".99"            
            fCreate_OneFinanceCharge(oneClient,count,pMonth,financeCharge)
        else:
            logging.debug('-- skip: ' + str(pMonth) + "-" + oneClient)

    type(Key.F4,KeyModifier.CTRL)
    myTools.checkProcesses()
    myTools.sectionEndTimeStamp()