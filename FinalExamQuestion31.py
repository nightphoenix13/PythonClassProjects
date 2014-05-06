def main():
    month = ["January", "February", "March", "April", "May", "June", "July",
            "August", "September", "October", "November", "December"]
    highs = [0] * 12
    lows = [0] * 12

    for temps in range(len(month)):
        highs[temps] = int(input("Enter the highest temperature for " +
                                 month[temps] + ": "))
        lows[temps] = int(input("Enter the lowest temperature for " +
                                month[temps] + ": "))
    #end for
    highMonth = findHighest(highs)
    lowMonth = findLowest(lows)
    print("The hottest month was ", month[highMonth], " at ", highs[highMonth],
          " degrees")
    print("The coldest month was ", month[lowMonth], " at ", lows[lowMonth],
          " degrees")
#main method end

#findHighest method start
def findHighest(highs):
    highest = 0
    highestIndex = 0
    for value in range(len(highs)):
        if highs[value] > highest:
            highest = highs[value]
            highestIndex = value
        #end if
    #end for
    return highestIndex
#findHighest method end

#findLowest method start
def findLowest(lows):
    lowest = 100
    lowestIndex = 0
    for value in range(len(lows)):
        if lows[value] < lowest:
            lowest = lows[value]
            lowestIndex = value
        #end if
    #end for
    return lowestIndex
#findLowest method end

#call to main method
main()
