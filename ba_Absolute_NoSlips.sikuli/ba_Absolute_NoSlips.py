from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fAbsoluteNoSlips_Setup(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient)
    logging.debug(pBAClient)

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for both
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(3)
    
    type(Key.RIGHT)
    time.sleep(1)    
    type(Key.ENTER)

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)  
    
# switch to absolute
    type(Key.HOME)
    myTools.pressDOWN(2)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)    
    time.sleep(1)

    type("1000")
    myTools.pressTAB(1)
    time.sleep(1)    

    if int(Settings.tsVersion) > 2014:
        type(Key.TAB)

    type("n")
    myTools.pressTAB(1)
    time.sleep(1)    

    type("3")
    myTools.pressTAB(1)
    time.sleep(1)    

    time.sleep(1)    
    type("Absolute FF - NoSlips")
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
def fAbsolute_NoSlips():
#---------------------------------------------------#

    baClient = "BA-Absolute-NoSlips"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Absolute FF - NoSlips","Absolute FF - NoSlips","Absolute FF - NoSlips")
    # do not create some slips
    # set up billing arrangement
    fAbsoluteNoSlips_Setup(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,2)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "2")
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,3)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "3")

