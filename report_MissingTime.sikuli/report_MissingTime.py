from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fPrint_MissingTime(pReportMonth,pRepExt,pAorB):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print MissingTime")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("MissingTime",pRepExt)
    logging.debug('Print_MissingTime: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open MissingTime')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(1)
    type("m")
    time.sleep(1)

    # choose csv
    myTools.pressSHIFTTAB(2)
    type("c")
    time.sleep(1)

    # period
    myTools.pressSHIFTTAB(2)
    if pAorB == "a":
        perDate = str(pReportMonth) + "/01/13" 
    else:
        perDate = str(pReportMonth) + "/15/13" 
    type(perDate)

    # tab to print button to get around AV
    myTools.pressTAB(3)   

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)