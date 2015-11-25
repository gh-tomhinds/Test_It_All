from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_FirmAssList(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print FirmAssList")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("FirmAssList",pRepExt)
    logging.debug('Print_FirmAssList: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open FirmAssList')
    type("r",KeyModifier.ALT)
    type("b")
    time.sleep(1)
    type("f")
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

    # OK
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # choose csv
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"n")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)