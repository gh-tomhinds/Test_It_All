from sikuli import *

import client_Create
import task_Create
import expense_Create

import timekeeper_Import
import timekeeper_Edit

import client_Import
import client_Edit
import client_FundsEdit

import task_Import
import task_Edit
import expense_Import
import expense_Edit

import ref_Create
import ref_Import

import client_FeeAlloc
import expense_Markup
import taxes_Setup
import client_Hold
import client_PayDistrib
import client_FundsNew
import budget_Setup

import backup_Data

import report_FundsAccountList
import report_TimekeeperInfo
import report_ClientInfo

#---------------------------------------------------#
def fCreateImportEdit_Names():
#---------------------------------------------------#
 
#    editDefaultClient.Edit_DefaultClient()

#---------------------------------------------------#

    client_Create.fCreate_Client("ZZZlient","Client001","9999 - First Client","In Ref to","Client Notes")
    task_Create.fCreate_Task()
    expense_Create.fCreate_Expense()
    
    timekeeper_Import.fImport_Timekeepers()
    timekeeper_Edit.fEdit_Timekeeper()
    
    client_Import.fImport_Clients()
    backup_Data.fBackup_Checkpoint("clients-import")    
    client_Edit.fEdit_Client()    
    client_FundsEdit.fEdit_ClientFunds()
    backup_Data.fBackup_Checkpoint("clients")
    report_FundsAccountList.fPrint_Funds("FundsSettings-01" + ".csv")
    
    client_Hold.fSetup_ClientHold()
    client_FeeAlloc.fSetup_FeeAlloc()

    task_Import.fImport_Tasks()
    task_Edit.fEdit_Task()
    expense_Import.fImport_Expenses()
    expense_Edit.fEdit_Expense()
    backup_Data.fBackup_Checkpoint("activities")    

    expense_Markup.fSetup_ExpMarkups()
    backup_Data.fBackup_Checkpoint("markups")    

    taxes_Setup.fSetup_Taxes()
    backup_Data.fBackup_Checkpoint("taxes")

    client_PayDistrib.fSetup_PayDist()
    backup_Data.fBackup_Checkpoint("pay-dist")

    client_FundsNew.fFundsAccouts_Setup()
    backup_Data.fBackup_Checkpoint("fundsaccts")

    ref_Create.fCreate_Refs()
    ref_Import.fImport_Refs()
    backup_Data.fBackup_Checkpoint("refs")

    budget_Setup.fBudget_Setup()

#    report_TimekeeperInfo.fPrint_TimekeeperInfo("Timekeepers-01" + Settings.tsVersion + ".csv")
#    report_ClientInfo.fPrint_ClientInfo("Clients-01-" + Settings.tsVersion + ".csv")

    backup_Data.fBackup_Checkpoint("names")
