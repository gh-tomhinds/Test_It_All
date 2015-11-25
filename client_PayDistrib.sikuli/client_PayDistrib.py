from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fExport_ClientSettings():
#---------------------------------------------------#
    
    logging.debug('-- export client settings')
    click("export_btn.png")    
    time.sleep(1)

    # move to Export To list
    myTools.pressTAB(1)

    # move to Nahant
    type("n")
    time.sleep(1)

    # move highlight to account for Timeslips weirdness
    type(Key.UP)
    type(Key.DOWN)
    time.sleep(1)

    # highlight and mark rest of clients
    type(Key.END, Key.SHIFT) 
    type(Key.F4)
    time.sleep(1)

    # click Export, then Yes
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

    myTools.waitForExportSuccess()

#---------------------------------------------------#
def fSetup_PayDist():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup pay dist")
    logging.debug('- set up pay dist')

    myTools.getFocus()

    # open client list
    type("i",KeyModifier.CTRL)
    time.sleep(2)
    
    # open Nahant
    type("n")
    type(Key.ENTER)
    time.sleep(1)

    # get to payment distribution fields

    if Settings.tsVersion > "2014":
        myTools.pressF6(8)
        time.sleep(1)
        myTools.pressTAB(6)
        time.sleep(1)
    else:
        myTools.pressF6(5)
        time.sleep(1)
        myTools.pressSHIFTTAB(7)
        time.sleep(1)        

    # First Pay = Newest
    type("n")
    time.sleep(1)

    # Order = Costs/Fees/Int
    myTools.pressTAB(1)
    type("c")
    time.sleep(1)

    # First Pay = Charge Type
    myTools.pressTAB(1)
    type("c")
    time.sleep(1)

    # save
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    fExport_ClientSettings()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)    
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()