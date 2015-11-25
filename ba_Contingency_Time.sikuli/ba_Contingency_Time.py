from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fContingencyTime_Setup1(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "1")
    logging.debug(pBAClient + "1")

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to contingency
    type(Key.HOME)
    myTools.pressDOWN(8)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")
    myTools.pressTAB(3)
	
    time.sleep(1)    
    type("Contingency - Time")
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
def fContingencyTime_Setup2(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "2")
    logging.debug(pBAClient + "2")

# open client
    myTools.openClient(pBAClient)

# get to arrangement fields
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
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
def fContingency_Time():
#---------------------------------------------------#

    baClient = "BA-Cont-Time"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Contingency - Time","Contingency - Time","Contingency - Time")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fContingencyTime_Setup1(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")

    # create some more slips
    ba__Common.fCreate_BASlips(baClient)
    # change billing arrangement
    fContingencyTime_Setup2(baClient) 
    # print 2nd bill to text
    ba__Common.fPrint_BABill(baClient,2)
    # compare 2nd bill's values
    ba__ReviewBills.fReview_BABill(baClient + "2")
