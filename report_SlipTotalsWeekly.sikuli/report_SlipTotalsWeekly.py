from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_SlipTotalsWeekly(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("slip totals")

    # name report file: ex: PayDistr-03
    reportName = myTools.buildRepName("SlipTot",pRepExt)
    logging.debug('Print_SlipTotalsWeekly: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(2)
    
    type("w")
    time.sleep(1)
    
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    logging.debug('- default options')

    # switch to CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")    

    # options button
    myTools.pressSHIFTTAB(2)
    type(Key.ENTER)
    time.sleep(1)
    
    # default button   
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)

    # Include totals
    myTools.pressTAB(8)
    time.sleep(1)
    type(Key.SPACE)
    
    # OK
    type(Key.ENTER)
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"y")

    logging.debug('- print report')

    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)