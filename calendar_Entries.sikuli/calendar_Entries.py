from sikuli import *
import logging
import csv
import backup_Data
import myTools

#---------------------------------------------------#
def fCreate_CalEntry(pOneEvent,pEventCount):
#---------------------------------------------------#

    logging.debug(' - create: ' + pOneEvent["subject"])

    type("l", KeyModifier.ALT)
    type("n")    
    time.sleep(1)
        
    # subject
    type(pOneEvent["subject"])
    type(Key.TAB)
        
    # categories
    myTools.pressDOWN((pEventCount%10)-1)
    type(Key.TAB)
        
    # start date
    type(pOneEvent["startDate"])
    type(Key.TAB)
    # TS2013 requires extra TAB
    if int(Settings.tsVersion) < 2014:    
        type(Key.TAB)
            
    # start time
    if pOneEvent["startTime"] != "no":
        type(pOneEvent["startTime"])
    type(Key.TAB)
        
    # end date
    type(pOneEvent["endDate"])
    type(Key.TAB)
        
    # TS2013 requires extra TAB
    if int(Settings.tsVersion) < 2014:
        type(Key.TAB)
            
    # end time
    if pOneEvent["endTime"] != "no":
        type(pOneEvent["endTime"])
    type(Key.TAB)
        
    # all day
    if pOneEvent["allday"] == "yes":
        type(Key.SPACE)          
    type(Key.TAB)
        
    # private
    if pOneEvent["private"] == "yes":
        type(Key.SPACE)          
    type(Key.TAB)
        
    # location
    type(pOneEvent["location"])
    type(Key.TAB)
        
    # mark for slip creation
    type(Key.TAB)
        
    # tabs
    type(Key.TAB)
        
    # create meeting for
    if pOneEvent["everyone"] == "no":
        type(Key.HOME)
        myTools.pressDOWN(pEventCount%5)
                
    # schedule
    if pOneEvent["everyone"] == "yes":
        click("schedule_attendees.png")
        time.sleep(1)
        type(Key.INSERT)          
        type(Key.ENTER)
            
    # switch to Notes tab
    type(Key.F6)
        
    # notes field
    type(pOneEvent["notes"])
    type(" - Event: " + str(pEventCount))
    click("save_and_close.png")

#---------------------------------------------------#
def fProcess_CalEntries():
#---------------------------------------------------#
    logging.debug('- create calendar entries')
    time.sleep(1)

    eventCount = 0

    eventDataFile = Settings.calFile
    allEvents = csv.DictReader(open(eventDataFile))

    for calEvent in allEvents:

        eventCount += 1
        fCreate_CalEntry(calEvent,eventCount)

    type(Key.F4, KeyModifier.CTRL)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fCalendar_Entries():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    logging.debug(' ')
    logging.debug('Calendar_Stuff')

    type("l", KeyModifier.ALT)
    type(Key.ENTER)
    time.sleep(1)     
    fProcess_CalEntries()
    backup_Data.fBackup_Checkpoint("cal")

    