from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_ClientsNotBilled(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print ClientsNotBilled")

    # name report file: ex: Worksheet-03
    reportName = myTools.buildRepName("CliNotBilled",pRepExt)
    logging.debug('Print_CliNotBilled: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("b")    
    time.sleep(1)
    
    logging.debug('- set up report')
    type("c")
    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # Options
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # Default
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # include auto pay
    myTools.pressSHIFTTAB(5)
    type(Key.SPACE)
    time.sleep(1)
    
    # include zero
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # OK
    type(Key.ENTER)
    time.sleep(1)

    # choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    # remove filters
    myTools.pressTAB(7)
    type(Key.ENTER)
    time.sleep(1)   

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)