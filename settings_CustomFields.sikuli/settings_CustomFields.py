from sikuli import *
import logging
import myTools

#---------------------------------------------------#
def fCreateOne(pName, pDownArrow):
#---------------------------------------------------#

    logging.debug('-- create ' + pName)

    type("n",KeyModifier.ALT)
    time.sleep(1)
    myTools.pressDOWN(pDownArrow+1)
    type(Key.ENTER)
    time.sleep(1)
    type(pName)
    type(Key.ENTER)

#---------------------------------------------------#
def fFillCliList():
#---------------------------------------------------#

    logging.debug('- fill list')

    doubleClick("custom_list.png")
    listItems = ['Barnstable','Berkshire','Bristol','Dukes','Essex','Franklin','Hampden','Hampshire','Middlesex','Nantucket','Norfolk','Plymouth','Suffolk','Worcester']

    for listItem in listItems:
        type("n",KeyModifier.ALT)
        type(listItem)
        time.sleep(1)
        type(Key.ENTER)
        time.sleep(1)
    type(Key.ENTER)

#---------------------------------------------------#
def fFillTkList():
#---------------------------------------------------#

    logging.debug('- fill list')

    doubleClick("custom_list.png")
    listItems = ['Brisket','Pork','Ribs','Chicken','Turkey']

    for listItem in listItems:
        type("n",KeyModifier.ALT)
        type(listItem)
        time.sleep(1)
        type(Key.ENTER)
        time.sleep(1)
    type(Key.ENTER)

#---------------------------------------------------#
def fFillActList():
#---------------------------------------------------#

    logging.debug('- fill list')

    doubleClick("custom_list.png")
    listItems = ["Construction","General","Landscape","Hardware","Supplies","Materials","Other"]

    for listItem in listItems:
        type("n",KeyModifier.ALT)
        type(listItem)
        time.sleep(1)
        type(Key.ENTER)
        time.sleep(1)
    type(Key.ENTER)

#---------------------------------------------------#
def fCreate_CustomFields():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("custom fields")

    logging.debug('Create_CustomFields')

    # make sure timeslips has focus
    myTools.getFocus()

    logging.debug('- open custom fields dialog box')
    type("p",KeyModifier.ALT)
    type("c")
    time.sleep(1)

    logging.debug('- add CLIENT custom fields')
    
    customFields = ['Date','Hours','List','Money','Number','Percent','Text','Timekeeper']
    for customField in customFields:
        fCreateOne(customField, customFields.index(customField))
    fFillCliList()

    logging.debug('- add TIMEKEEPER custom fields')

    type(Key.F6)
    time.sleep(1)

    customFields = ['Date','Hours','List','Money','Number','Percent','Text']
    for customField in customFields:
        fCreateOne(customField, customFields.index(customField))
    fFillTkList()

    logging.debug('- add ACTIVITY custom fields')

    type(Key.F6)
    time.sleep(1)

    customFields = ['Date','Hours','List','Money','Number','Percent','Text']
    for customField in customFields:
        fCreateOne(customField, customFields.index(customField))
    fFillActList()
    
    type(Key.ENTER)
    time.sleep(10)

    myTools.sectionEndTimeStamp()