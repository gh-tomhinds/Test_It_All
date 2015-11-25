from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_AvailableWIP(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print AvailableWIP")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("AvailableWIP",pRepExt)
    logging.debug('Print_AvailableWIP: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open AvailableWIP')
    type("r",KeyModifier.ALT)
    type("c")
    time.sleep(1)
    myTools.pressDOWN(4)
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
    type(Key.ENTER)
    time.sleep(1)

    # choose csv
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"y")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)