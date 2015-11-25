from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_SlipListing(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print SlipList")

    # name report file: ex: ARAgedBal-03
    reportName = myTools.buildRepName("SlipList",pRepExt)    
    logging.debug('Print_ARAgedBal: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    type("s")
    time.sleep(1)

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)