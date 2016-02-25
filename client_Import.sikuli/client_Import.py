from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fAdd_CustomField(name, downArrow):
#---------------------------------------------------#

    type(Key.ENTER)
    type(Key.TAB)
    type("a",KeyModifier.CTRL)

    for i in range(downArrow+1):
        type(Key.DOWN)

    type(Key.ENTER)
    type(Key.TAB,KeyModifier.SHIFT)
    time.sleep(1)        

#---------------------------------------------------#
def fSetup_Template():
#---------------------------------------------------#

    logging.debug('- set up client template')
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)
    
    type("c")
    type(Key.ENTER)
    time.sleep(1)
    type("c")
    type(Key.ENTER)

#choose source
    wait("put_data_into.png",FOREVER)
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    paste(Settings.cliFile)

#choose fields
    myTools.pressTAB(7)

# nn1
    myTools.pressDOWN(3)
    type(Key.ENTER)

# nn2
    myTools.pressDOWN(1)
    type(Key.ENTER)

  # fullname
    myTools.pressDOWN(1)
    type(Key.ENTER)

  # add1
    myTools.pressDOWN(1)
    type(Key.ENTER)

  # city
    type("c")
    time.sleep(1)    
    type(Key.ENTER)
  # state
    myTools.pressDOWN(1)
    type(Key.ENTER)
  # zip
    myTools.pressDOWN(1)
    type(Key.ENTER)

  # address 1
    type("aaaa")
    time.sleep(1)
    type(Key.ENTER)

    # phone 1
    type("p")
    time.sleep(1)
    type(Key.ENTER)

    # in reference to
    type("i")
    time.sleep(1)    
    type(Key.ENTER)

    # notes
    myTools.pressDOWN(1)
    type(Key.ENTER)

# rate 01 - 05
    type("rrr")
    type(Key.ENTER)
    time.sleep(1)        
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    time.sleep(1)    

# rate 06 - 10
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    time.sleep(1)    

# rate 11 - 15
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    time.sleep(1)    

# rate 16 - 20
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    myTools.pressDOWN(1)
    type(Key.ENTER)
    time.sleep(1)    

    # custom
    type("c")
    time.sleep(1)    
    type("c")
    time.sleep(1)        
    
    customFields = ['Date','Hours','CountyList','Money','PopNumber','Percent','GovText','Timekeeper']
    for customField in customFields:
        fAdd_CustomField(customField, customFields.index(customField))

    # Email address
    type("e")
    time.sleep(1)    
    type(Key.ENTER)

# if ts2015 or later, address2 fields

    if int(Settings.tsVersion) > 2014:
        
        # Add1        
        type("oo")
        type(Key.ENTER)

        # City2       
        myTools.pressDOWN(4)
        type(Key.ENTER)

        # State2
        myTools.pressDOWN(1)
        type(Key.ENTER)

        # ZIP2
        myTools.pressDOWN(1)
        type(Key.ENTER)

        # Country2
        myTools.pressUP(3)
        type(Key.ENTER)    

# omit 1st record
    click("limit_records.png")
    type(Key.TAB)
    type("2")
    time.sleep(1)

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
def fImport_Clients():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("import clients")
    logging.debug('Import_Clients')

    myTools.startTSImport()
    fSetup_Template()
    fImport_Data()
    fClose_TSImport()

    myTools.sectionEndTimeStamp()