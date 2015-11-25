from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fCreate_UDReport(pRepGroup,pRepTemplate,pRepToDup):
#---------------------------------------------------#

    logging.debug('-- fCreate_UDReport')

    # make sure timeslips has focus
    myTools.getFocus()

    type("r",KeyModifier.ALT)         # report menu
    type(pRepGroup)
    time.sleep(1)

    type(pRepToDup)                   # highlight "user-defined"
    time.sleep(1)

    click("design_tool.png")
    time.sleep(2)

    type("l",KeyModifier.ALT)         # duplicate
    type("a")
    time.sleep(1)

    type("a",KeyModifier.CTRL)        # rename
    time.sleep(1)
    type(pRepTemplate)
    time.sleep(1)

    type("l",KeyModifier.ALT)         # import fields
    type("p")
    time.sleep(1)

    templateName = Settings.dataFolder + '\\' + pRepTemplate + '.tsl'
    paste(templateName)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    type(Key.F4,KeyModifier.CTRL)      # close / save
    time.sleep(1)
    type(Key.ENTER)

    type(Key.F4,KeyModifier.CTRL)      # close
    time.sleep(1)

#---------------------------------------------------#
def fCreate_ClientListHistory():
#---------------------------------------------------#

    logging.debug('- fCreate_ClientListHistory')
    repTemplate = "UDC History"
    fCreate_UDReport("c",repTemplate,"user")
    
#---------------------------------------------------#
def fCreate_ClientListValues():
#---------------------------------------------------#

    logging.debug('- fCreate_ClientListValues')
    repTemplate = "UDC Values"
    fCreate_UDReport("c",repTemplate,"user")

#---------------------------------------------------#
def fPrint_ClientListHistory(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print clienthistory")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("UDClient1",pRepExt)
    logging.debug('Print_UDClient1: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("c")
    time.sleep(1)

    logging.debug('- choose report')
    type("ud")
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

#---------------------------------------------------#
def fPrint_ClientListValues(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print clientvalues")

    # name report file: ex: UDSlip1-03
    reportName = myTools.buildRepName("UDClient2",pRepExt)
    logging.debug('Print_UDClient2: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("r",KeyModifier.ALT)
    type("c")
    time.sleep(1)

    logging.debug('- choose report')
    type("ud")
    time.sleep(1)
    myTools.pressDOWN(1)
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
