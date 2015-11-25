from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fSetup_ARwRunBal():
#---------------------------------------------------#

    logging.debug('- set up ARwRunBal')
    
    myTools.getFocus()
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)
    myTools.pressDOWN(2)
    time.sleep(1)

    myTools.removeDateAndTime()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def fPrint_ARwRunBal(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print ARwRunBal")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("ARwRunBal",pRepExt)
    logging.debug('fPrint_ARwRunBal: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)

    logging.debug('- choose report')
    myTools.pressDOWN(2)
    time.sleep(1)

    # choose txt
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("t")
    time.sleep(1)

    myTools.enterCurrentMonthOnList(pReportMonth)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)