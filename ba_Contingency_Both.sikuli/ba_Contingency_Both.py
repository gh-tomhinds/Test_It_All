from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fContingencyBoth_Setup1(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "1")
    logging.debug(pBAClient + "1")

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
    
# switch to cont
    type(Key.HOME)
    myTools.pressDOWN(6)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    myTools.pressTAB(3)
	
    time.sleep(1)    
    type("Contingency - Both")
    time.sleep(1)    
    
# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    type("s",KEY_CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fContingencyBoth_Setup2(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "2")
    logging.debug(pBAClient + "2")

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for both
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)
    
# enter details    

#    if int(Settings.tsVersion) > 2014:
#        myTools.pressTAB(1)
#    else:
    myTools.pressTAB(2)
    
    type(Key.DOWN)
    type(Key.ENTER)
    
# save and close    
    time.sleep(1)    
    type("s",KeyModifier.CTRL)   

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fContingency_Both():
#---------------------------------------------------#

    baClient = "BA-Cont-Both"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Contingency - Both","Contingency - Both","Contingency - Both")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fContingencyBoth_Setup1(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")

    # create some more slips
    ba__Common.fCreate_BASlips(baClient)
    # change billing arrangement
    fContingencyBoth_Setup2(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,2)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "2")
