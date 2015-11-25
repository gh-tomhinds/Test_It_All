from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fEdit_ExpenseGenInfo():
#---------------------------------------------------#

    logging.debug('- open expense list')
    type("n",KeyModifier.ALT)
    type("o")
    time.sleep(1)

    logging.debug('- edit lipstick')
    logging.debug('  - names')
    type("lip")
    type(Key.ENTER)
    time.sleep(1)
    type("a",KeyModifier.CTRL)
    type("Hand Tools")
    type(Key.TAB)
    type("E001")
    myTools.pressTAB(2)
    type("Manual tools")
    type(Key.TAB)
    type("h")
    type(Key.TAB)
    time.sleep(1)

    logging.debug('  - prices')
    type(Key.TAB)    
    type("201.001")
    type(Key.TAB)

    if int(Settings.tsVersion) > 2012:

        # filling prices with 201.002 thru 201.020
        for i in range(201002,201021):
            price = str(float(i)/1000)
            type(price)
            type(Key.TAB)
        time.sleep(1)                

# price level to 20
        logging.debug('  - defaults')
        type("1")
        type(Key.TAB)
        time.sleep(1)
    
# Quantity
    type("1.125")    
    myTools.pressTAB(3)
    
# Description
    type("a",KeyModifier.CTRL)
    type("Hammers, saws, etc.")        

#---------------------------------------------------#
def fEdit_ExpenseCustom():
#---------------------------------------------------#

    logging.debug('  - custom fields')

    # switch to custom fields
    myTools.pressF6(2)
    type(Key.TAB)

    # Date
    type("12/1/16")
    type(Key.TAB)
 
    # Hours
    type("301.01")
    type(Key.TAB)
    
    # List
    type("Materials")
    type(Key.TAB)

    # Money
    type("301.01")
    type(Key.TAB)
    time.sleep(1)    
    
    # Number
    type("301.01")
    type(Key.TAB)
    
    # Percent
    type("301.01")
    type(Key.TAB)
    
    # Text
    type("Hand Tools")
    type(Key.TAB)
    
    time.sleep(1)

#---------------------------------------------------#
def fEdit_Expense():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("edit expense")

    logging.debug('Edit_Expense')

    # make sure timeslips has focus
    myTools.getFocus()

    fEdit_ExpenseGenInfo()
    fEdit_ExpenseCustom()    

    logging.debug('- save and close expense list')
    type("s",KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)    
    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()