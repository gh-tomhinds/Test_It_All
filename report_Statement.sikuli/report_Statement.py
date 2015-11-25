from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fImport_Statement():
#---------------------------------------------------#

    logging.debug('- fImport_Statement')

    # make sure timeslips has focus
    myTools.getFocus()

    type("b",KeyModifier.ALT)         # layouts
    type("t")
    time.sleep(1)
    type(Key.F6)
    time.sleep(1)

    type("o",KeyModifier.CTRL)        # open
    time.sleep(1)

    type("l",KeyModifier.ALT)         # import
    type("p")
    time.sleep(1)

    statementLayout = Settings.dataFolder + '\\Statement.tsl'
    type(statementLayout)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)
    type("y")
    time.sleep(1)

    type(Key.F4,KeyModifier.CTRL)     # close / save
    time.sleep(1)
    type("y")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)

#---------------------------------------------------#
def fPrint_Statement(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print statements")

    # name report file: ex: Statement-03
    reportName = myTools.buildRepName("Statement",pRepExt)
    logging.debug('Print_Statement: ' + reportName)
    myTools.getFocus()

    logging.debug('- open report list')
    type("b",KeyModifier.ALT)
    type("s")
    time.sleep(1)

    # text file
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("t")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    # fill in path and name
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)

    # press ENTER to print
    type(Key.ENTER)    

    # wait for report to complete
    myTools.waitForStatement()

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    # close the report
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("n")

    myTools.sectionEndTimeStamp()