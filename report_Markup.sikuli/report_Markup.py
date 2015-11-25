from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def print_Markup(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print markup")

    # name report file: ex: Markup-03
    reportName = myTools.buildRepName("Markup",pRepExt)
    logging.debug('Print_Markup: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("i")
    time.sleep(2)
    
    type("mark")
    time.sleep(1)
    
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    logging.debug('- default options')

    # options button
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)
    
    # default button   
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)
    
    # OK
    myTools.pressTAB(1)    
    type(Key.ENTER)
    time.sleep(1)

    logging.debug('- print report')

    # move to Print To and choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)