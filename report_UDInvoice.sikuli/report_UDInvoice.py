from sikuli import *
import logging
import myTools
import reports_Compare
from report_UDClient import fCreate_UDReport

#---------------------------------------------------#
def fCreate_InvoiceListFields():
#---------------------------------------------------#

    logging.debug('- fCreate_InvoiceListFields')
    repTemplate = "UDI Fields"
    fCreate_UDReport("a",repTemplate,"user-defined i")

#---------------------------------------------------#
def fSort_InvoiceListFields():
#---------------------------------------------------#

    logging.debug('- fSort_InvoiceListFields')

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)

    # open report
    type("udi")
    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # add invoice number sort
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
def fPrint_InvoiceListFields(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print invoicefields")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("UDInvoice1",pRepExt)
    logging.debug('Print_UDInvoice1: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)

    logging.debug('- choose report')
    type("udi")
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