from sikuli import *
import os
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Compare_Reports():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Compare_Reports')

    global newRepLine

# make a list of all files in the NewReports folder
    for reportFile in os.listdir(Settings.repFolder + "\\NewReports\\"):
        if reportFile.endswith(".txt"):

# point to old report, new report, and output file
            logging.debug('- process: ' + reportFile)
            oldFile = Settings.repFolder + "\\OldReports\\" + reportFile
            newFile = Settings.repFolder + "\\NewReports\\" + reportFile
            outFile = Settings.repFolder + "ReportLog.txt"

# don't compare if old report doesn't exist
            if not os.path.exists(oldFile):
                logging.debug(" - MISSING: " + reportFile)
                continue

# open report files
            oldRep = open(oldFile)
            newRep = open(newFile)

# read lines of the report files
            oldRepLines = oldRep.read().splitlines()
            newRepLines = newRep.read().splitlines()

# close report files
            oldRep.close()
            newRep.close()

# open output file
            ReportLog = open(outFile, "a")
            ReportLog.write("Report: %s \n" % reportFile)

# open reset line counter and error flag
            newRepLine = 0
            errorFound = False

# compare each line in old report to new report; jump out on first mismatch
            for oldRepLine in oldRepLines:  
                if oldRepLine != newRepLines[newRepLine]:
                    errorFound = True
                    logging.debug(" - FAILED : " + reportFile)
                    ReportLog.write(" Line: %d \n" % (newRepLine+1))
                    ReportLog.write(" Old: " + oldRepLine + "\n")
                    ReportLog.write(" New: " + newRepLines[newRepLine] + "\n\n")
                    break
                newRepLine += 1
    
            if errorFound != True:
                logging.debug(" - passed : " + reportFile)
                ReportLog.write(" No Error Found \n\n")
               
            ReportLog.close()
            