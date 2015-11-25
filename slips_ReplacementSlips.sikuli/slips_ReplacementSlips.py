from sikuli import *
import logging
import myTools
import slips_Create

#---------------------------------------------------#
def fCreate_ReplacementRule(pReplClient,pTimeOrExp,pActOrCat,pName):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("replacement rule")
    logging.debug('fCreate_ReplacementRule')

    # open replacement list
    type("s",KeyModifier.ALT)
    type("n")
    time.sleep(1)

    # move to client
    type(pReplClient)
    time.sleep(1)

    # new
    type("n",KeyModifier.ALT)
    time.sleep(1)
    
    # time or expense
    type(pTimeOrExp)
    myTools.pressTAB(1)
    time.sleep(1)

    # activity or category
    type(pActOrCat)
    myTools.pressTAB(1)
    time.sleep(1)

    # name
    type(pName)
    myTools.pressTAB(2)
    time.sleep(1)

    # description
    type("Replacing slips for: " + pName)
    myTools.pressTAB(4)
    time.sleep(1)

    # ok
    type(Key.ENTER)
    time.sleep(1)

    # close
    type(Key.F4,KeyModifier.ALT)
    time.sleep(1)

    myTools.sectionEndTimeStamp()

#---------------------------------------------------#
def fCreate_ReplacementSlips(pReplClient):
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("replacement slips")
    logging.debug('fCreate_ReplacementSlips')

    type("m",KeyModifier.CTRL)
    time.sleep(1)
    
    # create some time slips
    slips_Create.Create_OneSlip("t","TomH","gen004",pReplClient,1)   #override - General
    slips_Create.Create_OneSlip("t","CoreyM","gen005",pReplClient,2) #donotbill - General
    slips_Create.Create_OneSlip("t","SamS","lnd011",pReplClient,3)   #billable - Landscape
    slips_Create.Create_OneSlip("t","ShawnR","lnd010",pReplClient,4) #nocharge - Landscape
    slips_Create.Create_OneSlip("t","JamesR","lnd011",pReplClient,5) #billable - Landscape

    # create some expense slips
    slips_Create.Create_OneSlip("e","ShawnR","e006",pReplClient,6)   #donotbill - Supplies
    slips_Create.Create_OneSlip("e","SamS","e009",pReplClient,7)     #billable - Supplies
    slips_Create.Create_OneSlip("e","CoreyM","e003",pReplClient,8)   #nocharge - Supplies
    slips_Create.Create_OneSlip("e","TomH","e008",pReplClient,9)     #override - Supplies
    slips_Create.Create_OneSlip("e","JamesR","e010",pReplClient,10)  #billable - Other

    type(Key.F4,KeyModifier.CTRL)
    time.sleep(1)
    type(Key.F4,KeyModifier.CTRL)

    myTools.sectionEndTimeStamp()
