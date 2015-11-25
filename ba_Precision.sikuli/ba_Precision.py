from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fPrecision_Setup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("ba Precision")
    logging.debug("ba Precision")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type("BA-Precision")
    type(Key.ENTER)
    time.sleep(1)

# get to Rounding field
    if int(Settings.tsVersion) < 2015:
        myTools.pressF6(4)
        time.sleep(1)
        myTools.pressTAB(8)
    else:
        myTools.pressF6(7)
        time.sleep(1)
        myTools.pressTAB(7)               

    time.sleep(1)
    type(Key.UP) 
    
# save and close    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fPrecision():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # create a new client    
    client_Create.fCreate_Client("BA-Precision","BA-Precision","Precision Settings","Precision Settings","Precision Settings")
    # create some slips
    ba__Common.fCreate_BASlips("BA-Precision")
    # set up billing arrangement
    fPrecision_Setup() 
    # print a bill to text
    ba__Common.fPrint_BABill("BA-Precision",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-Precision1")
