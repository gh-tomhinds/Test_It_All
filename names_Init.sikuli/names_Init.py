from sikuli import *
import logging
import csv
import myTools

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInit_Clients():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # start with manually entered client, then load other clients from file
    clientList = ["Agawam"]
    allClis = csv.DictReader(open(Settings.cliFile))

    for oneCli in allClis:
        clientList.append(oneCli["NN1"])
    clientList.sort()

    return(clientList)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInit_Timekeepers():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # start with manually entered timekeeper, then load other tks from file
    timekeeperList = ["TomH"]
    allTks = csv.DictReader(open(Settings.tkFile))

    for oneTk in allTks:
        timekeeperList.append(oneTk["NN1"])
    timekeeperList.sort()

    return(timekeeperList)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInit_Tasks():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # start with manually entered task, then load other tasks from file
    taskList = ["CON001"]
    allTasks = csv.DictReader(open(Settings.taskFile))

    for oneTask in allTasks:
        taskList.append(oneTask["nn2"])
    taskList.sort()

    return(taskList)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def fInit_Expensess():
# - - - - - - - - - - - - - - - - - - - - - - - - - #

    # start with manually entered expense, then load other exps from file
    expenseList = ["E001"]
    allExps = csv.DictReader(open(Settings.expFile))

    for oneExp in allExps:
        expenseList.append(oneExp["NN2"])
    expenseList.sort()

    return(expenseList)

