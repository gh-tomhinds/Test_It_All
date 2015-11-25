from sikuli import *
import logging
import myTools


#---------------------------------------------------#
def fAdd_ExpCustomField(name, downArrow):
#---------------------------------------------------#

    type(Key.ENTER)
    type(Key.TAB)
    type("a",KeyModifier.CTRL)

    for i in range(downArrow+1):
        type(Key.DOWN)

    type(Key.ENTER)
    type(Key.TAB,KeyModifier.SHIFT)

#---------------------------------------------------#
def fSetup_Template():
#---------------------------------------------------#

    logging.debug('- set up task template')
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)

# comma
    type("c")
    type(Key.ENTER)
    time.sleep(1)

# expense activity info
    type("e")
    type(Key.ENTER)

# choose source
    wait("put_data_into.png",FOREVER)
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    paste(Settings.expFile)

# choose fields
    logging.debug('- choose fields')        
    myTools.pressTAB(7)

# nn1
    myTools.pressDOWN(3)
    type(Key.ENTER)

# nn2
    myTools.pressDOWN(1)
    type(Key.ENTER)

# full
    myTools.pressDOWN(1)
    type(Key.ENTER)

# description
    myTools.pressDOWN(4)
    type(Key.ENTER) 

# billstatus
    myTools.pressDOWN(1)
    type(Key.ENTER)

# category
    myTools.pressDOWN(2)
    type(Key.ENTER) 
    
# quantity
    myTools.pressDOWN(1)
    type(Key.ENTER) 

# default level
    myTools.pressDOWN(1)
    type(Key.ENTER) 

# prices
    myTools.pressDOWN(1)
    type(Key.ENTER) 

    for i in range(1,20):
        myTools.pressDOWN(1)
        type(Key.ENTER) 
    time.sleep(1)

# custom
    type("c")
    time.sleep(1)        
    
    customFields = ['Date','Hours','CountyList','Money','Number','Percent','Text']
    for customField in customFields:
        fAdd_ExpCustomField(customField, customFields.index(customField))

# omit 1st record
    click("limit_records.png")
    type(Key.TAB)
    time.sleep(1)    
    type("2")

#---------------------------------------------------#
def fImport_Data():
#---------------------------------------------------#

# import data
    logging.debug('- import data')
    type(Key.F9)
    time.sleep(1)    
    type(Key.RIGHT)
    type(Key.ENTER)   
     
# verify data
    wait("number_records_imported.png",FOREVER)
    if exists(Pattern("failed.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

#---------------------------------------------------#
def fClose_TSImport():
#---------------------------------------------------#

# close tsimport
    logging.debug('- close TSImport')
    time.sleep(1)
    type(Key.RIGHT)
    type(Key.ENTER)   
    
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("x")
    time.sleep(1)
    type("n")

#---------------------------------------------------#
def fImport_Expenses():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("import expenses")
    logging.debug('Import_Expenses')

    myTools.startTSImport()
    fSetup_Template()   
    fImport_Data()
    fClose_TSImport()

    myTools.sectionEndTimeStamp()        