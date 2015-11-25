from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fEdit_TaskGenInfo():
#---------------------------------------------------#

    logging.debug('- open task list')
    type("n",KeyModifier.ALT)
    type("f")
    time.sleep(1)
    logging.debug('- edit last task')
    logging.debug('  - names')
    type("ski")
    type(Key.ENTER)
    time.sleep(1)
    type("a",KeyModifier.CTRL)
    type("Build Structure")
    type(Key.TAB)
    type("CON001")
    myTools.pressTAB(2)
    type("Construct Structure")

    type(Key.TAB)
    type("Con")
    type(Key.TAB)
    time.sleep(1)

    logging.debug('  - rates')
    type(Key.TAB)    

    # filling rates with 101.01 thru 101.20
    for i in range(101,121):
        i += 10000
        rate = str(float(i)/100)
        type(rate)
        type(Key.TAB)
    time.sleep(1)    

    logging.debug('  - defaults')
    type(Key.TAB)
    type("1.2")
    type(Key.TAB)
    type("1.1")        
    myTools.pressTAB(3)
    type("a",KeyModifier.CTRL)
    time.sleep(1)
    type("Create something new")

#---------------------------------------------------#
def fEdit_TaskCustom():
#---------------------------------------------------#

    logging.debug('  - custom fields')

# switch to custom fields
    myTools.pressF6(2)
    type(Key.TAB)

# Date
    type("1/1/15")
    type(Key.TAB)
 # Hours
    type("101.01")
    type(Key.TAB)
 # List
    type("Construction")
    type(Key.TAB)
 # Money
    type("101.01")
    type(Key.TAB)
    time.sleep(1)    
 # Number
    type("101.01")
    type(Key.TAB)
 # Percent
    type("101.01")
    type(Key.TAB)
 # Text
    type("Build Structure")
    type(Key.TAB)
    
    time.sleep(1)

#---------------------------------------------------#
def fEdit_Task():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("edit task")

    logging.debug('Edit_Task')

    # make sure timeslips has focus
    myTools.getFocus()
    
    fEdit_TaskGenInfo()
    fEdit_TaskCustom()    

    logging.debug('- save and close task list')
    type("s",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)    
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()