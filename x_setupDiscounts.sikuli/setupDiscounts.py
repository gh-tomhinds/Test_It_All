from sikuli import *
import logging
import myTools


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Setup_Discounts():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug('Set Up Discounts')

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- change a client')
    type("i",KeyModifier.CTRL)
    time.sleep(1)

    type(Key.ENTER)
    time.sleep(1)

    myTools.pressF6(5)
    myTools.pressSHIFTTAB(10)
    time.sleep(1)
    
    type("10")
    type(Key.TAB)
    type("30")
    type(Key.TAB)
    myTools.pressDOWN(2)
    time.sleep(1)

    type("s", KeyModifier.CTRL)
    click("export_btn.png")
    time.sleep(1)
    
    type(Key.DELETE)
    type(Key.UP)
    type(Key.DOWN)
    type(Key.DOWN, KeyModifier.SHIFT)
    type(Key.DOWN, KeyModifier.SHIFT)    
    type(Key.F4)
    time.sleep(1)

    type(Key.TAB)    
    type(Key.INSERT)
    type(Key.TAB)    
    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    

    wait("export_successful.png", FOREVER)
    type(Key.ENTER)    

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
