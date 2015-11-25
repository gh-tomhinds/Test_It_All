from sikuli import *
import logging
import myTools
import reports_Compare
from report_UDClient import fCreate_UDReport

#---------------------------------------------------#
def fCreate_SlipListDetailed():
#---------------------------------------------------#

    logging.debug('- fCreate_SlipListDetailed')

    # make sure timeslips has focus
    myTools.getFocus()

    type(Key.F3,KeyModifier.CTRL)     # create a report
    time.sleep(1)
    type("r",KeyModifier.ALT)         # ud report
    type("n",KeyModifier.ALT)         # next
    time.sleep(1)

    type("s")                         # slip
    type("n",KeyModifier.ALT)         # next
    time.sleep(1)

    myTools.pressDOWN(2)              # detailed Listing Simple
    type("n",KeyModifier.ALT)         # next
    time.sleep(1)

    type("n",KeyModifier.ALT)         # next
    type(Key.ENTER)                   # Open Report Entry
    time.sleep(1)

    type("s",KeyModifier.CTRL)        # save
    type(Key.ENTER)                   # OK
    time.sleep(1)
    
    type(Key.F4,KeyModifier.CTRL)     # close report
    time.sleep(1)

#---------------------------------------------------#
def fCreate_SlipFields():
#---------------------------------------------------#

    logging.debug('- fCreate_SlipFields')
    repTemplate = "UDS SlipFields"
    fCreate_UDReport("s",repTemplate,"user")

#---------------------------------------------------#
def fCreate_SlipListCalc():
#---------------------------------------------------#

    logging.debug('- fCreate_SlipListCalc')
    repTemplate = "UDS Calcs"
    fCreate_UDReport("s",repTemplate,"user")

#---------------------------------------------------#
def fSort_SlipReportFields():
#---------------------------------------------------#

    logging.debug('- fSort_SlipReportFields')

    time.sleep(1)
    type("o",KeyModifier.CTRL)
    time.sleep(1)

    # switch to sort
    type(Key.F6)
    time.sleep(1)
    
    # select slip num
    myTools.pressTAB(1)
    time.sleep(1)
    type(Key.END)
    time.sleep(1)
    myTools.pressUP(4)
    time.sleep(1)    
    myTools.pressTAB(1)
    time.sleep(1)
    type(Key.SPACE)

#---------------------------------------------------#
def fChoose_CSV_Print(pReportName):
#---------------------------------------------------#

    logging.debug('- fChoose_CSV_Print')

    # choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    # fill in path and name; press ENTER    
    type(Settings.repFolder + "\\" + pReportName)
    time.sleep(1)
    myTools.pressTAB(2)
    time.sleep(1)
    type(Key.SPACE)
    time.sleep(1)  
    type(Key.ENTER)    

#---------------------------------------------------#
def fPrint_SlipListDetailed(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print sliplistdetailed")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("UDSlip1",pRepExt)
    logging.debug('Print_UDSlip1: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)

    logging.debug('- choose report')
    type("slip listing - d")
    time.sleep(1)

#    fSort_SlipReportFields()
    fChoose_CSV_Print(reportName)
    myTools.waitForReport()
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("n")
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPrint_SlipFields(pReportMonth,pRepExt):
#---------------------------------------------------#

    # this does not include applied fields, since we fixed some stuff in ts2016

    myTools.sectionStartTimeStamp("print slipfields")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("UDSlip2",pRepExt)
    logging.debug('Print_UDSlip2: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)

    logging.debug('- choose report')
    type("UDS SlipFields")
    time.sleep(1)

#    fSort_SlipReportFields()
    fChoose_CSV_Print(reportName)
    myTools.waitForReport()
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("n")
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPrint_SlipListCalc(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print slipcalcs")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("UDSCalc",pRepExt)
    logging.debug('Print_UDSCalc: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("s")
    time.sleep(1)

    logging.debug('- choose report')
    type("uds c")
    time.sleep(1)

#    fSort_SlipReportFields()
    fChoose_CSV_Print(reportName)
    myTools.waitForReport()
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("n")
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()