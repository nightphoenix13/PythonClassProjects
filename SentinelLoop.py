#Written by Zack Rosales
#Logic Design COSC 1309-2001
#Sentinel controlled loop

#main method start
def main():
    print("Welcome to this accumulating program")

    #local constants
    SENTINEL = -555

    #local variables
    total = 0
    entries = 0
    low = 0
    high = 0

    #getting priming input from user
    entry = int(input("Enter a number (Enter -555 to quit): "))
    low = entry
    high = entry
    
    #sentinel controlled loop
    while entry != SENTINEL:
        entries += 1
        total += entry
        if entry < low:
            low = entry
        #end if
        if entry > high:
            high = entry
        #end if
        entry = int(input("Enter another number (Enter -555 to quit): "))
    #end while

    #processing method
    average = getAverage(total, entries)

    #output method
    displayOutput(total, entries, low, high, average)
#end main method

#getAverage method start
def getAverage(total, entries):
    average = (total * 1.00) / (entries * 1.00)

    #return average to main method
    return average
#getAverage method end

#displayOutput method start
def displayOutput(total, entries, low, high, average):
    print("\nNumber of entries: ", entries)
    print("Total of numbers entered: ", total)
    print("Lowest number entered: ", low)
    print("Highest number entered: ", high)
    print("Average of numbers entered: ", average)
#displayOutput method end

#call to main method
main()                    
