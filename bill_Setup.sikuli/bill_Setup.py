from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fSetup_BillReport():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup bills")
    logging.debug('- set up bill report')

    myTools.getFocus()

    type("b",KeyModifier.CTRL)
    time.sleep(1)

    myTools.pressTAB(4)
    type(Key.ENTER)
    time.sleep(1)

# default button
    type("d",KeyModifier.ALT)

# mark a/r tran follow slip date
    myTools.pressTAB(6)
    time.sleep(1)
    type(Key.SPACE)

# unmark send bills by email
    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(4)
    else:
        myTools.pressTAB(5)        
    time.sleep(1)
    type(Key.SPACE)

# unmark envelopes
    myTools.pressTAB(4)
    time.sleep(1)
    type(Key.SPACE)
    time.sleep(1)

# OK
    type(Key.ENTER)
    time.sleep(1)

# Print to Text
    myTools.pressTAB(2)
    type("t")
    time.sleep(1)

# PDF Options
#    myTools.pressTAB(2)
#    type(Key.SPACE)
#    time.sleep(1)
#    type(Key.UP)
#    time.sleep(1)
#    type(Key.ENTER) 

# SAVE and Close
    type("s",KeyModifier.CTRL)
    
    # delay to get by error
    time.sleep(2)
    
    type(Key.ENTER)    
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()