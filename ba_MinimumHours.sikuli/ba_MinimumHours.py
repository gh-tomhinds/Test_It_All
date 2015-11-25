from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fMinimumHours_Setup(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient)
    logging.debug(pBAClient)

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(pBAClient)
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(9)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    type(Key.TAB)
    type("1")
    type(Key.TAB)
    type("500")
    myTools.pressTAB(3)
	
    time.sleep(1)    
    type("Minimum Hours FF")
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
def fMinimumHours():
#---------------------------------------------------#

    baClient = "BA-MinimumHours"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Minimum Hours FF","Minimum Hours FF","Minimum Hours FF")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fMinimumHours_Setup(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")
