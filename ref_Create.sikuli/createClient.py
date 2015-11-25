from sikuli import *
import logging

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fCreate_Client():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('fCreate_Client')

    logging.debug('- open client list')
    click("Names-2.png")
    type("i")
    time.sleep(1)

    logging.debug('- create new client')
    type("n",KEY_CTRL)

    logging.debug('- nicknames')
    time.sleep(1)
    type("ZZZerry")
    type(Key.TAB)
    type("ZhanaZZ")
    type(Key.ENTER)    
    time.sleep(1)

    logging.debug('- name and address')
    type("9999 - Zhana Z. Zerry")
    type(Key.TAB)
    type("9999 Spring Haven Trail")
    type(Key.TAB)   
    time.sleep(1)
    type(Key.TAB)    
    type(Key.TAB)
    type("Zutley")
    type(Key.TAB)
    type("ZZ")
    type(Key.TAB)
    type("99999-1")
    type(Key.TAB)
    type("ZZZ")
    type(Key.TAB)
    type(Key.TAB)
    time.sleep(1)

    logging.debug('- other info')    
# phone
    type("999-999-9999")
# in ref to    
    type("Inreferencet-1.png", "1-SST")
# notes
    click("Notes.png")
    type("Shana S. Terry")
    logging.debug('- save')    
    click("1352170237846-2.png")
    time.sleep(1)
    if exists("ConflictChec.png"):
        logging.debug('- conflict check')    
        type(Key.ENTER)
        time.sleep(1)        
        type(Key.ENTER)
        type(Key.F4,KEY_CTRL)
        time.sleep(1)    
    type(Key.F4,KEY_CTRL)
    time.sleep(1) 
    type(Key.F4,KEY_CTRL)
