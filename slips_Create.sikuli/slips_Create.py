from sikuli import *
import logging
import myTools
import names_Init
import backup_Data

#---------------------------------------------------#
def Open_SlipList():
#---------------------------------------------------#

    # open slip list and verify it's open
    myTools.getFocus()
    type("m",KeyModifier.CTRL)
    time.sleep(1)
    click("number_of_slips_button.png")

#---------------------------------------------------#
def Open_LastSlip():
#---------------------------------------------------#

    # go to the end of the list and open the slip so we can copy dates.
    type(Key.END)
    type(Key.ENTER)
    time.sleep(1)

#---------------------------------------------------#
def Close_SlipUI():
#---------------------------------------------------#

    logging.debug('- close slip entry; close slip list')
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    
    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def Attachment_Add(number):
#---------------------------------------------------#

    # open section
    click("attachments_open_button.png")

    # move to attachment field
    myTools.pressSHIFTTAB(2)
    
    # build name and paste it
    attachmentName = Settings.imgFolder + "\\" + str(number) + ".bmp"
    paste(attachmentName)

    # close section
    click("attachments_close_button.png")

#---------------------------------------------------#
def Create_OneSlip(slipType,tk,act,cli,slipnum):
#---------------------------------------------------#

    logging.debug('- Create_OneSlip: ' + str(slipnum))

    type("n",KeyModifier.CTRL)
    time.sleep(1)

    # slip type
    type(slipType)

    # timekeeper
    type(Key.TAB)
    type(tk)

    # activity
    type(Key.TAB)
    type("2",KeyModifier.CTRL + KeyModifier.SHIFT)
    time.sleep(1)
    type(act)

    # client
    type(Key.TAB)
    time.sleep(1)   
    type(cli)
    time.sleep(1)

    # reference
    type(Key.TAB)
    # use down arrow for ref; skip every 8th one
    type(Key.HOME)
    for ref in range(slipnum % 8):
        type(Key.DOWN)
    time.sleep(1)

    # extra
    type(Key.TAB)
    type("Slip: ")
    type(slipType)
    type(str(slipnum))
    time.sleep(1)

    # description
    type(Key.TAB)

    # start date for the first slip is 1/01
    type(Key.TAB)
    if slipnum == 1:
        slipDate = "1/1/" + Settings.dataYear
        type(slipDate)
        
    # increment the date every 8th slip.
    elif (slipnum - 1) % 8 == 0:
        type("+")

    # every 25th slip, tab to Hold and mark it
    # note: no slip with Hold will also be recurring (see next if)
    if slipnum % 25 == 0:
        myTools.pressTAB(6)
        time.sleep(1)
        type(Key.SPACE) 

    # recur the slips 6 thru 10; one slip of each bill status type
    # also add one hour DoNotBill time
    # note: no slip with Recur will also be on Hold (see previous if)
    # the slipType check below is so bill arrangement scripts don't run this part
    if slipType == "t" and slipnum in range(6,11):
        
        # recurring
        myTools.pressTAB(7)
        time.sleep(1)
        type(Key.SPACE)       
        
        # open section
        click("donotbill_open_button.png")

        # markup
        myTools.pressTAB(5)
        if slipnum in (7,8): 
            type("-50.12347")
        else:
            type("51.23457")            

        # adjustment
        myTools.pressTAB(1)
        if slipnum in (7,8): 
            type("-50.12347")
        else:
            type("51.23457")            

        # DNB time
        myTools.pressTAB(1)
        time.sleep(1)
        type(".75")
        
        click("donotbill_close_button.png")    
        time.sleep(1)        

        # add an attachment image
        Attachment_Add(slipnum)

    elif slipType == "e" and slipnum in range(706,711):

        # recurring
        myTools.pressTAB(7)
        time.sleep(1)
        type(Key.SPACE)
        
        # open section
        click("adjustment_open_button.png")

        # markup
        myTools.pressTAB(1)
        if slipnum in (706,708):
            type("-50.12347")
        else:
            type("51.23457")

        # adjustment
        myTools.pressTAB(1)
        if slipnum in (706,708):
            type("-50.12347")
        else:
            type("51.23457")
        
        time.sleep(1)        
        click("adjustment_close_button.png")

        # add an attachment image
        Attachment_Add(slipnum)

    type("s",KeyModifier.CTRL)
    time.sleep(1)

#---------------------------------------------------#
def Import_TimeSlips():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("import time slips")
    logging.debug('Import_TimeSlips')

    myTools.startTSImport()

    logging.debug('- set up slip template')
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)
    
    type("c")
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

#choose source
    wait("put_data_into.png")
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    paste(Settings.tSlipsFile)

