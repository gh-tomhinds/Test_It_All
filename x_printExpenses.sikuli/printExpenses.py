from sikuli import *
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def Print_Expenses():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
 
    logging.debug(' ')
    logging.debug('Print_Expenses')

    logging.debug('- open report list')
    click("Beports.png")
    type("i")

    logging.debug('- set up expense info listing')
    doubleClick("ExnenscInfoL.png")
    click("MZElpticns.png")
    click("1352843528241.png")
    click("Showar.png")
    type(Key.ENTER)

# choose CSV
    type(Key.TAB)
    type(Key.TAB)
    type(Key.F4)
    time.sleep(1)
    type("c")    
    type(Key.ENTER)

    logging.debug('- print')
    click("1352843841109.png")
    time.sleep(1)

    if Settings.tsVersion == "2014":
        type(Settings.repFolder + "\\NewReports\\expenselist.csv")
    else:
        type(Settings.repFolder + "\\OldReports\\expenselist.csv")        

    time.sleep(1)
    click("7.png")
    type(Key.ENTER)
    if exists("Confirm.png"):
        type(Key.ENTER)
    time.sleep(3)        
    type(Key.F4,KEY_CTRL)
    time.sleep(1)            
    type("n")
    type(Key.F4,KEY_CTRL)    
