from sikuli import *
import logging
import myTools
import names_Init

#---------------------------------------------------#
def fCreate_OneCredit(pClient,pCliNum,pMonth,pAmount):
#---------------------------------------------------#

    logging.debug('- Create_OneCred: ' + str(pMonth) + "-" + pClient + " = " + str(pAmount))

    # new payment
    type("n",KeyModifier.CTRL)
    myTools.waitForTransEntry()
    
    # type = credit
    type(Key.HOME)
    myTools.pressDOWN(1)
    type(Key.TAB)     
    time.sleep(1)        
        
    # client
    myTools.enterClient(pClient)
        
    # date
    credDate = str(pMonth) + "/28/" + Settings.dataYear
    type(credDate)
    time.sleep(1)
    type(Key.TAB)       
            
    # Amount
    type(str(pAmount))
    type(Key.TAB)
        
    # Description
    type("a",KeyModifier.CTRL)
    type(pClient + " - " + str(pCliNum) + " - " + credDate)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.TAB)

    # Invoice list; go to last entry
    type(Key.END, KeyModifier.CTRL)
    time.sleep(1)    
    click("apply_one_button.png")
    time.sleep(1) 

    # save
    type("s",KeyModifier.CTRL)
    myTools.checkForUnappliedAmount()
    myTools.waitForTransSave()    

#---------------------------------------------------#
def fCreate_CreditsForMonth(pMonth):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("credits" + str(pMonth))
    logging.debug('Create_CreditsForMonth: ' + str(pMonth))

    allClients = names_Init.fInit_Clients()
    count = 0

    myTools.getFocus()

    # open a/r tran list
    type("t",KeyModifier.CTRL)
    myTools.waitForTransList()
    
    for oneClient in allClients:
        count += 1
        
        # always create credits for first 5 clients 
        # then create credits for 1 out of 9 next clients
        
        if (count in range(6)) or ((count + pMonth) % 9 == 0):
            creditAmount = pMonth + pMonth/float(100)            
            fCreate_OneCredit(oneClient,count,pMonth,creditAmount)
        else:
            logging.debug('-- skip: ' + str(pMonth) + "-" + oneClient)           

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)
    
    myTools.sectionEndTimeStamp()
    myTools.checkProcesses()