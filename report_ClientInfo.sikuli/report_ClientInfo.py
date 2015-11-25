from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_ClientInfo(pReportName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print clients")

    logging.debug('fPrint_ClientInfo: ' + pReportName)

    # make sure timeslips has focus
    myTools.getFocus()
    
    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("c")    
    time.sleep(1)
    
    logging.debug('- set up client info listing')
    type("client info")    
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

    # hide a/r fields
    myTools.pressSHIFTTAB(5)
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