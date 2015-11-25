from sikuli import *
import logging
import myTools
import names_Init

#---------------------------------------------------#
def fCreate_OnePayment(pClient,pCliNum,pMonth,pAmount):
#---------------------------------------------------#

    logging.debug('- Create_OnePay: ' + str(pMonth) + "-" + pClient + " = " + str(pAmount))

    transferClients = ["East.Bridgewater","North.Adams","West.Boylston"]
    transferFundsClients = ["East.Brookfield","North.Andover","West.Bridgewater"]
    refundClients = ["Harvard","Harwich","Hatfield","Haverhill","Hawley"]   
    clearClients = transferClients + transferFundsClients + refundClients

    # new payment
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()
       
    # type
    type(Key.TAB)
       
    # source
    myTools.pressDOWN(pMonth-1)
    type(Key.TAB)
    time.sleep(1)
        
    # check number
    if pMonth == 1:
        type(str(pCliNum))
        type(Key.TAB)
        time.sleep(1)
            
    # skip card options
    if pMonth in (3,4,5,6,7,8):
        type(Key.TAB)
            
    # client
    myTools.enterClient(pClient)
        
    # date
    payDate = str(pMonth) + "/28/" + Settings.dataYear
    type(payDate)
    time.sleep(1)
    type(Key.TAB)
        
    # skip deposit slip
    if pMonth in (1,2):
        type(Key.TAB)
            
    # Amount
    type(str(pAmount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type(pClient + " - " + str(pCliNum) + " - " + payDate)
    type(Key.ENTER)
    time.sleep(1)

    # save
    type("s",KeyModifier.CTRL)
    myTools.checkForUnappliedAmount()
    myTools.waitForTransSave()    

    # clear applies and mark future invoice (this is for transfers in other scripts)
    if pClient in clearClients:
        logging.debug("==> CLEAR APPLIED")        
        click("clear_applies.png")
        time.sleep(1)
        click("apply_remaining_to_future.png")
        time.sleep(1)
        # save
        type("s",KeyModifier.CTRL)       
        myTools.checkForUnappliedAmount()
        myTools.waitForTransSave()    

#---------------------------------------------------#
def fCreate_PaymentsForMonth(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("payments" + str(pMonth))
    logging.debug('Create_PaymentsForMonth: ' + str(pMonth))

    allClients = names_Init.fInit_Clients()
    transferClients = ["East.Bridgewater","North.Adams","West.Boylston"]
    transferFundsClients = ["East.Brookfield","North.Andover","West.Bridgewater"]

    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()

    for oneClient in allClients:
        count += 1
        
        # always create payments for first 5 clients 
        # then create payments for 1 out of 5 next clients
        # always create payments for certain projects
        
        if (count in range(6)) or ((count + pMonth) % 5 == 0) or (oneClient in transferClients) or (oneClient in transferFundsClients):            
            payAmount = 100 + int(count) + pMonth/float(100)  # calc amount first, so we can log it
            fCreate_OnePayment(oneClient,count,pMonth,payAmount)
        else:
            logging.debug('-- skip: ' + str(pMonth) + "-" + oneClient)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()
    myTools.checkProcesses()    