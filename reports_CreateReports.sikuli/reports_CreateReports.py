from sikuli import *

import logging
import myTools
import backup_Data
from bill_Print import fSet_BillDate

import bill_Setup
import bill_ImportLayout

import report_UDSlip
import report_UDClient
import report_UDInvoice
import report_UDFunds
import report_Statement
import report_PBWorksheet
import report_TkCollections
import report_FirmAssTot
import report_AgedARBalDate
import report_InvoiceListing
import report_ARwRunBal
import report_FundsWRunBal


#---------------------------------------------------#
def create_Layouts():
#---------------------------------------------------#

    myTools.sectionStartTimeStamp("create layouts")
    logging.debug('create_Layouts')

    myTools.getFocus()
    fSet_BillDate(1)                                        # set bill date to prep delete of dates from layout

    report_UDSlip.fCreate_SlipListDetailed()
    report_UDSlip.fCreate_SlipFields()
    report_UDSlip.fCreate_SlipListCalc()
    
    report_UDClient.fCreate_ClientListHistory()
    report_UDClient.fCreate_ClientListValues()
    
    report_UDInvoice.fCreate_InvoiceListFields()
    report_UDInvoice.fSort_InvoiceListFields()
    
    report_UDFunds.fCreate_FundsListFields()
    report_UDFunds.fSort_FundsListFields()
    
    report_Statement.fImport_Statement()
    report_FirmAssTot.fSetup_FirmAssTot()    
    report_PBWorksheet.fSetup_PreBill()
    report_TkCollections.fSetup_TkCollections()
    report_AgedARBalDate.fSetup_AgedARBalDate()
    report_ARwRunBal.fSetup_ARwRunBal()
    report_FundsWRunBal.fSetup_FundsWRunBal()
    report_InvoiceListing.fSetup_InvoiceListing()

    myTools.sectionEndTimeStamp()

    bill_Setup.fSetup_BillReport()
    bill_ImportLayout.fImport_BillLayout("Bill with Taxes")
    backup_Data.fBackup_BillData(0,"a")                     # backup before first bill 

