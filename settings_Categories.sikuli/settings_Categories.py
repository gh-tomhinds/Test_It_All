from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_Categories():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("categories")

    logging.debug('fCreate_Categories')

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open category list')
    type("p",KeyModifier.ALT)
    
    # hot keys changed for TS2014
    if int(Settings.tsVersion) < 2014:
        type("i")
    else:
        type("o")
    time.sleep(1)

    for category in ["Construction","General","Landscape","Hardware","Supplies","Materials","Other"]:
        logging.debug('-- create: ' + category)
        type("n",KeyModifier.ALT)
        type(category)
        type(Key.ENTER)

    logging.debug('- close list')
    myTools.pressTAB(4)
    type(Key.ENTER)    

    myTools.sectionEndTimeStamp()
