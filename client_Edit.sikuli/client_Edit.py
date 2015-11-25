from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fEdit_CliGenInfo():
#---------------------------------------------------#

    myTools.openClient("zzz")

    logging.debug('  - nicknames')
    type("a",KeyModifier.CTRL)
    type("Agawam")
    type(Key.TAB)
    time.sleep(1)    
    type("01001")
    myTools.pressTAB(2)

    logging.debug('  - name and address')
    type("City of Agawam")
    type(Key.TAB)
    type("1855 Agawam Road")
    myTools.pressTAB(3)
    time.sleep(1)
    
    type("Agawam")
    type(Key.TAB)
    type("MA")
    type(Key.TAB)
    type("01001")
    type(Key.TAB)
    type("US")
    type(Key.TAB)

    # TS2015 has secondard address
    if int(Settings.tsVersion) > 2014:
        type("PO #1855")
        type(Key.TAB)   
        type(" ")
        type(Key.TAB)    
        type(" ")
        type(Key.TAB)
        type("Mawaga")
        type(Key.TAB)
        type("ma-01001")
        type(Key.TAB)
        type("Mawa-1001")
        type(Key.TAB)
        type("usa")
        type(Key.TAB)
        
    type(Key.TAB)
    time.sleep(1)

    logging.debug('  - other info')    
# phone
    type("617-855 1855")
# in ref to

    if int(Settings.tsVersion) > 2014:
        type(Key.F6)
    else:
        myTools.pressTAB(14)        
    type("a",KeyModifier.CTRL)
    type("County of Hampden")
    time.sleep(1)

#---------------------------------------------------#
def fEdit_CliCustom():
#---------------------------------------------------#

    logging.debug('  - custom fields')

# switch to custom fields
    type(Key.F6)
    
    if int(Settings.tsVersion) > 2014:
        type(Key.F6)
    else:
        type(Key.TAB)

# Date
    customDate = "1/1/" + Settings.dataYear
    type(customDate)
    type(Key.TAB)
 # Hours
    type(".01")
    type(Key.TAB)
 # List
    type("Hampden")
    type(Key.TAB)
 # Money
    type("1000.001")
    type(Key.TAB)
    time.sleep(1)    
 # Number
    type("28438")
    type(Key.TAB)
 # Percent
    type(".11")
    type(Key.TAB)
 # Text
    type("Mayor-council")
    type(Key.TAB)
 # Timekeeper
    type("t")
    time.sleep(1)

#---------------------------------------------------#
def fEdit_CliRatesNotes():
#---------------------------------------------------#

    logging.debug('  - rates and notes')

# switch to rates

    if int(Settings.tsVersion) > 2014:
        type(Key.F6,KeyModifier.SHIFT)
    else:
        type(Key.F6)

# filling rates with 1.01 thru 1.20
    for i in range(101,121):
        rate = str(float(i)/100)
        type(rate)
        type(Key.TAB)
    time.sleep(1)    

# new rate rule
    type("n", KeyModifier.CTRL + KeyModifier.SHIFT)

# timekeeper
    if int(Settings.tsVersion) > 2014:
        type(Key.DOWN)
    else:
        type(Key.TAB + Key.DOWN)
        
# task
    type(Key.TAB + Key.DOWN)
# source
    type(Key.TAB + Key.DOWN)
# level
    type(Key.TAB + Key.DOWN)
    time.sleep(1)    
    type(Key.ENTER)

# notes
# go to first page, then shift+f6

    type("1",KeyModifier.CTRL)
    type(Key.F6,KeyModifier.SHIFT)
    
    if int(Settings.tsVersion) > 2014:
        type(Key.F6,KeyModifier.SHIFT)
    
    type(Key.END)
    type(" edit")

#---------------------------------------------------#
def fEdit_DefaultRates():
#---------------------------------------------------#
    logging.debug('- edit default rates')

    # switch to first client
    type(Key.PAGE_UP, KeyModifier.CTRL)
    # switch to rates page
    type("3", KeyModifier.CTRL)
    # move to LEVEL
    if int(Settings.tsVersion) > 2014:
        myTools.pressSHIFTTAB(7)
    else:
        myTools.pressSHIFTTAB(4)

    counter = 0
    moreClients = True

    # loop through clients
    # assign default rate tk 1-20, then cl 1-20, then ta 1-20, 
    # then loop again until the end
    while moreClients == True:
        for source in ["ti","cl","ta"]:
            logging.debug('-- client: ' + str(counter+1))    
            
            if moreClients == False:
                break
            for level in range(1,21):
                # if i get to total clients, exit early
                if counter > 350:
                    moreClients = False
                    break
                # move to SOURCE
                type(Key.TAB,KeyModifier.SHIFT)
                type(source)
                type(Key.TAB)
                type(str(level))
                type("s",KeyModifier.CTRL)
                time.sleep(1)
    
                type(Key.PAGE_DOWN)
                counter += 1

#---------------------------------------------------#
def fEdit_InterestSetting():
#---------------------------------------------------#

    logging.debug('- edit interest setting')
    
    # switch to first client
    type(Key.PAGE_UP, KeyModifier.CTRL)

    # get to interest field
    if int(Settings.tsVersion) > 2014:
        myTools.pressSHIFTF6(9)
        myTools.pressTAB(9)
    else:
        myTools.pressF6(2)    
        myTools.pressTAB(7)
        
    type("5")
    type("s", KeyModifier.CTRL)
    time.sleep(1)
    click(Pattern("export_button.png").targetOffset(0,8))
    time.sleep(1)
    type(Key.DELETE)

    # interest rate
    myTools.pressDOWN(5)
    
    type(Key.F4)
    time.sleep(1)
    
    type(Key.TAB)
    type(Key.INSERT)
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)
    type("y")
    
    myTools.waitForExportSuccess()

#---------------------------------------------------#
def fEdit_Client():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("edit client")
    logging.debug('Edit_Client')

    # make sure timeslips has focus
    myTools.getFocus()

    fEdit_CliGenInfo()
    fEdit_CliCustom()
    fEdit_CliRatesNotes()

    logging.debug('- save')
    type("s",KeyModifier.CTRL)
    time.sleep(1)

    fEdit_DefaultRates()
    fEdit_InterestSetting()

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()
