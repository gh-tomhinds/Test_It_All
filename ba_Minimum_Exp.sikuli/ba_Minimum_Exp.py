from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fMinimumExp_Setup(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient)
    logging.debug(pBAClient)

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(pBAClient)
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(5)
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("5000")
    myTools.pressTAB(2)
	
    time.sleep(1)    
    type("Minimum FF - Expense")
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
def fMinimum_Exp():
#---------------------------------------------------#

    baClient = "BA-Minimum-Exp"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Minimum FF - Exp","Minimum FF - Exp","Minimum FF - Exp")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fMinimumExp_Setup(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")
