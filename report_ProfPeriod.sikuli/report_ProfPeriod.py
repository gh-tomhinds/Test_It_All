from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def print_ProfPeriod(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print ProdPer")

    # name report file: ex: ProfPer-03
    reportName = myTools.buildRepName("ProfPer",pRepExt)
    logging.debug('Print_ProfPeriod: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)
    
    logging.debug('- set up report')
    type("prof")
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

    # OK
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"y")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)