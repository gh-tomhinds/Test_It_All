from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fContingencyExp_Setup1(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "1")
    logging.debug(pBAClient + "1")

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to contingency
    type(Key.HOME)
    myTools.pressDOWN(8)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(3)

    time.sleep(1)    
    type("Contingency - Expense")
    time.sleep(1)    
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fContingencyExp_Setup2(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "2")
    logging.debug(pBAClient + "2")

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(6)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)
    
#    if int(Settings.tsVersion) > 2014:
#        myTools.pressTAB(1)
#    else:
    myTools.pressTAB(2)
    
    type(Key.DOWN)
    
# save and close    
    type(Key.ENTER)
    type("s",KeyModifier.CTRL)
    
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fContingency_Exp():
#---------------------------------------------------#

    baClient = "BA-Cont-Exp"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Contingency - Exp","Contingency - Exp","Contingency - Exp")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fContingencyExp_Setup1(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")

    # create some more slips
    ba__Common.fCreate_BASlips(baClient)
    # change billing arrangement
    fContingencyExp_Setup2(baClient) 
    # print the 2nd bill to text
    ba__Common.fPrint_BABill(baClient,2)
    # compare 2nd bill's values
    ba__ReviewBills.fReview_BABill(baClient + "2")
