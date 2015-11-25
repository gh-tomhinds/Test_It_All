from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fSetup_InvoiceListing():
#---------------------------------------------------#

    logging.debug('- set up invlist')
    
    myTools.getFocus()
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)
    type("i")
    time.sleep(1)

    myTools.removeDateAndTime()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")
    time.sleep(1)

    # open report
    type("o",KeyModifier.CTRL)
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
def fPrint_InvoiceListing(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print invoicelist")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("InvList",pRepExt)
    logging.debug('Print_InvoiceList: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("a")
    time.sleep(1)

    logging.debug('- choose report')
    type("i")
    time.sleep(1)

    # choose txt
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("t")
    time.sleep(1)

    myTools.enterYearToDateOnList(pReportMonth)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)