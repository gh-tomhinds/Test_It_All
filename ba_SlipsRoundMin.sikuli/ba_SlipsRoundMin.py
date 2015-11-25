from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fSlipsRoundMin_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba RoundMins")
    logging.debug("ba RoundMins")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-RoundMin")
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
    
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fSlipsRoundMin():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-RoundMin","BA-RoundMin","Rounding Minutes","Rounding Minutes","Rounding Minutes")
    # create some slips
    ba__Common.fCreate_BASlips("BA-RoundMin")
    # set up billing arrangement
    fSlipsRoundMin_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-RoundMin",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-RoundMin1")
