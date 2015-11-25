from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fEdit_ClientFunds():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("edit client funds")

    logging.debug('Edit_ClientFunds')

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open client list')
    type("n",KeyModifier.ALT)
    type("i")
    time.sleep(1)

    logging.debug('- edit client')
    type(Key.ENTER)
    time.sleep(1)

    # funds page
    myTools.pressSHIFTF6(3)
    time.sleep(1)

    # loop through clients
    for oneClient in range(1,352):

        # log every 10 clients
        if oneClient % 10 == 0:               
            logging.debug('-- client: ' + str(oneClient+1))    

        # list
        myTools.pressTAB(3)
        myTools.pressDOWN(1)
        time.sleep(1)
        
        #open funds
        type(Key.ENTER)
        time.sleep(.5)
        
        # enter 25 for "balance falls below" and "replenishment"    
        if int(Settings.tsVersion) > 2014:    
            myTools.pressTAB(3)
        else:
            myTools.pressTAB(4)    
        time.sleep(.5)
    
        type("25")
        myTools.pressTAB(1)
        type("25")
        myTools.pressTAB(2)
        type(Key.SPACE)
        type(Key.ENTER)
        time.sleep(.5)
        type("s",KeyModifier.CTRL)    
        time.sleep(.5)
        
        #go to nn1 field
        if int(Settings.tsVersion) > 2014:    
            myTools.pressTAB(1)
        else:
            myTools.pressTAB(4)
            
        #next client        
        type(Key.PAGE_DOWN)
        time.sleep(1)

    # close client info
    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1) 
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()