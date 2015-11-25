from sikuli import *
import logging
import myTools
import email_Send

#---------------------------------------------------#
def fBackup_Data(pBkuName):
#---------------------------------------------------#

    logging.debug('Backup_Data: ' + pBkuName)
    
    # make sure timeslips has focus
    myTools.getFocus()

    type("f",KeyModifier.ALT)
    type("b")
    time.sleep(1)

    # no subfolders
    type("s",KeyModifier.ALT)
    time.sleep(1)

    # YES button
    type(Key.ENTER)
    time.sleep(1)

    # enter backup name
    type(pBkuName)
    time.sleep(1)

    # SAVE button
    type(Key.ENTER)
    time.sleep(1)
    
    if exists("replace_old_one.png"):
        type(Key.ENTER)
        logging.debug('- overwrite backup')
        
    wait("backup_successful.png",FOREVER)

    # OK button
    type(Key.ENTER)
    email_Send.fSend_Text(pBkuName)

#---------------------------------------------------#
def fBackup_Checkpoint(pCheckpointName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("backup checkpoint")
    logging.debug('Backup_Checkpoint: ' + pCheckpointName)

    # name backup file: ex: 2015-slips
    strBackupFile = Settings.tsVersion + "-" + pCheckpointName

    fBackup_Data(strBackupFile)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fBackup_BillData(pBillMonth,pAorB):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("backup billdata")
    logging.debug('Backup_Data: ' + str(pBillMonth))

    if Settings.tsVersion == "PREM":
        bkuExt = pAorB + ".tbu"
    else:
        bkuExt = pAorB + ".bku"

    # name backup file: ex: 2015-bill-03
    strBackupFile = myTools.bkuName(pBillMonth,"-bill-",bkuExt)
    fBackup_Data(strBackupFile)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fRestore_Backup(pBackupName):
#---------------------------------------------------#

    logging.debug('Restore_Backup: ' + str(pBackupName))
    
    # make sure timeslips has focus
    myTools.getFocus()

    type("f",KeyModifier.ALT)
    type("r")
    time.sleep(1)

    if Settings.tsVersion == "PREM":
        myTools.pressTAB(1)    

    type(pBackupName)
    time.sleep(1)

    # no backup
    type("u",KeyModifier.ALT)
    time.sleep(1)

    # OK button
    type(Key.ENTER)
    time.sleep(1)
        
    wait("restore_success.png",FOREVER)

    # OK button
    type(Key.ENTER)
    time.sleep(2)   