from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreate_Jurisdictions():
#---------------------------------------------------#

    logging.debug('- Create_Jurisdiction')

    # move to jurisdictions
    myTools.pressF6(2)
    time.sleep(1)

    # new jurisdication for Zone 1
    logging.debug('-- new jurisdictions')  
    type("n",KeyModifier.ALT)
    time.sleep(1)
    type("o")
    myTools.pressTAB(1)
    type("Zone1")
    myTools.pressTAB(1)
    type("One")
    time.sleep(1)
    
    # OK
    type(Key.ENTER)

#---------------------------------------------------#
def fCreate_RateRules():
#---------------------------------------------------#
    logging.debug('- Create_RateRules')

    # switch to rate rules page
    myTools.pressSHIFTF6(1)
    time.sleep(1)

    fCreate_TimeOnly_RateRule()
    fCreate_ExpenseOnly_RateRule()
#    fCreate_Compound_RateRules()
#    fCreate_Minimum_RateRule()
#    fCreate_Maximum_RateRule()

#---------------------------------------------------#
def fCreate_TimeOnly_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_TimeOnly_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Time Only")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4")
    time.sleep(1)
    # options   
    myTools.pressTAB(5)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # OK
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)   

#---------------------------------------------------#
def fCreate_ExpenseOnly_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_ExpenseOnly_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Expense Only")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4.25")
    time.sleep(1)
    # type
    myTools.pressTAB(1)
    type("e")
    time.sleep(1)
    
    # options
    if int(Settings.tsVersion) > 2015:
        myTools.pressTAB(4)
    else:
        myTools.pressTAB(5)
    type(Key.SPACE)
    time.sleep(1)
    
    myTools.pressTAB(2)
    type(Key.SPACE)
    time.sleep(1)
    
    # OK    
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def fCreate_Compound_RateRules():
#---------------------------------------------------#
    logging.debug('- Create_Compound_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Compound2")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("3")
    myTools.pressTAB(5)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

    # new rule
    type("n",KeyModifier.ALT)
    type("Compound1")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("3.5")
    # Type
    myTools.pressTAB(1)
    myTools.pressDOWN(2)  
    # compound
    myTools.pressTAB(2)    
    type("com")
    # options
    myTools.pressTAB(1)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def fCreate_Minimum_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_Minimum_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Minimum")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4.5")
    # minimum
    myTools.pressTAB(4)
    myTools.pressDOWN(1)
    time.sleep(1)
    # threshold
    myTools.pressTAB(1)
    type("1000")
    # options
    myTools.pressTAB(2)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def fCreate_Maximum_RateRule():
#---------------------------------------------------#
    logging.debug('- Create_Maximum_RateRule')

    # new rule
    type("n",KeyModifier.ALT)
    type("Maximum")
    myTools.pressTAB(1)
    type("z")
    time.sleep(1)
    # rate
    myTools.pressTAB(2)
    type("4.5")
    # maximum
    myTools.pressTAB(4)
    myTools.pressDOWN(2)
    time.sleep(1)
    # threshold
    myTools.pressTAB(1)
    type("1000")   
    # options
    myTools.pressTAB(2)
    type(Key.SPACE)
    myTools.pressTAB(2)
    type(Key.SPACE)
    # save
    myTools.pressTAB(1)
    type(Key.SPACE)
    time.sleep(1)
    # export to all
    type(Key.INSERT)
    myTools.pressTAB(1)
    type(Key.SPACE)    
    time.sleep(1)

#---------------------------------------------------#
def fCreate_TaxProfile():
#---------------------------------------------------#
    logging.debug('- Create_TaxProfile')

    type("1",KeyModifier.CTRL)
    
    # new profile    
    type("n",KeyModifier.ALT)   
    time.sleep(1)
    
    type("MyTaxes")
    time.sleep(1)

    # Time rule    
    myTools.pressTAB(1)
    type("t")
    
    # Expense rule
    myTools.pressTAB(1)
    type("e")
    
#    # Compound rule
#    myTools.pressTAB(1)
#    type("com")
    
#    # Minimum rule    
#    myTools.pressTAB(1)
#    type("min")

#    # Maximum rule
#    myTools.pressTAB(1)
#    type("max")

    time.sleep(1)

    # OK
    type(Key.ENTER)    

    # DONE
    myTools.pressSHIFTTAB(2)
    type(Key.ENTER)

#---------------------------------------------------#
def fChange_TaxRule():
#---------------------------------------------------#
    logging.debug('- Change_TaxRule')

    logging.debug('-- open Taxes')
    type("p",KeyModifier.ALT)   
    type("t")
    time.sleep(2)

    logging.debug('-- open GA tax rule')
    type(Key.F6)
    type("g")
    type(Key.ENTER)
    time.sleep(1)

    logging.debug('-- change rate')
    myTools.pressTAB(3)
    type("7.25")
    type(Key.TAB)
    type(Key.END)
    time.sleep(1)

    logging.debug('-- change settings')
    type("s",KeyModifier.ALT)
    type("i",KeyModifier.ALT)
    type(Key.ENTER)
    click("done_btn.png")

#---------------------------------------------------#
def fExport_ClientSettings():
#---------------------------------------------------#
    
    logging.debug('-- export client settings')
    click("export_btn.png")    
    
    # clear all and highlight tax profile
    type(Key.DELETE)
    time.sleep(1)
    type(Key.UP)
    type(Key.DOWN)

    # mark tax profile
    type(Key.F4)
    type(Key.TAB)

    # mark all clients
    type(Key.INSERT)
    time.sleep(1)

    # click export
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

    myTools.waitForExportSuccess()   

#---------------------------------------------------#
def fExport_TemplateSettings():
#---------------------------------------------------#
    
    logging.debug('-- export template settings')
    click("export_btn.png")
    
    # clear all and highlight tax profile
    type(Key.DELETE)
    time.sleep(1)
    type(Key.UP)
    type(Key.DOWN)

    # mark tax profile
    type(Key.F4)

    # switch to Templates
    
    if Settings.tsVersion > "2014":
        myTools.pressSHIFTTAB(1)
        time.sleep(1)
        type("t")
        time.sleep(1)
        myTools.pressTAB(1)
    else:        
        click("templates.png")    

    # mark Default
    type(Key.TAB)    
    type(Key.F4)
    time.sleep(1)

    # click export
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

    myTools.waitForExportSuccess()   

#---------------------------------------------------#
def fChange_ClientSettings():
#---------------------------------------------------#

    logging.debug('- Change_ClientSettings')
    myTools.getFocus()
    
    logging.debug('-- change a client')
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(Key.ENTER)
    time.sleep(1)

    myTools.pressF6(4)
    if Settings.tsVersion > "2014":
        myTools.pressF6(3)       
    time.sleep(1)
    
    myTools.pressTAB(3)   
    time.sleep(1)
    type("my")

    logging.debug('-- save client')
    type("s",KeyModifier.CTRL)

    fExport_ClientSettings()
    fExport_TemplateSettings()

    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    type(Key.F4,KeyModifier.CTRL)

#---------------------------------------------------#
def fSetup_Taxes():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup taxes")

    logging.debug('Setup_Taxes')
    
    # make sure timeslips has focus
    myTools.getFocus()
    time.sleep(1)

    # open taxes UI
    logging.debug('-- open Taxes')
    type("p",KeyModifier.ALT)   
    type("t")
    time.sleep(2)

    fCreate_Jurisdictions()
    fCreate_RateRules()
    fCreate_TaxProfile()
    fChange_ClientSettings()

    myTools.sectionEndTimeStamp()