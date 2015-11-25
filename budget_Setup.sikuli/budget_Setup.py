from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fBudgetDetails(pStartMonth,pEndMonth,pDay):
#---------------------------------------------------#

    logging.debug('-- budget details: ' + str(pStartMonth))

    # new
    type("n", KeyModifier.CTRL)
    time.sleep(1)    

    # skip date fields if pMonth < 13 (ex: for client)
    if pStartMonth < 13:        

        # start date
        startDate = str(pStartMonth) + "/1/" + Settings.dataYear
        type(startDate)
        myTools.pressTAB(1)

        # end date
        endDate = str(pEndMonth) + "/" + str(pDay) + "/" + Settings.dataYear
        type(endDate)
        myTools.pressTAB(1)
        time.sleep(1)    
    else:
        myTools.pressTAB(2)

    # hours total
    hoursTotal = 5 + pEndMonth/float(100)
    type(str(hoursTotal))
    type(Key.TAB)

    # fees total
    feesTotal = 100 + pEndMonth/float(100)
    type(str(feesTotal))
    type(Key.TAB)

    # costs total
    costsTotal = 15 + pEndMonth/float(100)
    type(str(costsTotal))
    type(Key.TAB)

    # hours billable
    hoursBillable = 4 + pEndMonth/float(100)
    type(str(hoursBillable))
    type(Key.TAB)

    # fees billable
    feesBillable = 90 + pEndMonth/float(100)
    type(str(feesBillable))
    type(Key.TAB)

    # costs billable
    costsBillable = 13 + pEndMonth/float(100)
    type(str(costsBillable))
    type(Key.TAB)

    # hours unbillable
    hoursUnbillable = 1 + pEndMonth/float(100)
    type(str(hoursUnbillable))
    type(Key.TAB)

    # fees unbillable
    feesUnbillable = 10 + pEndMonth/float(100)
    type(str(feesUnbillable))
    type(Key.TAB)

    # costs unbillable
    costsUnbillable = 2 + pEndMonth/float(100)
    type(str(costsUnbillable))
    type(Key.TAB)

    # fees billed
    feesBilled = 50 + pEndMonth/float(100)
    type(str(feesBilled))
    type(Key.TAB)

    # costs billed
    costsBilled = 20 + pEndMonth/float(100)
    type(str(costsBilled))    
    type(Key.TAB)

    # ENTER
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

#---------------------------------------------------#
def fTimekeeperBudget():
#---------------------------------------------------#

    logging.debug('- Timekeeper budget')
   
    # switch to timekeeper tab
    type(Key.F6)
    time.sleep(1)    

    #switch to Tom
    myTools.pressSHIFTTAB(1)
    time.sleep(1)    
    type("tomh")

    count = 0
    for endDay in [31,28,31,30,31,30,31,31,30,31,30,31]:
        count += 1        
        fBudgetDetails(count,count,endDay)

#---------------------------------------------------#
def fClientBudget():
#---------------------------------------------------#

    logging.debug('- Client budget')
   
    # switch to client tab
    myTools.pressSHIFTF6(1)
    time.sleep(1)    

    # budget for abington
    # use numbers over 12 to keep dates open
    fBudgetDetails(13,13,13)

    # budget for yarmouth
    time.sleep(1)
    type(Key.END)
    time.sleep(1)    
    # use numbers over 12 to keep dates open
    fBudgetDetails(14,14,14)

#---------------------------------------------------#
def fFirmBudget():
#---------------------------------------------------#

    logging.debug('- Firm budget')
   
    # switch to firm tab
    myTools.pressSHIFTF6(1)
    time.sleep(1)    

    # budget for firm
    # firstmonth, lastmonth, lastday
    fBudgetDetails(1,12,31)

#---------------------------------------------------#
def fBudget_Setup():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("budgets")
    logging.debug('budgets')
    
    myTools.getFocus()

    # open budget setup
    type("n", KeyModifier.ALT)
    type("b")
    time.sleep(1)    

    fTimekeeperBudget()
    fClientBudget()
    fFirmBudget()

    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()