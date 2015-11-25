from sikuli import *
import logging
import myTools
import client_Create
import ba__Common
import ba__ReviewBills

#---------------------------------------------------#
def fPercent_Setup1(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "1")
    logging.debug(pBAClient + "1")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(pBAClient)
    type(Key.ENTER)
    time.sleep(1)

# get to arrangement field for time
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(4)
    
# switch to contingency
    type(Key.HOME)
    myTools.pressDOWN(10)
    
# enter details    
    type(Key.TAB)
    type(Key.ENTER)
    time.sleep(1)    
    type("1000")

# enter phases

    myTools.pressTAB(3)
    
    type(Key.SPACE)
    time.sleep(1)    
    type("Phase1")
    type(Key.TAB)
    type("50")
    myTools.pressTAB(3)
    type("25")   
    type(Key.ENTER)
    
    type(Key.SPACE)
    time.sleep(1)    
    type("Phase2")
    type(Key.TAB)
    type("30")
    myTools.pressTAB(3)
    type("25")   
    type(Key.ENTER)
    
    type(Key.SPACE)
    time.sleep(1)    
    type("Phase3")
    type(Key.TAB)
    type("20")
    myTools.pressTAB(3)
    type("25")   
    type(Key.ENTER)

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(5)
    else:
        myTools.pressTAB(6)
		
    time.sleep(1)    
    type("Percent Complete")
    time.sleep(1)    

# save and close    
    type(Key.TAB)
    type(Key.SPACE)
    time.sleep(1)    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPercent_Setup2(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "2")
    logging.debug(pBAClient + "2")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(pBAClient)
    type(Key.ENTER)
    time.sleep(1)

# enter details    
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    type(Key.ENTER)
    time.sleep(1)    

    myTools.pressTAB(2)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("80")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("80")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("80")
    type(Key.ENTER)
    time.sleep(1)    

    # save and close

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(8)        
    else:
        myTools.pressTAB(9)

    type(Key.SPACE)
    time.sleep(1)    
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)    

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPercent_Setup3(pBAClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp(pBAClient + "3")
    logging.debug(pBAClient + "3")

# open client    
    type("i",KeyModifier.CTRL)
    time.sleep(1)
    type(pBAClient)
    type(Key.ENTER)
    time.sleep(1)

# enter details    
    ba__Common.fMoveto_BAPage()
    myTools.pressTAB(5)
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.TAB)
    type(Key.DOWN)
    type(Key.TAB)
    
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("100")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("100")
    type(Key.ENTER)
    time.sleep(1)    

    type(Key.DOWN)
    type("o",KeyModifier.CTRL)
    myTools.pressTAB(4)
    type("100")
    type(Key.ENTER)
    time.sleep(1)    

    # save and close

    if int(Settings.tsVersion) > 2014:
        myTools.pressTAB(8)        
    else:
        myTools.pressTAB(9)

    type(Key.SPACE)
    time.sleep(1)
    type("s",KeyModifier.CTRL)

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fPercent():
#---------------------------------------------------#

    baClient = "BA-Percent"

    # create a new client    
    client_Create.fCreate_Client(baClient,baClient,"Percent Comp","Percent Comp","Percent Comp")
    # create some slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fPercent_Setup1(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,1)
    # compare bill values
    ba__ReviewBills.fReview_BABill(baClient + "1")

    # create some more slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fPercent_Setup2(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,2)
    # compare bill values
    ba__ReviewBills.fReview_BABill(baClient + "2")

    # create some more slips
    ba__Common.fCreate_BASlips(baClient)
    # set up billing arrangement
    fPercent_Setup3(baClient) 
    # print a bill to text
    ba__Common.fPrint_BABill(baClient,3)
    # compare bill values
    ba__ReviewBills.fReview_BABill(baClient + "3")
