from sikuli import *
import logging
import myTools
import client_Create
import slips_ReplacementSlips
import ba__Common
import ba__ReviewBills

#===================================================#
def fReplaceTimeA():
#===================================================#

    # create a new client    
    client_Create.fCreate_Client("BA-ReplaceTimeA","BA-ReplaceTimeA","Replace Time A","Replace Time A","Replace Time A")
    # create some slips
    slips_ReplacementSlips.fCreate_ReplacementSlips("BA-ReplaceTimeA")
    # set up rule
    slips_ReplacementSlips.fCreate_ReplacementRule("BA-ReplaceTimeA","t","c","General")
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ReplaceTimeA",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ReplaceTimeA1")

#===================================================#
def fReplaceTimeB():
#===================================================#

    # create a new client    
    client_Create.fCreate_Client("BA-ReplaceTimeB","BA-ReplaceTimeB","Replace Time B","Replace Time B","Replace Time B")
    # create some slips
    slips_ReplacementSlips.fCreate_ReplacementSlips("BA-ReplaceTimeB")
    # set up rule
    slips_ReplacementSlips.fCreate_ReplacementRule("BA-ReplaceTimeB","t","c","Landscape")
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ReplaceTimeB",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ReplaceTimeB1")

#===================================================#
def fReplaceTimeC():
#===================================================#

    # create a new client    
    client_Create.fCreate_Client("BA-ReplaceTimeC","BA-ReplaceTimeC","Replace Time C","Replace Time C","Replace Time C")
    # create some slips
    slips_ReplacementSlips.fCreate_ReplacementSlips("BA-ReplaceTimeC")
    # set up rule
    slips_ReplacementSlips.fCreate_ReplacementRule("BA-ReplaceTimeC","t","a","Pave")
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ReplaceTimeC",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ReplaceTimeC1")

