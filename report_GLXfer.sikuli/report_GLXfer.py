from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Print_GLXfer(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print glxfer")

    # name report file: ex: TkCC-03
    reportName = myTools.buildRepName("GLXfer",pRepExt)
    logging.debug('Print_GLXfer: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("a",KeyModifier.ALT)
    type("g")
    time.sleep(1)

    logging.debug('- default options')

    # options button
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)
    
    # default button   
    myTools.pressSHIFTTAB(4)
    type(Key.ENTER)
    time.sleep(1)

    # trans types 
    myTools.pressTAB(4)
    type(Key.ENTER)
    time.sleep(1)

    # remove transfer since they were wrong before ts2016
    type("t")
    time.sleep(1)
    type(Key.SPACE)
    time.sleep(1)
    type(Key.ENTER)

    # close dialog
    myTools.pressSHIFTTAB(3)
    type(Key.ENTER)
    time.sleep(1)   

    logging.debug('- print report')

    # move to Print To and choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)