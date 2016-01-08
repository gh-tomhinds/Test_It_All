from sikuli import *
import shutil
import os
import logging
import myTools
import backup_Data

#---------------------------------------------------#
def fDelete_DataFolder():
#---------------------------------------------------#
    logging.debug('- fDeleteDataFolder')

    if Settings.tsDB == "PREM" and Settings.tsNetwork == "YES":
        # copy over registration database
        logging.debug('-- copy: ' + Settings.baseTSReg)
        logging.debug('-- to:   ' + Settings.tsSharedData)
        shutil.copy(Settings.baseTSReg,Settings.tsSharedData)
        
        # delete database
        if os.path.isfile(Settings.dbFolder):
            logging.debug('-- exists: ' + Settings.dbFolder)
            os.remove(Settings.dbFolder)            
        else:
            logging.debug('-- not exists: ' + Settings.dbFolder)

        popup("x")

    elif os.path.exists(Settings.dbFolder):
        logging.debug("-- Delete folder:     %s" % Settings.dbFolder)
        shutil.rmtree(Settings.dbFolder)
    else:
        logging.debug("-- Missing:           %s" % Settings.dbFolder)

#---------------------------------------------------#
def fStart_TS():
#---------------------------------------------------#
    logging.debug('- fStartTS')

    # show desktop
    type("d",KeyModifier.KEY_WIN)

    # start timeslips
    App.open(Settings.tsEXE)   
    time.sleep(3)
    
    logging.debug('-- wait until TS is open')

    if int(Settings.tsVersion) < 2016:
        wait("sage_timeslips.png",60)
      

#---------------------------------------------------#
def fCheckFor_Sample():
#---------------------------------------------------#
    logging.debug('- checkFor_Sample')

    time.sleep(1)     
    if exists("demo_database_msg.png"):
        logging.debug('-- Sample message exists')
        type(Key.ENTER)        

#---------------------------------------------------#
def fCheckFor_PEP():
#---------------------------------------------------#
    logging.debug('- checkFor_PEP')

    time.sleep(1)     
    if exists("pep.png"):
        logging.debug('-- PEP message exists')
        type(Key.ENTER)        

#---------------------------------------------------#
def fCheckFor_SPS():
#---------------------------------------------------#
    logging.debug('- checkFor_SPS')

    time.sleep(1)     
    if exists("sps.png"):
        logging.debug('-- SPS message exists')
        type(Key.ENTER)        

#---------------------------------------------------#
def fCheckFor_BillingDate():
#---------------------------------------------------#
    logging.debug('- checkFor_BillingDate')

    time.sleep(1)     
    if exists("bill_date.png"):
        logging.debug('-- billing date message exists')
        type(Key.ENTER)

#---------------------------------------------------#
def fStartTS_CreateNewDB():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("new db")
    
    logging.debug('StartTS_CreateNewDB')

    popup("make sure Timeslips is closed")

    fDelete_DataFolder()
    fStart_TS()
    fCheckFor_PEP()

# start the new db process
    logging.debug('- Check for database')
    time.sleep(3)

    if exists("database_not_found.png"):
        logging.debug('-- BDE db not found')
        type(Key.ENTER)
        time.sleep(2)
        type("n")
    elif exists("fb_encountered_error.png"):
        logging.debug('-- TS2016 db not found')
        type(Key.ENTER)
        time.sleep(2)
        type("n")
    else:
        logging.debug('-- db found')
        if exists("supervisor.png"):
            type(Key.ENTER)        
            time.sleep(1)
        fCheckFor_Sample()
        fCheckFor_PEP()
        fCheckFor_BillingDate()
        fCheckFor_SPS()
        time.sleep(1)

        # File > New > Database
        logging.debug('- create new database')
        type("f",KeyModifier.ALT)
        type("n")
        type("d")
        
    time.sleep(1)
    
# Empty database, press Next
    type("n",KeyModifier.ALT)
    time.sleep(1)

# For Premium, choose Local or Network, press Next
    if Settings.tsDB == "PREM" and Settings.tsNetwork == "NO":
        myTools.pressDOWN(1)
        type("n",KeyModifier.ALT)
    elif Settings.tsDB == "PREM" and Settings.tsNetwork == "YES":
        type("n",KeyModifier.ALT)

# new db path and settings

    logging.debug('- enter path')

    if Settings.tsDB == "PREM" and Settings.tsNetwork == "YES":
        type("SHARED-01")
    else:
        type(Settings.dbFolder)
        
    type(Key.ENTER)

# Firm name
    type("TS Handyman Services")
    type(Key.ENTER)    
    logging.debug('- db settings')

# Decimals
    time.sleep(1)     
    type(Key.ENTER)        

# set Fiscal month to July
    myTools.pressDOWN(6)
    type(Key.ENTER)

# starting invoice number    
    type("12345")
    type(Key.ENTER)

# bill with firm heading    
    myTools.pressDOWN(2)
# mark cover page
    type(Key.TAB,KeyModifier.SHIFT)
    type(Key.SPACE)
    time.sleep(1)        
    type(Key.ENTER)    
    
#    click("do_not_use_tal.png")    
    time.sleep(1)        
    type(Key.ENTER)

# unmark outlook
    type(Key.SPACE)
    time.sleep(1)        
    type(Key.ENTER)

# Ready to Create Your Database
    time.sleep(1)     
    type(Key.ENTER)

# Wait for db to be created    
    wait("finish.png",FOREVER)

# press Finish    
    type(Key.ENTER)
    time.sleep(1)

# wait for address info
    wait("address_info.png",60)

# Firm name/address
    type(Key.TAB)
    type("239 Western Avenue")
    myTools.pressTAB(2)
    type("Essex")
    type(Key.TAB)
    type("MA")
    type(Key.TAB)
    type("01929")
    type(Key.TAB)
    type("USA")
    type(Key.TAB)
    type("508-768-6100")
    time.sleep(1)

# project separator
    myTools.pressF6(6)
    time.sleep(1)
    type(".")

# close General settings
    type(Key.ENTER)    

# getting started
    logging.debug('- getting started wiz')
    wait("enter_your_name.png",FOREVER)
    type("Xander Yakuza Zork")
    type(Key.TAB)
    time.sleep(1)     
    type(Key.ENTER)    
    type("XanderZ")
    type(Key.TAB)
    type("XZork")
    type("f",KeyModifier.ALT)

# backup
    time.sleep(1)
    if exists("backup_database.png"):
        click("no_btn.png")
        time.sleep(1)
        type("n")

    fCheckFor_BillingDate()
    fCheckFor_SPS()
    fCheckFor_PEP()  
    
    myTools.sectionEndTimeStamp()
    backup_Data.fBackup_Checkpoint("new")
