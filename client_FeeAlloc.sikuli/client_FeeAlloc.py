from sikuli import *
import logging
import myTools


#---------------------------------------------------#
def fSetup_CustomFields():
#---------------------------------------------------#

    logging.debug('- Set Up Custom Fields')
    type("p", KeyModifier.ALT)
    type("c")
    time.sleep(1)    
    type(Key.TAB)

    for customName in ["Originating","Responsible","Other"]:                

        type("n", KeyModifier.ALT)
        type(Key.UP)
        type(Key.ENTER)
        time.sleep(1)
    
        type(customName)
        myTools.pressTAB(2)
        type(Key.DOWN)            
        type(Key.ENTER)    

    myTools.pressTAB(7)
    type(Key.ENTER)
    time.sleep(3) # extra time to restructure table

#---------------------------------------------------#
def fExport_Timekeepers():
#---------------------------------------------------#

    logging.debug('- Export Timekeepers')

    # open client info
    type("i", KeyModifier.CTRL)
    time.sleep(1)    
    type(Key.ENTER)
    time.sleep(1)   

    if int(Settings.tsVersion) > 2014:    
        myTools.pressF6(4)
        myTools.pressTAB(2)        
    else:
        type(Key.F6)
        myTools.pressTAB(3)
        type(Key.RIGHT)

    # enter custom field values
    type(Key.TAB)
    type("t")
    type(Key.TAB)
    type("20")
    
    type(Key.TAB)
    type("c")
    type(Key.TAB)
    type("10")

    type(Key.TAB)
    type("j")
    type(Key.TAB)
    type("5")

    type("s", KeyModifier.CTRL)
    
    wait("export_btn.png")
    click("export_btn.png")
    time.sleep(1)

    if int(Settings.tsVersion) > 2014:    
        type(Key.DOWN)
        # sometimes a keypress is needed to make INS work
    else:    
        type(Key.DELETE)
        myTools.pressDOWN(8)
        type(Key.DOWN, KeyModifier.SHIFT)
        type(Key.DOWN, KeyModifier.SHIFT)    
        type(Key.F4)
    time.sleep(1)

    type(Key.TAB)        
    type(Key.INSERT)
    type(Key.TAB)    
    
    type(Key.ENTER)    
    time.sleep(1)
    type(Key.ENTER)    

    myTools.waitForExportSuccess()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def fSetup_FeeAlloc():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup fee alloc")
    logging.debug('Set Up Fee Allocation')

    # make sure timeslips has focus
    myTools.getFocus()

    fSetup_CustomFields()
    fExport_Timekeepers()
    
    myTools.sectionEndTimeStamp()