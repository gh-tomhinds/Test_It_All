from sikuli import *
import logging
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Edit_DefaultClient():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Edit_DefaultClient')

    # make sure timeslips has focus
    myTools.getFocus()

    # open client list
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    
    # open template client
    type(Key.F6)
    type(Key.ENTER)
    time.sleep(1)

    # switch to Funds Accounts page
    myTools.pressSHIFTF6(3)
    time.sleep(1)

    # switch to Account list    
    myTools.pressTAB(3)
    myTools.pressDOWN(1)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    # enter 25 for "balance falls below" and "replenishment"    
    if int(Settings.tsVersion) > 2014:    
        myTools.pressTAB(3)
    else:
        myTools.pressTAB(4)    
    time.sleep(1)
    
    type("25")
    myTools.pressTAB(1)
    type("25")
    myTools.pressTAB(2)
    type(Key.SPACE)
    type(Key.ENTER)
    time.sleep(1)
    type("s",KeyModifier.CTRL)    
    
    time.sleep(1)    
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
