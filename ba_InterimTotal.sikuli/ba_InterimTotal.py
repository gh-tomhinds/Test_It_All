from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimTotal_Setup1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimTot1")
    logging.debug("ba InterimTot1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimTot")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to interim
    type(Key.HOME)
    myTools.pressDOWN(13)
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("500")
    time.sleep(1)    
    type(Key.ENTER)
	
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimTotal_Setup2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimTot2")
    logging.debug("ba InterimTot2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimTot")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)    
    type("600")
    time.sleep(1)    
    type(Key.ENTER)
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimTotal_Setup3():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba InterimTot3")
    logging.debug("ba InterimTot3")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-InterimTot")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    
# enter details    
    type(Key.ENTER)
    time.sleep(1)    
    type("700")
    time.sleep(1)    

    type("u",KeyModifier.ALT)
    type(Key.END)
    type(Key.ENTER)

# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInterimTotal():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-InterimTot","BA-InterimTot","Interim Total FF","Interim Total FF","Interim Total FF")
    # create some slips
    ba__Common.fCreate_BASlips("BA-InterimTot")
    # set up billing arrangement
    fInterimTotal_Setup1() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-InterimTot",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-InterimTot1")

    # create some slips
    ba__Common.fCreate_BASlips("BA-InterimTot")
    # set up billing arrangement
    fInterimTotal_Setup2() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-InterimTot",2)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-InterimTot2")

    # create some slips
    ba__Common.fCreate_BASlips("BA-InterimTot")
    # set up billing arrangement
    fInterimTotal_Setup3() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-InterimTot",3)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-InterimTot3")
