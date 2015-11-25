from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_AgedWIP(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print AgedWIP")

    # name report file: ex: ARAgedBal-03    
    reportName = myTools.buildRepName("AgedWIP",pRepExt)    
    logging.debug('fPrint_AgedWIP: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("c")
    time.sleep(1)
    type("aged w")
    time.sleep(1)

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)