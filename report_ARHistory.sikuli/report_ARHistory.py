from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_ARHistory(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print ARHistory")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("ARHist",pRepExt)
    logging.debug('fPrint_ARHistory: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)

    # choose txt
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")
    time.sleep(1)

    myTools.enterYearToDateOnList(pReportMonth)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)