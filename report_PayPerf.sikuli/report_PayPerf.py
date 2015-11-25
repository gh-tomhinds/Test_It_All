from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_PayPerf(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print PayPerf")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("PayPerf",pRepExt)
    logging.debug('Print_PayPerf: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open PayPerf')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)
    type("p")
    time.sleep(1)
    myTools.pressDOWN(1)
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

    # Quarterly
    myTools.pressSHIFTTAB(2)
    type("q")
    time.sleep(1)

    # totals
    myTools.pressSHIFTTAB(8)
    type(Key.SPACE)
    time.sleep(1)

    # costs
    myTools.pressSHIFTTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # OK
    type(Key.ENTER)
    time.sleep(1)

    # choose csv
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"y")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)