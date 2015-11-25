from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_AgedInv(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print AgedInv")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("AgedInv",pRepExt)
    logging.debug('Print_AgedInv: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open AgedInv')
    type("r",KeyModifier.ALT)
    type("c")
    time.sleep(1)
    myTools.pressDOWN(2)
    time.sleep(1)
    
    logging.debug('- set up report')
    type("o",KeyModifier.CTRL)
    
    # Options
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # Default
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # Due values
    myTools.pressSHIFTTAB(4)
    type("d")
    time.sleep(1)

    # OK
    type(Key.ENTER)
    time.sleep(1)

    # choose csv
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)