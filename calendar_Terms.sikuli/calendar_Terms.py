from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fSetUpEntryTerm():
#---------------------------------------------------#

    time.sleep(1)
    logging.debug('- set up entry terminology')
# open general settings
    myTools.getFocus()
    type("p",KeyModifier.ALT)
    type(Key.ENTER)
    time.sleep(1)
# switch to Calendar Terminology
    myTools.pressF6(2)
# entry terminology
    type("Entry")
    type(Key.TAB)
    type("Entries")
    type(Key.TAB)
    time.sleep(1)

    type("Event")
    type(Key.TAB)
    type("Events")
    type(Key.TAB)
    time.sleep(1)

    type("TooDoo")
    type(Key.TAB)
    type("TooDoo")
    type(Key.TAB)
    time.sleep(1)

    type("Type")
    type(Key.TAB)
    type("Types")

    time.sleep(1)
    type(Key.ENTER)

#---------------------------------------------------#
def fSetUpCatTerm():
#---------------------------------------------------#

    time.sleep(1)
    logging.debug('- set up category terminology')
# open general settings
    type("p",KeyModifier.ALT)
    type(Key.ENTER)
    time.sleep(1)
# switch to Calendar Terminology
    myTools.pressF6(2)
# category terminology
    type("1",KeyModifier.ALT)
    type("One")
    type(Key.TAB)
    type("Two")
    type(Key.TAB)
    type("Three")
    type(Key.TAB)
    type("Four")
    type(Key.TAB)
    type("Five")
    type(Key.TAB)
    type("Six")
    type(Key.TAB)
    type("Seven")
    type(Key.TAB)
    type("Eight")
    type(Key.TAB)
    type("Nine")
    type(Key.TAB)
    type("Ten")
    type(Key.ENTER)

#---------------------------------------------------#
def fSetup_CalTerms():
#---------------------------------------------------#

    logging.debug(' ')
    logging.debug('Setup_CalTerms')
    fSetUpEntryTerm()
    fSetUpCatTerm()
