from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fProgressTotal_Setup1():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ProgressTot1")
    logging.debug("ba ProgressTot1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-ProgressTot")
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to minimum
    type(Key.HOME)
    myTools.pressDOWN(11)
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
    type(Key.F4,KEY_CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fProgressTotal_Setup2():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ProgressTot2")
    logging.debug("ba ProgressTot2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-ProgressTot")
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
def fProgressTotal_Setup3():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba ProgressTot3")
    logging.debug("ba ProgressTot3")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-ProgressTot")
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
def fProgressTotal():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-ProgressTot","BA-ProgressTot","Progress Total FF","Progress Total FF","Progress Total FF")
    # create some slips
    ba__Common.fCreate_BASlips("BA-ProgressTot")
    # set up billing arrangement
    fProgressTotal_Setup1() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ProgressTot",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ProgressTot1")

    # create some slips
    ba__Common.fCreate_BASlips("BA-ProgressTot")
    # set up billing arrangement
    fProgressTotal_Setup2() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ProgressTot",2)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ProgressTot2")

    # create some slips
    ba__Common.fCreate_BASlips("BA-ProgressTot")
    # set up billing arrangement
    fProgressTotal_Setup3() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ProgressTot",3)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ProgressTot3")
