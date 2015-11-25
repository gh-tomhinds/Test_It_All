from sikuli import *
import logging
import myTools
import backup_Data

#---------------------------------------------------#
def fSetup_Primary(pPrimaryClient):
#---------------------------------------------------#

    # new primary
    type("n",KeyModifier.ALT)
    time.sleep(1)
    
    # beverly
    type(pPrimaryClient)
    
    # split bill info
    myTools.pressTAB(1)    
    type(pPrimaryClient)
    
    # recurring
    myTools.pressTAB(2)
    type(Key.SPACE)

    # OK
    myTools.pressTAB(3)
    type(Key.SPACE)
    time.sleep(1)

#---------------------------------------------------#
def fSetup_Secondary(pSecondaryClient,pTimePercentage):
#---------------------------------------------------#

    type(Key.SPACE)
        
    type(pSecondaryClient)

    # percentages
    myTools.pressTAB(2)
    type(str(pTimePercentage))
    myTools.pressTAB(1)
    type(str(pTimePercentage+5))

    # ok
    myTools.pressTAB(3)
    type(Key.SPACE)
    time.sleep(1)

#---------------------------------------------------#
def fSetup_SplitBills():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup split")
    logging.debug('- set up split bills')

    myTools.getFocus()

    # open split billing rule list
    type("b",KeyModifier.ALT)
    time.sleep(1)
    type("i")
    time.sleep(1)

    fSetup_Primary("Beverly")

    # new secondary
    myTools.pressTAB(7)   
    fSetup_Secondary("Peabody",15)
    fSetup_Secondary("Saugus",20)

    # done
    myTools.pressTAB(4)
    type(Key.SPACE)

    myTools.sectionEndTimeStamp()
    backup_Data.fBackup_Checkpoint("split")    