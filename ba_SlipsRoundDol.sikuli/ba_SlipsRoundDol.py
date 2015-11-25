from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fSlipsRoundDol_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba RoundDollars")
    logging.debug("ba RoundDollars")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-RoundDol")
    type(Key.ENTER)
    time.sleep(1)

# get to Rounding field
    if int(Settings.tsVersion) < 2015:
        myTools.pressF6(4)
        time.sleep(1)
        myTools.pressTAB(6)
    else:
        myTools.pressF6(7)
        time.sleep(1)
        myTools.pressTAB(5)               

    time.sleep(1)
    type("5") 
    type(Key.TAB)
    type("u")
    
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fSlipsRoundDol():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-RoundDol","BA-RoundDol","Rounding Dollars","Rounding Dollars","Rounding Dollars")
    # create some slips
    ba__Common.fCreate_BASlips("BA-RoundDol")
    # set up billing arrangement
    fSlipsRoundDol_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-RoundDol",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-RoundDol1")
