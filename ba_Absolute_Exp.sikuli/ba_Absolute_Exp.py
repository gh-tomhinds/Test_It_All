from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fAbsoluteExp_Setup(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient)
    logging.debug(pBAClient)

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to absolute
    type(Key.HOME)
    myTools.pressDOWN(4)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    myTools.pressTAB(3)
	
    time.sleep(1)    
    type("Absolute FF - Expense")
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
def fAbsolute_Exp():
#---------------------------------------------------#

    baClient = "BA-Absolute-Exp"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Absolute FF - Expense","Absolute FF - Expense","Absolute FF - Expense")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fAbsoluteExp_Setup(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")
