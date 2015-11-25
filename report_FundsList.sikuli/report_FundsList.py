from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_FundsList(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print FundsList")

    # name report file: ex: ARAgedBal-03
    reportName = myTools.buildRepName("FundsList",pRepExt)
    logging.debug('fPrint_FundsList: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("f")
    time.sleep(1)
    type("funds t")
    time.sleep(1)

    type("o",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F6)
    time.sleep(1)    

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")
    time.sleep(1)

    # move to sort list, choose ID
    myTools.pressTAB(5)
    time.sleep(1)
    type(Key.SPACE)
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)