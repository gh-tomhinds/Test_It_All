from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fHold_Time_NextBill_Hours():
#---------------------------------------------------#

    logging.debug('- Hold_Time_NextBill_Hours')

    # open Wakefield    
    type("Wakefield")
    type(Key.ENTER)
    time.sleep(1)

    # move to page with Hold fields
    if int(Settings.tsVersion) > 2014:
        myTools.pressF6(5)        
    else:
        myTools.pressF6(3)

    # move to Hold time charges
    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(3)        
    else:
        myTools.pressTAB(6)
    time.sleep(1)

    # set to "on next bill" until 5 hours
    myTools.pressDOWN(1)
    myTools.pressTAB(2)
    type("5")

    # save
    time.sleep(1)
    type("s",KeyModifier.CTRL)

#---------------------------------------------------#
def fHold_Exp_AllBills_Amount():
#---------------------------------------------------#

    logging.debug('- Hold_Exp_AllBills_Amount')

    # move to Wales
    type(Key.PAGE_DOWN)

    # move to Hold expense charges
    myTools.pressTAB(1)
    time.sleep(1)

    # set to "on all bills" until $1000 
    myTools.pressDOWN(2)
    myTools.pressTAB(1)
    type("1000")

    # save
    time.sleep(1)
    type("s",KeyModifier.CTRL)

#---------------------------------------------------#
def fHold_Bill_AllBills_AmountAndHours():
#---------------------------------------------------#

    logging.debug('- Hold_Bill_AllBills_AmountAndHours')

    # move to Walpole
    type(Key.PAGE_DOWN)

    # move to Hold full bill
    myTools.pressTAB(1)
    time.sleep(1)

    # set to "on all bills" until 10 hours or 1000
    myTools.pressDOWN(2)
    myTools.pressTAB(1)
    type("1000")
    myTools.pressTAB(1)
    type("10")

    # save
    time.sleep(1)
    type("s",KeyModifier.CTRL)

#---------------------------------------------------#
def fHold_AR_AllBills():
#---------------------------------------------------#

    logging.debug('- Hold_AR_AllBills')

    # move to Waltham
    type(Key.PAGE_DOWN)

    # move to Hold AR
    myTools.pressTAB(1)
    time.sleep(1)

    # set to "on all bills"
    myTools.pressDOWN(2)

    # save
    time.sleep(1)
    type("s",KeyModifier.CTRL)

#---------------------------------------------------#
def fSetup_ClientHold():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("set up client hold")
    logging.debug('set up client hold')

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open client list')
    type("n",KeyModifier.ALT)
    type("i")
    time.sleep(1)

    fHold_Time_NextBill_Hours()
    fHold_Exp_AllBills_Amount()
    fHold_Bill_AllBills_AmountAndHours()
    fHold_AR_AllBills()

    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()