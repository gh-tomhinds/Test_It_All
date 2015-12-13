from sikuli import *
import logging
import os
import datetime

#---------------------------------------------------#
def fSetup_Time():
#---------------------------------------------------#

# get current month and year (forget where this is used)
    Settings.rightNow = datetime.datetime.now()
    Settings.thisMonth = Settings.rightNow.month
    Settings.thisYear = Settings.rightNow.year

#---------------------------------------------------#
def fSetup_Folders():
#---------------------------------------------------#

# point to Sikuli folder on desktop
    Settings.sikFolder = os.environ['USERPROFILE']+'\\desktop\\Sikuli'
    logging.debug("- Sikuli folder:    %s" %Settings.sikFolder)

# point to scripts folder on desktop
    Settings.scriptFolder = Settings.sikFolder + '\\Test_It_All'
    logging.debug("- Script folder:    %s" %Settings.scriptFolder)

# point to source data folder on desktop and data files
    Settings.dataFolder = Settings.scriptFolder + '\\!data'
    logging.debug("- Data folder:      %s" %Settings.dataFolder)

    Settings.imgFolder = Settings.dataFolder + '\\images'

# point to folder to copy report errors
    Settings.errorFolder = Settings.scriptFolder + '\\!errors'

#---------------------------------------------------#
def fSetup_ImportDataFiles():
#---------------------------------------------------#

    Settings.cliFile = Settings.dataFolder + '\\towns.csv'
    Settings.tkFile = Settings.dataFolder + '\\timekeepers.csv'
    Settings.taskFile = Settings.dataFolder + '\\tasks.csv'
    Settings.expFile = Settings.dataFolder + '\\expenses.csv'
    Settings.refFile = Settings.dataFolder + '\\refs.csv'
    Settings.tSlipsFile = Settings.dataFolder + '\\slips1.csv'
    Settings.eSlipsFile = Settings.dataFolder + '\\slips2.csv'
    Settings.calFile = Settings.dataFolder + '\\calData.csv'

#---------------------------------------------------#
def fSetup_AppFolders():
#---------------------------------------------------#

# point to report paths
    Settings.rootRepFolder = Settings.scriptFolder + "\\!reports"
    logging.debug("- Rep root folder:  %s" %Settings.rootRepFolder)

    Settings.repFolder = Settings.rootRepFolder + "\\" + Settings.tsVersionPath
    logging.debug("- Report folder:    %s" %Settings.repFolder)

    if Settings.tsDB == "PREM":
        Settings.baseRepFolder = Settings.rootRepFolder + "\\Baseline-PREM"
    else:
        Settings.baseRepFolder = Settings.rootRepFolder + "\\Baseline-BDE"
    logging.debug("- Base Rep folder:  %s" %Settings.baseRepFolder)  

# point to TS paths
    Settings.tsFolder = "C:\\Program Files (x86)\\Timeslips " + Settings.tsVersionPath
    logging.debug("- Timeslips folder: %s" %Settings.tsFolder)

    if Settings.tsDB == "PREM":
        Settings.dbFolder = "C:\\Sikuli"
    else:        
        Settings.dbFolder = Settings.tsFolder + "\\Sikuli"
    logging.debug("- DB folder:        %s" %Settings.dbFolder)

#---------------------------------------------------#
def fSetup_AppFiles():
#---------------------------------------------------#

    Settings.tsEXE = Settings.tsFolder + "\\timeslip.exe" 
    logging.debug("- Timeslips EXE:    %s" %Settings.tsEXE)

    Settings.tsimpEXE = Settings.tsFolder + "\\tsimport.exe" 
    logging.debug("- TSImport EXE:     %s" %Settings.tsimpEXE)

#---------------------------------------------------#
def fSetup_LogFiles():
#---------------------------------------------------#

    # point to Billing Arrangement log file
    Settings.BALogFile = Settings.sikFolder + "\\!BA-Log.txt"

    # point to report log file
    Settings.reportLogFile = Settings.sikFolder + "\\!Rep-Log.txt"
    reportLog = open(Settings.reportLogFile, "a")
    reportLog.write("\n")
    reportLog.write("========================================" + "\n")
    reportLog.close()

    # set up duration log and add version to it
    Settings.durationFile = Settings.sikFolder + "\\Durations-" + Settings.tsVersion + ".csv" 
    durationLog = open(Settings.durationFile, "a")
    durationLog.write(" ," + str(Settings.tsVersion) + "\n")
    durationLog.close()

#---------------------------------------------------#
def fSetup_Envirnoment():
#---------------------------------------------------#

    logging.debug('Setup_Stuff')

    fSetup_Time()

    # get TS version
    Settings.tsVersion = input("TIMESLIPS:", "2016")
    time.sleep(1)

    # we now need to differentiate between TS2016 BDE and Firebird
    if int(Settings.tsVersion) > 2015:
        Settings.tsDB = input("PREM or BDE", "PREM")
        time.sleep(1)
    else:
        Settings.tsDB = "BDE"        

    # append the path with "BDE" for TS2016+ BDE versions
    if (int(Settings.tsVersion) > 2015) and (Settings.tsDB == "BDE"):
        Settings.tsVersionPath = Settings.tsVersion + Settings.tsDB
    else:
        Settings.tsVersionPath = Settings.tsVersion
    logging.debug("- Version path:     %s" %Settings.tsVersionPath)       

    # get data version 
    # setting this automatically for now
#    Settings.dataYear = input("DATA:", "2013")
    Settings.dataYear = "2013" 

    time.sleep(2)
    
    fSetup_Folders()
    fSetup_ImportDataFiles()

    fSetup_AppFolders()
    fSetup_AppFiles()
    fSetup_LogFiles()    

    logging.debug("- OS:               %s" %Settings.getOS())
    logging.debug("- OS Version:       %s" %Settings.getOSVersion())