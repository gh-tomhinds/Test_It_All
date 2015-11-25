from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def fSetup_AgedARBalDate():
#---------------------------------------------------#

    logging.debug('- fSetup_AgedARBalDate')

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("b")
    time.sleep(1)
    myTools.pressDOWN(1)
    time.sleep(1)

    logging.debug('- options')
    type("o",KeyModifier.CTRL)
    myTools.pressSHIFTTAB(4)
    time.sleep(1)
    type(Key.SPACE)
    time.sleep(1)

    logging.debug('- default')
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    logging.debug('- include last pay')
    myTools.pressSHIFTTAB(10)
    type(Key.SPACE)
    time.sleep(1)

    logging.debug('- include last bill date')
    myTools.pressSHIFTTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    logging.debug('- include interest')
    myTools.pressSHIFTTAB(2)
    type(Key.SPACE)
    time.sleep(1)

    logging.debug('- include costs')
    myTools.pressSHIFTTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    logging.debug('- include fees')
    myTools.pressSHIFTTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    type(Key.ENTER)
    time.sleep(1)

    type("s",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def Print_ARAgedBalDate(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print aged bal date")

    # name report file: ex: AgedARDate-03
    reportName = myTools.buildRepName("AgedARDate",pRepExt)
    logging.debug('Print_AgedARDate: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("b")
    time.sleep(1)
    myTools.pressDOWN(1)
    time.sleep(1)

    # move to Print To and choose CSV
    myTools.pressSHIFTTAB(2)
    time.sleep(1)
    type("c")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)