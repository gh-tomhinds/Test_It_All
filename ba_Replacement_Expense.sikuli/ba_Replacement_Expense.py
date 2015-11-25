from sikuli import *
import logging
import myTools
import client_Create
import slips_ReplacementSlips
import ba__Common
import ba__ReviewBills

#===================================================#
def fReplaceExpenseA():
#===================================================#

    # create a new client    
    client_Create.fCreate_Client("BA-ReplaceExpA","BA-ReplaceExpA","Replace Exp A","Replace Exp A","Replace Exp A")
    # create some slips
    slips_ReplacementSlips.fCreate_ReplacementSlips("BA-ReplaceExpA")
    # set up rule
    slips_ReplacementSlips.fCreate_ReplacementRule("BA-ReplaceExpA","x","c","Supplies")
    # print a bill to text
    ba__Common.fPrint_BABill("BA-ReplaceExpA",1)
    # compare at bill values
    ba__ReviewBills.fReview_BABill("BA-ReplaceExpA1")

    