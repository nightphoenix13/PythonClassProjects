# Written by Zack Rosales
# Logic Desgin COSC 1309-2001
# Chapter 10 File Assignment

#main method start
def main():
    file = open('Numbers.txt', 'r')
    numbers = []
    count = 0
    total = 0
    highest = 0
    lowest = 100
    numberCount = [0] * 90
    for line in file:
        numbers.append(int(line))
        count += 1
        total += int(line)
        if int(line) > highest:
            highest = int(line)
        if int(line) < lowest:
            lowest = int(line)
        numberCount[int(line)] += 1
    average = float(total / (count * 1.0))
    mostRecurring = findMostRecurring(numberCount)
    print("Total numbers: %d" % count)
    print("Sum of numbers: %d" % total)
    print("Average of numbers: %f" % average)
    print("Highest number: %d" % highest)
    print("Lowest number: %d" % lowest)
    print("The number that recurrs most: %d" % mostRecurring)
#main method end

#findMostRecurring method start
def findMostRecurring(numberCount):
    high = 0
    index = 0
    for number in numberCount:
        if number > high:
            high = number
            x = index
        index += 1
    return x
#findMostRecurring method end

#call to main method
main()
