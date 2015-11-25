from sikuli import *
import logging
import myTools
import email_Send

import report_AgedARBal
import report_AgedARBalDate
import report_AgedClient
import report_AgedInv
import report_AgedWIP
import report_ARHistory
import report_ARwRunBal
import report_AvailableWIP
import report_BillStage
import report_Budgets
import report_ClientsNotBilled
import report_DaysToPay
import report_FeeAlloc
import report_FeeAllocPer
import report_FirmAssList
import report_FirmAssTot
import report_FundsBal
import report_FundsList
import report_FundsWRunBal
import report_Hold
import report_InvoiceListing
import report_MissingTime
import report_PayDistr
import report_PayPerf
import report_PBWorksheet
import report_ProdPeriod
import report_ProfPeriod
import report_Markup
import report_SlipListing
import report_SlipSummary
import report_SlipTotalsWeekly
import report_SplitBill
import report_Statement
import report_Taxes
import report_TkCC
import report_TkCollections
import report_TkContribution
import report_TkHistory
import report_TOWorksheet
import report_UDSlip
import report_UDClient
import report_UDFunds
import report_UDInvoice
import report_GLXfer

from bill_Print import fSet_BillDate

#---------------------------------------------------#
def fPrint_PostbillReports(pMonth,pAorB):
#---------------------------------------------------#

    # print various reports to check db values and calculations

    fSet_BillDate(pMonth)

    Settings.PartOfRepName = myTools.padZero(pMonth) + pAorB + "-" + Settings.tsVersion

    csvExt = ".csv"
    txtExt = ".txt"
    
    report_AvailableWIP.fPrint_AvailableWIP(pMonth,csvExt)
    report_MissingTime.fPrint_MissingTime(pMonth,csvExt,pAorB)
    report_ClientsNotBilled.Print_ClientsNotBilled(pMonth,csvExt)
    report_FirmAssList.fPrint_FirmAssList(pMonth,csvExt)
    report_PayPerf.fPrint_PayPerf(pMonth,csvExt)

    report_AgedARBal.Print_ARAgedBal(pMonth,csvExt)
    report_AgedARBalDate.Print_ARAgedBalDate(pMonth,csvExt)
    report_AgedClient.fPrint_AgedClient(pMonth,csvExt)
    report_AgedInv.fPrint_AgedInv(pMonth,csvExt)
    report_ARwRunBal.fPrint_ARwRunBal(pMonth,txtExt)

    report_ARHistory.fPrint_ARHistory(pMonth,csvExt)
    report_UDSlip.fPrint_SlipListDetailed(pMonth,csvExt)
    report_UDSlip.fPrint_SlipFields(pMonth,csvExt)
    report_UDSlip.fPrint_SlipListCalc(pMonth,csvExt)    
    report_UDClient.fPrint_ClientListHistory(pMonth,csvExt)
    report_SlipTotalsWeekly.Print_SlipTotalsWeekly(pMonth,csvExt)
    report_TkHistory.Print_TkHistory(pMonth,csvExt)
    report_TkContribution.Print_TkContribution(pMonth,csvExt)  
    report_TkCC.Print_TkCC(pMonth,csvExt)
    report_FundsBal.fPrint_FundsBal(pMonth,csvExt)
    report_Taxes.Print_Taxes(pMonth,csvExt)
    report_TOWorksheet.Print_Worksheet(pMonth,csvExt)
    report_PBWorksheet.fPrint_PreBill(pMonth,txtExt)
    
    email_Send.fSend_Text("rep-half " + str(pMonth) + pAorB)  
    
    report_SlipListing.fPrint_SlipListing(pMonth,csvExt)
    report_BillStage.fPrint_BillStage(pMonth,csvExt)    
    report_FirmAssTot.fPrint_FirmAssTot(pMonth,txtExt)
    report_ProdPeriod.print_ProdPeriod(pMonth,csvExt)
    report_ProfPeriod.print_ProfPeriod(pMonth,csvExt)
    report_Markup.print_Markup(pMonth,csvExt)
    report_SlipSummary.print_SlipSummary(pMonth,csvExt)
    report_Statement.fPrint_Statement(pMonth,txtExt)
#    report_Budgets.printCliBudget(pMonth,csvExt)
#    report_Budgets.printTkBudget(pMonth,csvExt)
#    report_Budgets.printFirmBudget(pMonth,csvExt)    
    report_UDInvoice.fPrint_InvoiceListFields(pMonth,csvExt)
    report_InvoiceListing.fPrint_InvoiceListing(pMonth,txtExt)    
    report_GLXfer.Print_GLXfer(pMonth,csvExt)

    if (pMonth == 13): # skip some reports for ba clients
        logging.debug('')
        logging.debug('!!! SKIP UD FUNDS REPORT')
        logging.debug('!!! SKIP HOLD REPORT')
        logging.debug('!!! SKIP SPLIT BILL DIST')
        logging.debug('!!! SKIP FUNDS w/RUNNING BAL')
        logging.debug('!!! SKIP FUNDS LIST')
    else:
        report_UDFunds.fPrint_FundsListFields(pMonth,csvExt)   
        report_Hold.Print_Hold(pMonth,csvExt)
        report_SplitBill.fPrint_SplitBill(pMonth,csvExt)
        report_FundsWRunBal.fPrint_FundsWRunBal(pMonth,txtExt)
        report_FundsList.fPrint_FundsList(pMonth,csvExt)

    if (pMonth == 13) or (pMonth == 1):
        logging.debug('!!! SKIP FEE ALLOCATION PERIOD REPORT')
    else:        
        report_FeeAllocPer.fPrint_FeeAllocPer(pMonth,csvExt)
        
    if (pMonth == 13) or ((pMonth == 1) and (pAorB == "a")):
        # fee allocation cannot be run without some payments entered
        logging.debug('')
        logging.debug('!!! SKIP COLLECTIONS REPORT')
        logging.debug('!!! SKIP FEE ALLOCATION REPORT')
        logging.debug('!!! SKIP PAYMENT DISTR REPORT')        
        logging.debug('!!! SKIP AGED WIP REPORT')        
    else:
        report_TkCollections.Print_TkCollections(pMonth,txtExt)        
        report_FeeAlloc.Print_FeeAlloc(pMonth,csvExt)
        report_PayDistr.Print_PayDistr(pMonth,csvExt)
        report_AgedWIP.fPrint_AgedWIP(pMonth,csvExt)    

#    report_UDClient.fPrint_ClientListValues(pMonth,csvExt)
#    report_DaysToPay.print_DaysToPay(pMonth,csvExt)   

#    email_Send.fSend_Email("rep " + str(pMonth) + pAorB)
    """
    email_Send.fSend_Text("rep-all " + str(pMonth) + pAorB)