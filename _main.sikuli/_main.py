""" _main: This is the driver for all scripts
    These scripts rely on the following:
    1) Windows Explorer windows opens on primary monitor 
    2) Timeslips BDE is installed below C:\Program Files (x86)    
    3) Timeslips Premium Network installed below C:\TSSHARE 
    4) Timeslips install folder is in format: Timeslips 2016
""" 

# import my sikuli scripts
import myTools

import _global_Settings
import db_New
import settings_Prefs

import names_Create

import settings_Categories
import settings_CustomFields
import settings_TAL

import slips_Create
import slips_CreateManually

import bill_Split
import bill_MonthlyCycle

import ba__Main
import ba__Common

import bill_BillFields

import backup_Data
import calendar_Terms
import calendar_Entries

import email_Send
import reports_PostBill

import reports_CreateReports
import email_Setup

##############################################################
# setup stuff - never comment this out
##############################################################

if __name__ == '__main__':
    myTools.setupLog()
    myTools.startTimeStamp()
    _global_Settings.fSetup_Environment()

##############################################################
# this section contains 1-off tests
##############################################################

#reports_PostBill.fPrint_PostbillReports(1,"b") # use for quick test of reports
#type("f",KeyModifier.ALT)
#type("x")

##############################################################
# this section contains 1-off tests
##############################################################

"""
for theMonth in range(12):
    realMonth = theMonth + 1
    for AorB in ("a","b"):
        buName = Settings.tsVersion + "-bill-" + str(myTools.padZero(realMonth)) + AorB
        backup_Data.fRestore_Backup(buName)
        reports_PostBill.fPrint_PostbillReports(realMonth,AorB) # use for quick test of reports

import trans_PostBill
trans_PostBill.fEnter_Transactions(12)
"""

##############################################################
# the real stuff starts below
##############################################################

if __name__ == '__main__':    # this stops pydoc import from executing    

    db_New.fStartTS_CreateNewDB()
    settings_Prefs.fTweak_Prefs()

    settings_Categories.fCreate_Categories()
    settings_CustomFields.fCreate_CustomFields()
    
    names_Create.fCreateImportEdit_Names()
    
    slips_Create.Create_Slips(10,10) # pass in numTimeSlips and numExpSlips to create manually; should be 10, 10
    slips_CreateManually.Create_Slips(702,702) # pass in numTimeSlips and numExpSlips to create manually; should be 10, 10
    
    settings_TAL.fSetup_TAL()
    bill_Split.fSetup_SplitBills()
    email_Setup.setup_Templates()
    
    reports_CreateReports.create_Layouts()
    bill_MonthlyCycle.fRun_BillCycle(1,2) # pass in start and end+1 month; should by 1, 13 unless starting in mid stream
    
    ba__Common.fRestore_BABackup()
    ba__Common.fSetup_BADefaultLayout()
    ba__Main.fReview_Arrangements()
    
    bill_BillFields.fBill_BillFields()
    
    calendar_Terms.fSetup_CalTerms()
    calendar_Entries.fCalendar_Entries()
    
    myTools.checkProcesses()
    myTools.endTimeStamp()

    exit()
 