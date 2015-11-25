## Intro

This project contains SIKULI code to automate some regression test plans.

## Supporting Folders

### !data

Contains data files for various functions, such as:
* .csv files for importing names and slips
* .csv files for comparing bill arrangement values
* .tsl files to import bill layouts

### !reports

Stores reports for comparison
* there is a folder that holds baseline reports
* there are folders to store newly generated reports

##  Files

### _main

This script the main driver of all other scripts.
* It sets up the logging system.
* It generates the starting time stamp
* It calls all scripts (or all scripts that call other scripts)
* It generates the ending time stamp

### myTools

**setupLog**,
called by: _main,
initializes main log file

**pressTAB**,
called by: many places,
presses TAB key x times

**pressSHIFTTAB**,
called by: many places,
presses SHIFT+TAB key x times

**pressF6**
    called by: many places
    presses F6 key x times

**pressSHIFTF6**
    called by: many places
    presses SHIFT+F6 key x times

**pressDOWN**
    called by: many places
    presses DOWN key x times

**pressUP**
    called by: many places
    presses UP key x times

**pressLEFT**
    called by: many places
    presses LEFT key x times

**pressRIGHT**
    called by: many places
    presses RIGHT key x times

**getFocus**
    called by: many places
    clicks the data label in the bottom task bar to ensure Timeslips has focus

**waitForExportSuccess**
    called by: import scripts
    waits for the import to end successfully

**monthToName**
    called by: some scripts that require file names
    takes the current month and a file extension and returns a file name

**startTimeStamp**
    called by: _main
    beginning time stamp for log file

**endTimeStamp**
    called by: _main
    ending time stamp for log file

**sectionStartTimeStamp**
    called by: any script that is logging duration
    beginning section time stamp for log file

**sectionEndTimeStamp**
    called by: any script that is logging duration
    ending section time stamp for log file

### _global_Settings

**Setup_Stuff**
called by: _main
This script sets up many of the global variables (usually paths and file names) used throughout the scripts.
* some of these are based on the version number
* some of these are based on the Sikuli folder on the desktop

### closeTimeslips

This file used to include code to close Timeslips.
After a while that seemed silly. Now it simply reminds you to close Timeslips before continuing.

### delDataFolder

This file contains code to delete the folder containing the test data. It will be rebuilt.

### db_New

This file contains code to create a new empty database.
* StartTS_CreateNewDB - Opens Timeslips and walks through the data creation process.
* checkFor_BillingDate - Closes the Revise Billing Date dialog
* checkFor_SPS - closes the SPS dialog
* checkFor_PEP - closes the PEP message
* checkFor_Sample - closes the Sample Database message

### settings_Prefs

This file first resets preferences to their default, then sets several preferences to values that help speed data entry. These changes are saved in a new preference file.

### settings_Categories

This file creates a set of categories for use with new tasks and expenses.

### settings_CustomFields

This file create one of each type of client custom fields.
* Create_CustomFields - opens the Custom fields dialog box and calls CreateOne for each type of custom field; then calls FillList
* CreateOne - Creates a specific custom field
* FillList - Fills the List type custom field with values

### client_Create

This file contains code to create one client. 
Initially, it's called with values to create the first client in the database. 
Then it's called to by each billing arrangement script to create a new client for that specific billing arrangement. 

### task_Create

This file contains code to create the initial task. 

### expense_Create

This file contains code to create the initial expense. 

### timekeeper_Imports

This file contains code to open TSImport to import additional timekeepers from a file.
That data file is: Desktop\Sikuli\DataFiles\timekeepers.csv.

### timekeeper_Edit

This file contains code to edit the initial timekeeper that was created in db_New.

### client_Import

This file contains code to open TSImport to import additional timekeepers from a file.
That data file is: Desktop\Sikuli\DataFiles\towns.csv.
* Import_Clients - Opens TSImport, sets up the template, imports data
* Add_CustomField - Adds the custom fields to the template

### client_Edit

This file contains code to edit the initial client that was created in client_Create, then also edit default rate and interest for all clients.
* EditClient - Drives the process
* Edit_CliGenInfo - edits values in the Contact Info page for initial client
* Edit_CliCustom - edits values in the Custom page for initial client
* Edit_CliRatesNotes - edits billing rates and notes for initial client
* Edit_DefaultRates - loops through all clients, editing default rate settings
* Edit_InterestSetting - edits interest setting and exports it to all other clients

### task_Import

This file contains code to open TSImport to import additional tasks from a file.
That data file is: Desktop\Sikuli\DataFiles\tasks.csv.

### task_Edit

This file contains code to edit the initial client that was created in task_Create.

### expense_Import

This file contains code to open TSImport to import additional expenses from a file.
That data file is: Desktop\Sikuli\DataFiles\expenses.csv.

### expense_Edit

This file contains code to edit the initial client that was created in expense_Create.

### ref_Create

This file contains code that changes reference settings, exports them to all clients, then creates global references (from names in a data file) that are used by all clients.
That data file is: Desktop\Sikuli\DataFiles\templateRefs.csv.

### ref_Import

This file contains code that sets up a TSImport template and imports client-specific references for each client.
That data file that is imported is: Desktop\Sikuli\DataFiles\refs.csv.

### client_FeeAlloc

### expense_Markup

### taxes_Setup

### slips_Create

### createPayments

### bill_ImportLayout

### bill_Print

### baCommon

### reviewBillingArrangements

### calendar_Terms

### calendar_Entries

### report_ClientInfo

### printTasks

### printExpenses

### report_TimekeeperInfo

### compareReports

