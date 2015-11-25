from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_TimekeeperInfo(pReportName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print timekeepers")
    logging.debug('fPrint_TimekeeperInfo: ' + pReportName)

    # make sure timeslips has focus
    myTools.getFocus()
    
    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("t")    
    time.sleep(1)
    
    logging.debug('- set up timekeeper info listing')
    type("timekeeper info")    
    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # Options
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # Default
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # overhead costs
    myTools.pressTAB(6)
    type(Key.SPACE)
    time.sleep(1)   

    # OK
    myTools.pressTAB(6)
    type(Key.SPACE)
    time.sleep(1)

    # choose CSV
    myTools.pressTAB(2)
    type("c")    
    type(Key.ENTER)
    time.sleep(1)

    myTools.finishReport(pReportName)