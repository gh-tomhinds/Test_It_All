from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def print_SlipSummary(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print SlipSummary")

    # name report file: ex: SlipSumm-03
    reportName = myTools.buildRepName("SlipSumm",pRepExt)
    logging.debug('Print_SlipSumm: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    
    logging.debug('- set up report')
    type("slip s")
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

    # exclude analysis info
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)  

    # OK
    myTools.pressTAB(5)
    type(Key.SPACE)
    time.sleep(1)

    # choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)