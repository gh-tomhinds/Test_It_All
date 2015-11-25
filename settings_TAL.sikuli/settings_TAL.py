from sikuli import *
import logging
import myTools
import backup_Data

#---------------------------------------------------#
def fSetup_ChooseTAL():
#---------------------------------------------------#

    type("a",KeyModifier.ALT)           # choose accounting link 
    time.sleep(1)
    type("c")
    time.sleep(1)
    
    myTools.pressUP(3)                  # TAL 
    myTools.pressTAB(1)                 # OK
    type(Key.ENTER)                     
    time.sleep(1)

#---------------------------------------------------#
def fSetup_LinkDetails():
#---------------------------------------------------#

    type("a",KeyModifier.ALT)           # set up accounting link
    time.sleep(1)
    type("s")
    time.sleep(1)

    myTools.pressF6(1)                  # method page
    time.sleep(1)
    type("a")                           # accrual
    
    myTools.pressTAB(3)                         # time WIP
    type(Key.SPACE)

    myTools.pressTAB(1)                         # expense WIP
    type(Key.SPACE)

    type(Key.ENTER)                     # OK
    time.sleep(1)

#---------------------------------------------------#
def fSetup_LinkDetailsUnmarkWIP():
#---------------------------------------------------#

    type("a",KeyModifier.ALT)           # set up accounting link
    time.sleep(1)
    type("s")
    time.sleep(1)

    myTools.pressF6(1)                  # method page
    time.sleep(1)
    
    myTools.pressTAB(3)                         # time WIP
    type(Key.SPACE)

    myTools.pressTAB(1)                         # expense WIP
    type(Key.SPACE)

    type(Key.ENTER)                     # OK
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts():
#---------------------------------------------------#

    type("a",KeyModifier.ALT)           # set up accounts
    time.sleep(1)
    type("a")
    time.sleep(1)

    fLink_Accounts_Cash()
    fLink_Accounts_Charges()
    fLink_Accounts_WUs()
    fLink_Accounts_WDs()   
    fLink_Accounts_TaxPay()
    fLink_Accounts_TaxRec()
    fLink_Accounts_AccRec()
    fLink_Accounts_Suspense()        
    fLink_Accounts_Credit()
    fLink_Accounts_Allowances()
    fLink_Accounts_WO()
    fLink_Accounts_Interest()
    fLink_Accounts_Refund()
    fLink_Accounts_CashEscrowIn()
    fLink_Accounts_CashEscrowOut()
    fLink_Accounts_ClientEscrow()    
    fLink_Accounts_WIP()
    fLink_Accounts_WIPOffset()
    fLink_Accounts_ProgBilling()    

    type(Key.ENTER)

