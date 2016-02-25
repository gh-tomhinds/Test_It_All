from sikuli import *

import logging
import myTools

#---------------------------------------------------#
def setup_BillTemplate():
#---------------------------------------------------#

    logging.debug('- edit bill template')
    type("o",KeyModifier.CTRL)
    time.sleep(1)
    type("Invoice: [Invoice Number], Balance: [New Balance]")
    time.sleep(1)
    
    myTools.pressTAB(1)
    type("a",KeyModifier.CTRL)
    time.sleep(1)
    
    type("Timekeeper: [Custom Timekeeper]")
    type(Key.ENTER)
    type("List: [Custom List]")
    type(Key.ENTER)
    type("Previous: [Previous Balance]")
    type(Key.ENTER)
    type("Fees: [Actual Fees - ITD + New]")
    type(Key.ENTER)
    type("Aged: Period 1: [Aged Period 1]")
    time.sleep(1)
    
    myTools.pressTAB(1)
    type(Key.ENTER)
    time.sleep(1)

#---------------------------------------------------#
def moveTo_NextTemplate():
#---------------------------------------------------#

    if int(Settings.tsVersion) < 2015:
        myTools.pressDOWN(1)
        time.sleep(1)
        type("o",KeyModifier.CTRL)
    else:
        myTools.pressF6(1)
        
    time.sleep(1)

#---------------------------------------------------#
def setup_StatementTemplate(pPeriod):
#---------------------------------------------------#

    logging.debug('- edit statement template: ' + pPeriod)

    type("Client: [Nickname 1] - Balance: [New Balance]")
    myTools.pressTAB(1)
    
    type("a",KeyModifier.CTRL)
    time.sleep(1)

    type("Period: " + pPeriod)
    type(Key.ENTER)    
    type("Timekeeper: [Custom Timekeeper]")
    type(Key.ENTER)
    type("List: [Custom List]")
    type(Key.ENTER)
    type("Previous: [Previous Balance]")
    type(Key.ENTER)
    type("Fees: [Actual Fees - ITD + New]")
    type(Key.ENTER)
    type("Aged: Period 1: [Aged Period 1]")
    type(Key.ENTER)    
    type("Oldest: [Oldest Balance Amount]")
    type(Key.ENTER)    
    type("Email: [Email Address]")
    time.sleep(1)

    if int(Settings.tsVersion) < 2015:
        myTools.pressTAB(1)
        type(Key.ENTER)
        time.sleep(1)

#---------------------------------------------------#
def setup_StatementTemplates():
#---------------------------------------------------#

    logging.debug('- edit statement template')

    myTools.pressF6(1)
    
    if int(Settings.tsVersion) < 2015:
        type("o",KeyModifier.CTRL)

    setup_StatementTemplate("Current")
    moveTo_NextTemplate()
    
    setup_StatementTemplate("Period1")
    moveTo_NextTemplate()
    
    setup_StatementTemplate("Period2")
    moveTo_NextTemplate()
    
    setup_StatementTemplate("Period3")
    moveTo_NextTemplate()
    
    setup_StatementTemplate("Period4")

#---------------------------------------------------#
def setup_ReprintTemplates():
#---------------------------------------------------#

    logging.debug('- edit reprint template')

    if int(Settings.tsVersion) < 2015:    
        type("3",KeyModifier.CTRL)  # use Ctrl+3 instead of F6; defect in ts2014
        type(Key.ENTER)
    else:
        type(Key.F6)
    time.sleep(1)
    
    type("Copy [Invoice Number] for [Invoice Balance]: [Invoice Status]")
    time.sleep(1)
    
    myTools.pressTAB(1)
    type("a",KeyModifier.CTRL)
    time.sleep(1)

    type("Timekeeper: [Custom Timekeeper]")
    type(Key.ENTER)
    type("Bill Date: [Bill Date]")
    type(Key.ENTER)
    type("New Charges: [New Charges]")
    type(Key.ENTER)
    type("InRefTo: [In Reference To]")
    type(Key.ENTER)
    type("Firm Name: [Firm Name]")
    time.sleep(1)    

    if int(Settings.tsVersion) < 2015:    
        myTools.pressTAB(1)
        type(Key.ENTER)
        time.sleep(1)


#---------------------------------------------------#
def setup_Templates():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("setup email templates")
    logging.debug('setup_Templates')

    myTools.getFocus()

    # open template list
    type("p",KeyModifier.ALT)
    type("l")
    time.sleep(1)
    
    setup_BillTemplate()
    setup_StatementTemplates()
    setup_ReprintTemplates()    
    
    if int(Settings.tsVersion) < 2015:
        myTools.pressTAB(2)
    else:    
        myTools.pressTAB(5) 
    type(Key.ENTER)        

    myTools.sectionEndTimeStamp()

