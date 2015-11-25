from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_SplitBill(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print splitbill")

    # name report file: ex: ARAgedBal-03
    reportName = myTools.buildRepName("Split",pRepExt)    
    logging.debug('Print_SplitBill: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("b")
    time.sleep(1)
    type("s")

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)