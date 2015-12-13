from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_OneRefund(pClient,pMonth,pAmount):
#---------------------------------------------------#

    logging.debug('- Create_OneRefund: ' + str(pMonth) + "-" + pClient + " = " + str(pAmount))

    # new transaction
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()

    # switch to Refund

    type(Key.UP)    # this is to get by a UI defect
    time.sleep(1)
    
    type("r")
    time.sleep(1)   
    type(Key.TAB)
       
    # client
    myTools.enterClient(pClient)
        
    # date
    tranDate = str(pMonth) + "/28/" + Settings.dataYear
    type(tranDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Amount
    type(str(pAmount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type("Refund: " + pClient + " - " + tranDate)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.TAB)

    # payment list
    if (int(Settings.tsVersion) > 2016) and (Settings.tsDB == "PREM"):
        type(Key.SPACE)             # in TS2017+ PREM, this marks the check box
    else:    
        type(Key.DOWN)              # in others, this movement highlights first in list
    time.sleep(1)
    type("s",KeyModifier.CTRL)   
    myTools.waitForTransSave()    

#---------------------------------------------------#
def fCreate_Refunds(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("refunds" + str(pMonth))
    logging.debug('fCreate_Refunds: ' + str(pMonth))

    # list the client that will get a refund each month
    refundClients = ["Hawley","Haverhill","Hatfield","Harwich","Harvard","Hawley","Haverhill","Hatfield","Harwich","Harvard","Hawley","Haverhill"]
    oneClient = refundClients[(pMonth - 1)]

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    refundAmount = 99 + pMonth/float(100)        
    fCreate_OneRefund(oneClient,pMonth,refundAmount)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()
    myTools.checkProcesses()