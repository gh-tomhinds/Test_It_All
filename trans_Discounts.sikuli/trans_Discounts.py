from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_OneDiscount(pClient,pMonth,pAmount):
#---------------------------------------------------#

    logging.debug('- Create_OneDiscount: ' + str(pMonth) + "-" + pClient + " = " + str(pAmount))

    # new transaction
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()

    # switch to Discount

    type(Key.UP)    # this is to get by a UI defect
    time.sleep(1)
    
    type("d")
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
    type("Discount: " + pClient + " - " + tranDate)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.TAB)

    # invoice list
    type(Key.DOWN,KeyModifier.CTRL)
    time.sleep(1)
    click("apply_one.png")
    time.sleep(1)    
    type("s",KeyModifier.CTRL)
    myTools.waitForTransSave()    

#---------------------------------------------------#
def fCreate_Discounts(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("discounts" + str(pMonth))
    logging.debug('fCreate_Discounts: ' + str(pMonth))

    # list the client that will get a refund each month
    discountClients = ["Natick","Orange","Oakham","Oak Bluffs","Southampton","Otis","Oxford","Leyden","Monroe","Monson","Methuen","Uxbridge"]
    oneClient = discountClients[(pMonth - 1)]

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    discountAmount = 49 + pMonth/float(100)
    fCreate_OneDiscount(oneClient,pMonth,discountAmount)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()
    myTools.checkProcesses()