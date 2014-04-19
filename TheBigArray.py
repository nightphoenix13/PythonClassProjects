#Written by Zack Rosales
#Logic Design COSC 1309-2001
#The Big Array

#random module
import random

#global constant
SIZE = 500

#main method start
def main():
    #array of 500 elements
    numbers = [0] * SIZE

    #randomize array
    for index in range(SIZE - 1):
        numbers[index] = random.randint(0, 100)
    #end for

    #initializing variables
    total = 0
    lowest = numbers[0]
    highest = numbers[0]

    #for loop to step through array
    for n in numbers:
        total += n
        if n < lowest:
            lowest = n
        #end if
        if n > highest:
            highest = n
        #end if
    #end for

    average = (total * 1.00) / (SIZE * 1.00)

    displayOutput(total, average, lowest, highest)
#main method end

#displayOutput method start
def displayOutput(total, average, lowest, highest):
    print("The total of the elements in the array is ", total)
    print("The average of the elements is ", average)
    print("The lowest number in the array is ", lowest)
    print("The highest number in the array is ", highest)
#displayOutput method end

#call to main method
main()
