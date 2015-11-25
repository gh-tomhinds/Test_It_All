from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fEdit_TkGenInfo():
#---------------------------------------------------#

    logging.debug('- open timekeeper list')
    type("n",KeyModifier.ALT)    
    type("n")
    time.sleep(1)
    logging.debug('- edit default timekeeper')
    logging.debug('  - names')

# select timekeeper
    type("x")
    type(Key.ENTER)
    time.sleep(1)
# edit stuff
    type("a",KeyModifier.CTRL)
    type("TomH")
    type(Key.TAB)
    type("HindsT")

    myTools.pressTAB(2)
    type("Tom Hinds")
    type(Key.TAB)
    type("TH")    
    myTools.pressTAB(2)

    logging.debug('  - email')
    time.sleep(1)
    type("th@example.com")
    type(Key.TAB)
    type("th2@example.com")

    logging.debug('  - rates')
    type(Key.TAB)    

    # filling rates with 101.01 thru 101.20
    for i in range(10101,10121):
        rate = str(float(i)/100)
        type(rate)
        type(Key.TAB)
    time.sleep(1)    

    logging.debug('  - min hours and overhead')
    type("8")    
    type(Key.TAB)
    type(Key.UP)    
    type(Key.TAB)
    type("50.01")

#---------------------------------------------------#
def fEdit_TkCustom():
#---------------------------------------------------#

    logging.debug('  - custom fields')

# switch to custom fields
    type(Key.F6)    
    type(Key.TAB)

# Date
    type("1/1/14")
    type(Key.TAB)
 # Hours
    type("111.11")
    type(Key.TAB)
 # List
    type("Ribs")
    type(Key.TAB)
 # Money
    type("111.11")
    type(Key.TAB)
    time.sleep(1)    
 # Number
    type("111.11")
    type(Key.TAB)
 # Percent
    type("111.11")
    type(Key.TAB)
 # Text
    type("Tom Hinds")
    type(Key.TAB)
    
    time.sleep(1)

#---------------------------------------------------#
def fEdit_Timekeeper():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("edit timekeeper")

    logging.debug('Edit_Timekeeper')

# make sure timeslips has focus
    myTools.getFocus()

    fEdit_TkGenInfo()
    fEdit_TkCustom()    

    logging.debug('- save and close')
    type("s",KeyModifier.CTRL)
    
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)       
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()