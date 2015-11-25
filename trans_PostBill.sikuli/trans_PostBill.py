from sikuli import *

import myTools
import backup_Data

import trans_SpecCredits
import trans_Writeoff
import trans_ReversePay
import trans_Payments
import trans_Discounts
import trans_Refunds
import trans_Transfers
import trans_TransfersToFunds
import trans_PaymentsToAccount
import trans_Credits
import client_FinanceCharges
import trans_BankDepositSlip

#---------------------------------------------------#
def fEnter_Transactions(transMonth):
#---------------------------------------------------#

    myTools.checkProcesses()

    # enter transactions for month

    trans_SpecCredits.fCreate_SpecCredits(transMonth)
    trans_Writeoff.fCreate_Writeoffs(transMonth)
    trans_ReversePay.fCreate_RevPays(transMonth)
    trans_Discounts.fCreate_Discounts(transMonth)
    trans_Payments.fCreate_PaymentsForMonth(transMonth)
    backup_Data.fBackup_Checkpoint("payments")    
    trans_Transfers.fCreate_Transfers(transMonth)
    trans_TransfersToFunds.fCreate_TransfersToFunds(transMonth)
    backup_Data.fBackup_Checkpoint("transfers")
        
    trans_Refunds.fCreate_Refunds(transMonth)        
    trans_PaymentsToAccount.fCreate_PaymentsToAccount(transMonth)
    backup_Data.fBackup_Checkpoint("pta")
    trans_Credits.fCreate_CreditsForMonth(transMonth)
    backup_Data.fBackup_Checkpoint("credits")
    client_FinanceCharges.fCreate_FinanceCharges(transMonth)        
    backup_Data.fBackup_Checkpoint("finchar")
    
    trans_BankDepositSlip.fBankDepositSlips_Create(transMonth)