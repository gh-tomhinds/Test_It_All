from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_TkHistory(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print tk history")

    # name report file: ex: TkHistory-03
    reportName = myTools.buildRepName("TkHistory",pRepExt)   
    logging.debug('Print_TkHistory: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(1)   
    type("timekeeper history")
    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # remove all filters
    myTools.pressTAB(4)
    type(Key.ENTER)

    logging.debug('- default options')

    # options button
    myTools.pressTAB(3)
    type(Key.ENTER)
    time.sleep(1)
    
    # default button   
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)

    # period = quarterly
    myTools.pressSHIFTTAB(2)
    type("q")

    # unmark "show analysis"
    myTools.pressSHIFTTAB(8)
    type(Key.SPACE)

    # close dialog
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