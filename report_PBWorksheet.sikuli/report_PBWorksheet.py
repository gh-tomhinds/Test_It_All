from sikuli import *
import logging
import myTools
import reports_Compare
import backup_Data

#---------------------------------------------------#
def fSetup_PreBill():
#---------------------------------------------------#

    logging.debug('- set up prebill')
    
    myTools.getFocus()
    logging.debug('- open worksheet')
    type("b",KeyModifier.ALT)
    type("p")

    myTools.removeDateAndTime()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type("y")
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def setupCustomFilter():
#---------------------------------------------------#

    # this is used in fPrint_PreBill_2    

    logging.debug('- enterCustomFilter')    

    wait("slip_trans_date.png",60)                
    time.sleep(1)                
    
    click("slip_trans_date.png")
    time.sleep(1)

    # switch to the client group
    myTools.pressSHIFTTAB(1)
    type("c")
    time.sleep(1)

    # choose Client List
    myTools.pressTAB(1)
    myTools.pressDOWN(7)
    click("add_filter.png")
    time.sleep(1)

    # mark All
    type(Key.INSERT)
    time.sleep(1)

    # remove Franklin
    myTools.pressDOWN(5)
    type(Key.F4,KeyModifier.SHIFT)

    # press OK
    myTools.pressTAB(1)
    type(Key.ENTER)
    time.sleep(1)
                                
#---------------------------------------------------#
def setupCustomSort():
#---------------------------------------------------#

    # this is used in fPrint_PreBill_2

    # switch to the Sort page
    myTools.pressF6(1)
    time.sleep(1)

    # remove sorts
    myTools.clickRemoveAll()

    # switch to the activity group
    myTools.pressSHIFTTAB(1)
    type("a")
    time.sleep(1)

    # choose Activity List
    myTools.pressTAB(1)
    myTools.pressDOWN(7)
    click("add_filter.png")
    time.sleep(1)
                

#---------------------------------------------------#
def fPrint_PreBill_1(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print PreBill 1")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("PreBill",pRepExt)
    logging.debug('Print_PreBill: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open worksheet')
    type("b",KeyModifier.ALT)
    type("p")    
    time.sleep(1)
    
    logging.debug('- set up worksheet')
    # Options
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # Default
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # OK
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # choose text
    myTools.pressTAB(2)
    type("t")
    time.sleep(1)

    myTools.enterSlipFilter(pReportMonth,"n")

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)

#---------------------------------------------------#
def fPrint_PreBill_2(pReportMonth,pRepExt):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("print PreBill 2")

    # name report file: ex: PreBill-03
    reportName = myTools.buildRepName("PreBill2",pRepExt)
    logging.debug('Print_PreBill: ' + reportName)

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open worksheet')
    type("b",KeyModifier.ALT)
    type("p")    
    time.sleep(1)
    
    logging.debug('- set up worksheet')
    # Options
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)

    # Default
    myTools.pressSHIFTTAB(4)
    type(Key.SPACE)
    time.sleep(1)
    
    # Exclude paid-in-full
    myTools.pressTAB(8)
    type(Key.SPACE)
    time.sleep(1)

    # Include bills with balances but no activity
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Include bills on Full Bill hold
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Exclude payments with unapplied
    myTools.pressTAB(2)
    type(Key.SPACE)
    time.sleep(1)

    # Release slips on hold
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Hide full address
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Hide reference
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Show client notes
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Show custom fields
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Don't itemize slips
    myTools.pressTAB(3)
    type(Key.SPACE)
    time.sleep(1)

    # Hide aged balances
    myTools.pressTAB(5)
    type(Key.SPACE)
    time.sleep(1)

    # Don't itemize a/r transactions
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Show client funds
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)

    # Show summary table
    myTools.pressTAB(3)
    type(Key.SPACE)
    time.sleep(1)   

    # OK
    type(Key.ENTER)
    time.sleep(1)    

    # choose text
    myTools.pressTAB(2)
    type("t")
    time.sleep(1)

    # filters
    setupCustomFilter()

    # sort
    setupCustomSort()

    # print the report
    type(Key.ENTER)    
    time.sleep(1)

    myTools.finishReport(reportName)

    # RESTORE
    buName = Settings.tsVersion + "-bill-" + str(myTools.padZero(pReportMonth)) + AorB
    backup_Data.fRestore_Backup(buName)                
    