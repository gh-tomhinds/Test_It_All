from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_Task():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("create task")

    logging.debug('Create_Task: Skipping')

    logging.debug('- open task list')
    type("n",KeyModifier.ALT)
    type("f")
    time.sleep(1)

    logging.debug('- create new task')
    type("n",KeyModifier.CTRL)

    logging.debug('  - names')
    # NN1
    type("Skipping")
    # NN2
    type(Key.TAB)
    type("1234")
    # Full name
    type(Key.ENTER)
    type("Skipping Around in Circles")
    # category
    type(Key.TAB)
    type("o")
    time.sleep(1)
    
    logging.debug('  - rates')
    myTools.pressTAB(2)
    type("1")
    type(Key.TAB)    
    type("2")    
    type(Key.TAB)    
    type("3")
    type(Key.TAB)    
    type("4")    
    type(Key.TAB)    
    type("5")
    type(Key.TAB)    
    type("6")    
    type(Key.TAB)    
    type("7")
    type(Key.TAB)    
    type("8")    
    type(Key.TAB)    
    type("9")
    type(Key.TAB)    
    type("10")    
    type(Key.TAB)    
    type("11")
    type(Key.TAB)    
    type("12")    
    type(Key.TAB)    
    type("13")
    type(Key.TAB)    
    type("14")    
    type(Key.TAB)    
    type("15")
    type(Key.TAB)    
    type("16")    
    type(Key.TAB)    
    type("17")
    type(Key.TAB)    
    type("18")    
    type(Key.TAB)    
    type("19")
    type(Key.TAB)    
    type("20")    

    logging.debug('  - defaults')
    time.sleep(1)
    myTools.pressTAB(2)
    # time spent
    type("11.2")    
    type(Key.TAB)
    # time est
    type("11.1")    
    type(Key.TAB)
    # bill status
    type("b")
    type(Key.TAB)
    # hold
    type("o")
    type(Key.TAB)
    # description
    type("Frolicking and Playing")

    logging.debug('- save and close task list')
    type("s",KeyModifier.CTRL)
    
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)    
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()