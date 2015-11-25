from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_AgedClient(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print AgedClient")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("AgedClient",pRepExt)
    logging.debug('Print_AgedClient: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open PayPerf')
    type("r",KeyModifier.ALT)
    type("c")
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

    # Show hours
    myTools.pressTAB(10)
    type(Key.SPACE)
    time.sleep(1)

    # Show Adjustment columns
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # OK
    type(Key.ENTER)
    time.sleep(1)

    # choose csv
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"yy")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)