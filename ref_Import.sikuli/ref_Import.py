from sikuli import *
import logging
import myTools


#---------------------------------------------------#
def fSetup_Template():
#---------------------------------------------------#

    logging.debug('- set up ref template')
    time.sleep(1)
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)

# comma
    type("c")
    type(Key.ENTER)
    time.sleep(1)

# ref info
    myTools.pressDOWN(5)
    type(Key.ENTER)

# choose source
    wait("put_data_into.png",FOREVER)
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    paste(Settings.refFile)

#choose fields
    logging.debug('- choose fields')        
    myTools.pressTAB(6)

# nn1
    myTools.pressDOWN(1)
    type(Key.ENTER)
    
# nn2
    myTools.pressDOWN(1)
    type(Key.ENTER) 
    
#CliNN1
    myTools.pressDOWN(1)
    type(Key.ENTER) 

# omit 1st record
    click("limit_records.png")
    type(Key.TAB)
    time.sleep(1)    
    type("2")

#---------------------------------------------------#
def fImport_Data():
#---------------------------------------------------#

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
def fImport_Refs():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("import refs")
    logging.debug('Import_Refs')

    myTools.startTSImport()
    fSetup_Template()   
    fImport_Data()
    fClose_TSImport()

    myTools.sectionEndTimeStamp()