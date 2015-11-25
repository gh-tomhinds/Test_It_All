from sikuli import *
import logging
import myTools
from datetime import date
import reports_Compare

#---------------------------------------------------#
def fSet_BillDate(pMonth):
#---------------------------------------------------#

    if pMonth == 13:
        pMonth = 12     

    logging.debug('- change bill date: ' + str(pMonth) + "/27/" + Settings.dataYear)
    time.sleep(1)

    # make sure timeslips has focus
    myTools.getFocus()

    # open revise date
    type("b",KeyModifier.ALT)
    type("d")    
    time.sleep(2)

    # go to today
    type("t")

    #get to 01/01 of current year
    type(Key.HOME,KeyModifier.CTRL)        

    # get to 01/01 of the data year
    thisYear = date.today().year
    for prevYear in range(int(Settings.dataYear),thisYear):
        type(Key.PAGE_UP,KeyModifier.CTRL)        
    time.sleep(1)

    # get to 01/27 of the data year
    myTools.pressDOWN(4)
    myTools.pressLEFT(2)        

    for nextMonth in range(pMonth-1):
        type(Key.PAGE_DOWN)       
    time.sleep(1)
    
    type(Key.ENTER)
    time.sleep(1)  

#---------------------------------------------------#
def fRemove_Sort():
#---------------------------------------------------#

    time.sleep(1)
    logging.debug('- remove sort')
    
    type(Key.F6)
    time.sleep(1)

    click(Pattern("remove_sort-1.png").similar(0.80))
    time.sleep(1)
    
    type(Key.F6)
    time.sleep(1)

#---------------------------------------------------#
def fPrint_BillRun(pMonth):
#---------------------------------------------------#
    
    reportName = "Bill-" + myTools.padZero(pMonth) + "-" + Settings.tsVersion + ".txt"    
    logging.debug('fPrint_BillRun: ' + reportName)

    type("b",KeyModifier.CTRL)
    time.sleep(1)

    fRemove_Sort()
    myTools.enterSlipFilter(pMonth,"n")

    # print bills to text
    logging.debug('-- print')    
    type(Key.ENTER)    
    time.sleep(1)

    # fill in path and name; press ENTER
    type(Settings.repFolder + "\\" + reportName)
    time.sleep(1)
    type(Key.ENTER)    
    time.sleep(1)

    if exists("replace_msg.png"):
        type("y")

    # approve bills
    logging.debug('-- approve')    
    wait(Pattern("approve_bills-1.png").targetOffset(-100,-8),FOREVER)
    click(Pattern("approve_bills-1.png").targetOffset(-100,-8))
    type(Key.ENTER)
    time.sleep(3)

    if int(Settings.tsVersion) > 2015:
        wait("approving_bills.png",FOREVER)       
        while exists("approving_bills.png"):
            logging.debug('--- msg exists')
            time.sleep(2)
    else:
        waitVanish("approving_statusbar.png",FOREVER) 
    time.sleep(1)

    # compare the report with baseline
    reports_Compare.Compare_OneReport(reportName)

    # close report entry / don't save
    logging.debug('-- close report window')
    click("report_generate_bills.png")
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(2)
    type("n")    
    time.sleep(1)

#---------------------------------------------------#
def fPrint_Bills(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("bills" + str(pMonth))
    logging.debug('Print_Bills: ' + str(pMonth))
    
    fSet_BillDate(pMonth)
    fPrint_BillRun(pMonth)
    myTools.sectionEndTimeStamp()
