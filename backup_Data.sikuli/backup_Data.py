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

    wait("make_backup.png",60)

    # no subfolders
    if Settings.tsDB == "BDE":
        logging.debug('- no subfolders')
        type("s",KeyModifier.ALT)
    time.sleep(1)

    # YES button
    type(Key.ENTER)
    time.sleep(1)

    if Settings.tsDB == "PREM" and exists("back_up_to_a_file.png"):
        click("back_up_to_a_file.png")
        time.sleep(1)
        myTools.pressTAB(1)      

    # enter backup name
    wait("save_in.png",60)
    
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

    myTools.checkProcesses()
    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fBackup_BillData(pBillMonth,pAorB):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("backup billdata")
    logging.debug('Backup_Data: ' + str(pBillMonth))

    if Settings.tsDB == "PREM":
        bkuExt = pAorB + ".tbu"
    else:
        bkuExt = pAorB + ".bku"

    # name backup file: ex: 2015-bill-03
    strBackupFile = myTools.bkuName(pBillMonth,"-bill-",bkuExt)
    fBackup_Data(strBackupFile)

    myTools.checkProcesses()
    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fRestore_Backup(pBackupName):
#---------------------------------------------------#

    logging.debug('Restore_Backup: ' + str(pBackupName))

    if Settings.tsDB == "PREM":
        buExt = ".tbu"
    else:
        buExt = ".bku"
    pBackupName = pBackupName + buExt

    # make sure timeslips has focus
    myTools.getFocus()

    type("f",KeyModifier.ALT)
    type("r")
    time.sleep(1)

    if Settings.tsDB == "PREM":
        click("restore_back_from_local.png")
        time.sleep(1)
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