#choose fields
    myTools.pressTAB(7)

# type
    myTools.pressDOWN(1)
    type(Key.ENTER)

# timekeeper
    myTools.pressDOWN(1)
    type(Key.ENTER)

# client
    myTools.pressDOWN(2)
    type(Key.ENTER)

# activity
    myTools.pressDOWN(2)
    type(Key.ENTER)

# reference
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# extra
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# date
    myTools.pressDOWN(2)
    type(Key.ENTER)

# hold
    myTools.pressDOWN(9)
    type(Key.ENTER)

# omit 1st 10 records
    click("limit_records.png")
    type(Key.TAB)
    type("12")
    time.sleep(1)        

# import data
    logging.debug('- import data')
    type(Key.F9)
    time.sleep(1)    
    type(Key.RIGHT)
    type(Key.ENTER)   
     
# verify data
    wait("number_of_records.png",FOREVER)
    if exists(Pattern("failed.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

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
    
    myTools.sectionEndTimeStamp()
    
# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Import_ExpenseSlips():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    myTools.sectionStartTimeStamp("import expense slips")
    logging.debug('Import_ExpenseSlips')

    myTools.startTSImport()

    logging.debug('- set up slip template')
    type("f",KeyModifier.ALT)
    type("n")
    time.sleep(1)
    
    type("c")
    type(Key.ENTER)
    time.sleep(1)
    type(Key.ENTER)

#choose source
    wait("put_data_into.png")
    time.sleep(1)
    type("g",KeyModifier.ALT)
    time.sleep(1)
    paste(Settings.eSlipsFile)

#choose fields
    myTools.pressTAB(7)

# type
    myTools.pressDOWN(1)
    type(Key.ENTER)

# timekeeper
    myTools.pressDOWN(1)
    type(Key.ENTER)

# client
    myTools.pressDOWN(2)
    type(Key.ENTER)

# activity
    myTools.pressDOWN(2)
    type(Key.ENTER)

# reference
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# extra
    myTools.pressDOWN(2)
    type(Key.ENTER)
    
# date
    myTools.pressDOWN(2)
    type(Key.ENTER)

# hold
    myTools.pressDOWN(9)
    type(Key.ENTER)

# omit 1st 10 records
    click("limit_records.png")
    type(Key.TAB)
    type("12")
    time.sleep(1)        

# import data
    logging.debug('- import data')
    type(Key.F9)
    time.sleep(1)    
    type(Key.RIGHT)
    type(Key.ENTER)   
     
# verify data
    wait("number_of_records.png",FOREVER)
    if exists(Pattern("failed.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

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
    
    myTools.sectionEndTimeStamp()    

#---------------------------------------------------#
def Create_Slips(tmslips,exslips):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("init names")
    logging.debug('Init Names')    

    clients = names_Init.fInit_Clients()
    timekeepers = names_Init.fInit_Timekeepers()
    tasks = names_Init.fInit_Tasks()
    expenses = names_Init.fInit_Expensess()
    count = 0
    myTools.sectionEndTimeStamp()

    myTools.sectionStartTimeStamp("create time slips")
    Open_SlipList()    

    for slip in range(tmslips):
        Create_OneSlip("t",timekeepers[count%len(timekeepers)],tasks[count%len(tasks)],clients[count%len(clients)],count+1)
        count += 1
    Close_SlipUI()

    Import_TimeSlips()

    myTools.sectionStartTimeStamp("create expense slips")
    # increase count to account for imported slips
    count += 692

    Open_SlipList()    
    Open_LastSlip()

    for slip in range(exslips):
        Create_OneSlip("e",timekeepers[count%len(timekeepers)],expenses[count%len(expenses)],clients[count%len(clients)],count+1)
        count += 1        
    Close_SlipUI()

    Import_ExpenseSlips()

#---------------------------------------------------#
# remove this later
#
#    myTools.sectionStartTimeStamp("create time slips")
#    Open_SlipList()    
#    Open_LastSlip()
#
#    for slip in range(tmslips):
#        Create_OneSlip("t",timekeepers[count%len(timekeepers)],tasks[count%len(tasks)],clients[count%len(clients)],count+1)
#        count += 1
#    Close_SlipUI()
#
#    myTools.sectionStartTimeStamp("create expense slips")
#    Open_SlipList()
#    Open_LastSlip()
#    
#    for slip in range(exslips):
#        Create_OneSlip("e",timekeepers[count%len(timekeepers)],expenses[count%len(expenses)],clients[count%len(clients)],count+1)
#        count += 1        
#    Close_SlipUI()

#---------------------------------------------------#

    backup_Data.fBackup_Checkpoint("slips")
