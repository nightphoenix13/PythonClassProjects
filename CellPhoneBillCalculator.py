#Written by Zack Rosales
#Logic Design COSC 1309-2001
#Old School Cell Phone Bill Calculator

#main method start
def main():
    #local variable
    endProgram = "no"

    while endProgram == "no":
        #re-initializing variables
        minutesAllowed = 0
        minutesUsed = 0
        minutesOver = 0
        totalDue = 0.00
        
        #input methods
        minutesAllowed = getAllowed(minutesAllowed)
        minutesUsed = getUsed(minutesUsed)

        #processing methods
        minutesOver = calcMinutesOver(minutesAllowed, minutesUsed)
        totalDue = calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver)

        #output method
        printData(minutesAllowed, minutesUsed, totalDue, minutesOver)

        #asking user for input
        endProgram = input("Do you want to end the program? \"yes\" or \"no\"")

        #input validation to ensure user enters a valid option
        while not(endProgram.lower() == "yes" or endProgram.lower() == "no"):
            print("You must enter \"yes\" or \"no\".")
            endProgram = input("Do you want to end the program? \"yes\" or \"no\"")
        #end while
    #end while
print("Have a good day!")
#main method end

#getAllowed method start
def getAllowed(minutesAllowed):
    #asking user for input
    minutesAllowed = int(input("How many minutes are allowed? "))

    #input validation to ensure user enters a valid number
    while minutesAllowed < 200 or minutesAllowed > 800:
        print("You must enter a value between 200 and 800.")
        minutesAllowed = int(input("How many minutes are allowed? "))
    #end while

    #return minutesAllowed to main method
    return minutesAllowed
#getAllowed method end

#getUsed method start
def getUsed(minutesUsed):
    #asking user for input
    minutesUsed = int(input("How many minutes were used? "))

    #input validation to ensure user enters a valid number
    while minutesUsed < 0:
        print("You cannot enter a negative value.")
        minutesUsed = int(input("How many minutes were used? "))
    #end while

    #return minutesUsed to main method
    return minutesUsed
#getUsed method end

#calcMinutesOver method start
def calcMinutesOver(minutesAllowed, minutesUsed):
    if minutesUsed > minutesAllowed:
        minutesOver = minutesUsed - minutesAllowed
    #end if
    else:
        minutesOver = 0
    #end else

    #return minutesOver to main method
    return minutesOver
#calcMinutesOver method end

#calcTotal method start
def calcTotal(minutesAllowed, minutesUsed, totalDue, minutesOver):
    if minutesOver == 0:
        totalDue = 74.99
        print("You were not over your minutes for the month.")
    #end if
    else:
        extra = minutesOver * 0.20
        totalDue = 74.99 + extra
        print("You were over your minutes by ", minutesOver, " minutes.")
    #end else

    #return totalDue to main method
    return totalDue
#calcTotal method end

#printData method start
def printData(minutesAllowed, minutesUsed, totalDue, minutesOver):
    print("----------------------MONTHLY USE REPORT----------------------")
    print("Minutes allowed: ", minutesAllowed)
    print("Minutes used: ", minutesUsed)
    if minutesOver != 0:
        print("Minutes over: ", minutesOver)
    #end if
    print("Total amount due: $", round(totalDue, 2))
#printData method end

#call to main method
main()
