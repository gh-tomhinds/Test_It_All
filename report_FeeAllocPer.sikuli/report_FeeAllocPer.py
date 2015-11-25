from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_FeeAllocPer(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print FeeAllocPer")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("FeeAllocPer",pRepExt)
    logging.debug('Print_FeeAllocPer: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open FeeAllocPer')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(1)
    myTools.pressDOWN(3)
    time.sleep(1)    

    # choose csv
    myTools.pressSHIFTTAB(2)
    type("c")
    time.sleep(1)

    myTools.enterCurrentMonthOnList(pReportMonth)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)