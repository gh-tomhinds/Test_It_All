from sikuli import *
import logging
import myTools
import reports_Compare
from report_UDClient import fCreate_UDReport

#---------------------------------------------------#
def fCreate_FundsListFields():
#---------------------------------------------------#

    logging.debug('- fCreate_FundsListFields')
    repTemplate = "UDF Fields"
    fCreate_UDReport("f",repTemplate,"user")

#---------------------------------------------------#
def fSort_FundsListFields():
#---------------------------------------------------#

    logging.debug('- fSort_FundsListFields')

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("f")
    time.sleep(1)

    # open report
    type("udf")
    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # add funds id sort
    type(Key.F6)
    time.sleep(1)
    myTools.pressTAB(2)
    time.sleep(1)
    type(Key.SPACE)

    # close and save report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def fPrint_FundsListFields(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print fundsfields")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("UDFunds1",pRepExt)
    logging.debug('Print_UDFunds1: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("f")
    time.sleep(1)

    logging.debug('- choose report')
    type("udf")
    time.sleep(1)

    # choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    # fill in path and name
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)

    # export column titles
    myTools.pressTAB(2)
    time.sleep(1)
    type(Key.SPACE)
    time.sleep(1)

    # press ENTER to print
    type(Key.ENTER)    

    # wait for report to complete
    myTools.waitForReport()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()