#---------------------------------------------------#
def fLink_Accounts_Cash():
#---------------------------------------------------#

    myTools.pressSHIFTTAB(2)            # cash comp
    type(Key.DOWN,KeyModifier.CTRL)
    time.sleep(1)
    myTools.pressTAB(2)
    type("Cash-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(3)                # cash fees
    myTools.pressTAB(1)
    type("Cash-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # cash costs
    myTools.pressTAB(1)
    type("Cash-Fees")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)
    
#---------------------------------------------------#
def fLink_Accounts_Charges():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # charges comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(6)
    time.sleep(1)
    myTools.pressTAB(1)
    type("Charges-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # charges fees
    myTools.pressTAB(1)
    type("Charges-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # charges costs
    myTools.pressTAB(1)
    type("Charges-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_WUs():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # wu comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(9)
    time.sleep(1)
    myTools.pressTAB(1)
    type("WU-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # wu fees
    myTools.pressTAB(1)
    type("WU-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # wu costs
    myTools.pressTAB(1)
    type("WU-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_WDs():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # wd comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(12)
    time.sleep(1)
    myTools.pressTAB(1)
    type("WD-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # wd fees
    myTools.pressTAB(1)
    type("WD-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # wd costs
    myTools.pressTAB(1)
    type("WD-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_TaxPay():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # tp comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(15)
    time.sleep(1)
    myTools.pressTAB(1)
    type("TaxPay-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # tp fees
    myTools.pressTAB(1)
    type("TaxPay-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # tp costs
    myTools.pressTAB(1)
    type("TaxPay-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_TaxRec():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # tr comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(18)
    time.sleep(1)
    myTools.pressTAB(1)
    type("TaxRec-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # tr fees
    myTools.pressTAB(1)
    type("TaxRec-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # tr costs
    myTools.pressTAB(1)
    type("TaxRec-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_AccRec():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # ar comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(21)
    time.sleep(1)
    myTools.pressTAB(1)
    type("AR-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # ar fees
    myTools.pressTAB(1)
    type("AR-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # ar costs
    myTools.pressTAB(1)
    type("AR-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_Suspense():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # suspense comp
    myTools.pressTAB(1)
    type("Suspense")
    myTools.pressSHIFTTAB(1)

#---------------------------------------------------#
def fLink_Accounts_Credit():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # credit comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(25)
    time.sleep(1)
    myTools.pressTAB(1)
    type("Credit-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # credit fees
    myTools.pressTAB(1)
    type("Credit-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # credit costs
    myTools.pressTAB(1)
    type("Credit-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_Allowances():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # allowances comp
    myTools.pressTAB(1)
    type("Allowances")
    myTools.pressSHIFTTAB(1)

#---------------------------------------------------#
def fLink_Accounts_WO():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # WO comp
    myTools.pressTAB(1)
    type("WriteOff")
    myTools.pressSHIFTTAB(1)

#---------------------------------------------------#
def fLink_Accounts_Interest():
#---------------------------------------------------#

    myTools.pressDOWN(3)                # Interest comp
    myTools.pressTAB(1)
    type("Interest")
    myTools.pressSHIFTTAB(1)

#---------------------------------------------------#
def fLink_Accounts_Refund():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # Refund comp
    myTools.pressTAB(1)
    type("Refund")
    myTools.pressSHIFTTAB(1)

#---------------------------------------------------#
def fLink_Accounts_CashEscrowIn():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # cashescin comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(34)
    time.sleep(1)
    myTools.pressTAB(1)
    type("CashEscIn-Comp")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_CashEscrowOut():
#---------------------------------------------------#

    myTools.pressDOWN(3)                # cashescout comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(37)
    time.sleep(1)
    myTools.pressTAB(1)
    type("CashEscOut-Comp")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_ClientEscrow():
#---------------------------------------------------#

    myTools.pressDOWN(3)                # clientescrow comp
    myTools.pressTAB(1)
    type("ClientEscrow-Comp")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_WIP():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # wip comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(41)
    time.sleep(1)
    myTools.pressTAB(1)
    type("WIP-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # wip fees
    myTools.pressTAB(1)
    type("WIP-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # wip costs
    myTools.pressTAB(1)
    type("WIP-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_WIPOffset():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # wipo comp
    type(Key.DOWN,KeyModifier.CTRL)
    myTools.pressDOWN(44)
    time.sleep(1)
    myTools.pressTAB(1)
    type("WIPOffset-Comp")
    myTools.pressSHIFTTAB(1)

    myTools.pressDOWN(1)                # wipo fees
    myTools.pressTAB(1)
    type("WIPOffset-Fees")
    myTools.pressSHIFTTAB(1)
    
    myTools.pressDOWN(1)                # wipo costs
    myTools.pressTAB(1)
    type("WIPOffset-Costs")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fLink_Accounts_ProgBilling():
#---------------------------------------------------#

    myTools.pressDOWN(1)                # progbill comp
    myTools.pressTAB(1)
    type("ProgBilling-Comp")
    myTools.pressSHIFTTAB(1)
    
    time.sleep(1)

#---------------------------------------------------#
def fSetup_TAL():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup tal")
    logging.debug('fSetup_TAL')

    # make sure timeslips has focus
    myTools.getFocus()

    fSetup_ChooseTAL()
    fSetup_LinkDetails()
    fLink_Accounts()
    fSetup_LinkDetailsUnmarkWIP()

    myTools.sectionEndTimeStamp()

    backup_Data.fBackup_Checkpoint("TAL")    