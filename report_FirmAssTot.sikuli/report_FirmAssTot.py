from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fSetup_FirmAssTot():
#---------------------------------------------------#

    logging.debug('- set firmasstot')
    
    myTools.getFocus()
    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("b")
    time.sleep(1)
    type("f")
    myTools.pressDOWN(1)
    time.sleep(1)

    myTools.removeDateAndTime()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def fPrint_FirmAssTot(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print FirmAssTot")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("FirmAssTot",pRepExt)
    logging.debug('Print_FirmAssTot: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open FirmAssTot')
    type("r",KeyModifier.ALT)
    type("b")
    time.sleep(1)
    type("f")
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

    # OK
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # choose text
    myTools.pressTAB(2)
    type("t")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"n")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)