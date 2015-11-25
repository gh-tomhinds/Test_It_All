from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAdjustTimekeeperExp_Setup(pBAClient):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp(pBAClient)
    logging.debug(pBAClient)

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for exp
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
        
# switch to adjust by timekeeper    
    type(Key.HOME)
    myTools.pressDOWN(2)    

# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("n",KeyModifier.ALT)
    type("sh")    
    type(Key.TAB)    
    type("25")
    type(Key.TAB)    
    type(Key.RIGHT)    

    if int(Settings.tsVersion) < 2014:
        myTools.pressTAB(3)
    else:
        type("d",KeyModifier.ALT)
		
    time.sleep(1)    
    type("Adjust Timekeeper - Exp")
    time.sleep(1)    

# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    myTools.pressTAB(4)
    type(Key.SPACE)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fAdjustTimekeeper_Exp():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    baClient = "BA-AdjTK-Exp"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Adjust Timekeeper - Expense","Adjust Timekeeper - Expense","Adjust Timekeeper - Expense")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fAdjustTimekeeperExp_Setup(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")
