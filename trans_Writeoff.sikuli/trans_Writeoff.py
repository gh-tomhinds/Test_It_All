from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_OneWriteOff(pClient,pCliNum,pMonth,pAmount):
#---------------------------------------------------#

    logging.debug('- Create_OneWO: ' + str(pMonth) + "-" + pClient + " = " + str(pAmount))

    # new writeoff
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()
    
    # type = writeoff    
    type(Key.HOME)
    type("w")
    type(Key.TAB)     
        
    # client
    myTools.enterClient(pClient)
        
    # date
    woDate = str(pMonth) + "/28/" + Settings.dataYear
    type(woDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Amount
    type(str(pAmount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type(pClient + " - " + str(pCliNum) + " - " + woDate)
    type(Key.ENTER)
    time.sleep(1)

    # move to invoice list
    if (int(Settings.tsVersion) > 2016) and (Settings.tsDB == "PREM"):
        myTools.pressTAB(2)
    else:
        myTools.pressTAB(1)

    # move to last entry
    myTools.moveToLastTrans()
    myTools.clickApplyOne()

    # save
    type("s",KeyModifier.CTRL)
    myTools.waitForTransSave()    

#---------------------------------------------------#
def fCreate_Writeoffs(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("writeoffs" + str(pMonth))
    logging.debug('Create_Writeoffs: ' + str(pMonth))

    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    clientList = ["Blackstone","Carver"]
    for woClient in clientList:    
        count += 1
        if woClient == "Blackstone":
            woAmount = 2
        else:
            woAmount = 3
            
        woAmount = woAmount + pMonth/float(100)            
        fCreate_OneWriteOff(woClient,count,pMonth,woAmount)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()
    myTools.checkProcesses()