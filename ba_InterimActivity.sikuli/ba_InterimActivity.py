from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fInterimActivity_Setup1(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "1")
    logging.debug(pBAClient + "1")

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to Interim
    type(Key.END)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1) 
    type(Key.DOWN)
    time.sleep(1) 
    type("o",KeyModifier.ALT)    
    type("500")
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)    
    type(Key.ENTER)
	
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimActivity_Setup2(pBAClient):
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp(pBAClient + "2")
    logging.debug(pBAClient + "2")

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)
    type(Key.DOWN)
    time.sleep(1)
    type("o",KeyModifier.ALT)        
    type("600")
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)    
    type(Key.ENTER)
    
# save and close    
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    if int(Settings.tsVersion) > 2014:
        if exists("are_you_sure.png"):
            type("y",KeyModifier.ALT)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fInterimActivity_Setup3(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "3")
    logging.debug(pBAClient + "3")

# open client
    myTools.openClient(pBAClient)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)
    type(Key.DOWN)
    time.sleep(1)
    type("o",KeyModifier.ALT)        
    type("700")
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)    
    type("u",KeyModifier.ALT)
    type(Key.DOWN)
    type(Key.ENTER)
    
# save and close    
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    if int(Settings.tsVersion) > 2014:
        if exists("are_you_sure.png"):
            type("y",KeyModifier.ALT)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fInterimActivity():
#---------------------------------------------------#

    baClient = "BA-InterimAct"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Interim Activity FF","Interim Activity FF","Interim Activity FF")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fInterimActivity_Setup1(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")

    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fInterimActivity_Setup2(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,2)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "2")

    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fInterimActivity_Setup3(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,3)
    # compare at bill values
    ba__ReviewBills.fReview_BABill(baClient + "BA-InterimAct3")
