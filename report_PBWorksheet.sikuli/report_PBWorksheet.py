from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fSetup_PreBill():
#---------------------------------------------------#

    logging.debug('- set up prebill')
    
    myTools.getFocus()
    logging.debug('- open worksheet')
    type("b",KeyModifier.ALT)
    type("p")

    myTools.removeDateAndTime()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def fPrint_PreBill(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print PBworksheet")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("PreBill",pRepExt)
    logging.debug('Print_PreBill: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open worksheet')
    type("b",KeyModifier.ALT)
    type("p")    
    time.sleep(1)
    
    logging.debug('- set up worksheet')
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