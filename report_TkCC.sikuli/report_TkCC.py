from sikuli import *
import logging
import myTools
import reports_Compare

#---------------------------------------------------#
def Filter_SplitClients():
#---------------------------------------------------#

    logging.debug('- filter split clients')
    
    click("client_selection.png")
    time.sleep(1)
    click("add_filter.png")
    wait(Pattern("selected_items_will_be.png").similar(0.50),60)

    # switch to Excluded
    myTools.pressSHIFTTAB(1)
    time.sleep(1)
    type("e")

    # mark Beverly
    myTools.pressTAB(1)
    time.sleep(1)
    type("bev")
    time.sleep(1)
    type(Key.F4)
    time.sleep(2)

    # mark Peabody
    type("pea")
    time.sleep(1)
    type(Key.F4)
    time.sleep(2)

    # mark Saugus
    type("sau")
    time.sleep(1)
    type(Key.F4)
    time.sleep(2)

    # close
    type(Key.ENTER)

#---------------------------------------------------#
def Print_TkCC(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print tkcc")

    # name report file: ex: TkCC-03
    reportName = myTools.buildRepName("TkCC",pRepExt)
    logging.debug('Print_TkCC: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open report')
    type("r",KeyModifier.ALT)
    type("t")
    time.sleep(2)   
    type("timekeeper cont")    
    time.sleep(1)
    myTools.pressDOWN(1)
    time.sleep(1)
    type("o",KeyModifier.CTRL)
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

    # show client breakdown   
    myTools.pressTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # close dialog
    type(Key.ENTER)
    time.sleep(1)   

    logging.debug('- print report')

    # move to Print To and choose CSV
    myTools.pressTAB(2)
    type("c")
    time.sleep(1)

    if pReportMonth != 13:
        Filter_SplitClients()

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)