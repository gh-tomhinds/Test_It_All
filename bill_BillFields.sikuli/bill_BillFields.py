from sikuli import *
import logging
import myTools
import bill_ImportLayout
from bill_Print import fSet_BillDate
import reports_Compare

#---------------------------------------------------#
def fWait_ForBills():
#---------------------------------------------------#

    # wait for report to complete
    wait(Pattern("approve_bills-2.png").targetOffset(-100,-8),FOREVER)
    time.sleep(1)

    # click Do Nothing
    click("do_nothing.png")
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

#---------------------------------------------------#
def fClose_ReportEntry():
#---------------------------------------------------#

    # close report entry / don't save
    logging.debug('-- close report window')
    click("report_generate_bills-1.png")
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(2)
    type("n")    
    time.sleep(1)

#---------------------------------------------------#
def fPrint_BillsToText(pReportName):
#---------------------------------------------------#

    logging.debug("- print bills to text")

    type("b",KeyModifier.CTRL)
    time.sleep(1)

    myTools.pressSHIFTTAB(3)    # get to Print To
    time.sleep(1)
    type("t")                   # ensure Text File is selected
    time.sleep(1)

    # print bills to text
    logging.debug('-- print button')
    type(Key.ENTER)

    logging.debug('Printing: ' + pReportName)

    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + pReportName)
    time.sleep(1)
    type(Key.ENTER)    

    if exists("replace_it-1.png"):
        type(Key.ENTER)
        time.sleep(1)

    fWait_ForBills()
    fClose_ReportEntry()

#---------------------------------------------------#
def fBill_BillFields():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("bill fields")
    logging.debug("fBill_BillFields")    

    reportName = myTools.monthToName(13,"-BillFields-",".txt")

    myTools.getFocus()                                # make sure timeslips has focus
    bill_ImportLayout.fImport_BillLayout("Fields")    # import the layout    
    fSet_BillDate(12)                                 # set billing data to 12/27 for text bills 
    fPrint_BillsToText(reportName)                    # print all bills to one text file
    reports_Compare.Compare_OneReport(reportName)

    myTools.sectionEndTimeStamp()
