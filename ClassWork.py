#Zack Rosales
#Logic Desgin COSC 1309-2001
#April 11 class work

#main method start
def main():
    #creating parallel arrays
    nameList = ["Turner", "Philips", "Stevenson", "Jones", "Gonzalez",
                "Whitaker", "Bruner", "Webster", "Foster", "Anderson", "Klein",
                "Conners", "Rivers", "Wilson", "Duncan"]
    gradeList = [94, 82, 87, 78, 65, 90, 85, 97, 70, 100, 57, 88, 73, 92, 84]
    #displays menu and gets user selection
    choice = menu()
    while choice != 0:
        if choice == 1:
            displayLists(nameList, gradeList)
        #end if
        elif choice == 2:
            sortLists(nameList, gradeList)
        #end elif
        elif choice == 3:
            print("\nThe average test score is ", calcAverage(gradeList), "\n")
        #end elif
        elif choice == 4:
            print("\nThe mean test score is:")
            print(getMean(nameList, gradeList))
            print("\n")
        #end elif
        elif choice == 5:
            name = input("\nEnter the name of the student: ")
            specificStudent(name, nameList, gradeList)
        #end elif
        choice = menu()
    #end while
    print("Have a good day!")
#main method end

#menu method start
def menu():
    #displaying menu options
    print("Please select one of the following options:")
    print("1. Display unsorted list")
    print("2. Display sorted list")
    print("3. See the average grade")
    print("4. See the median grade")
    print("5. Get grade for specific student")
    print("0. Exit the program")
    choice = int(input("Please enter a selection: "))

    #input validation
    while choice < 0 or choice > 5:
        print("You did not choose a valid option. Please try again.")
        choice = int(input("Please enter a selection(0 - 5): "))
    #end while

    return choice
#menu method end

#displayLists method start
def displayLists(nameList, gradeList):
    index = 0
    print("\n%-30s%10s" % ("Student", "Grade"))
    while index < 15:
        print("%-30s%10d" % (nameList[index], gradeList[index]))
        index += 1
    #end while
    print("\n")
#displayLists method end

#sortLists method start
def sortLists(nameList, gradeList):
    sortedNameList = nameList
    sortedGradeList = gradeList
    index = highestIndex = 0
    highest = sortedGradeList[index]
    startingIndex = 1
    while startingIndex < 14:
        index = startingIndex
        while index < 15:
            if sortedGradeList[index] > highest:
                highestIndex = index
                highest = sortedGradeList[index]
            #end if
            index += 1
        #end while
        tempName = sortedNameList[startingIndex - 1]
        tempGrade = sortedGradeList[startingIndex - 1]
        sortedNameList[startingIndex - 1] = sortedNameList[highestIndex]
        sortedGradeList[startingIndex - 1] = sortedGradeList[highestIndex]
        sortedNameList[highestIndex] = tempName
        sortedGradeList[highestIndex] = tempGrade
        highest = sortedGradeList[startingIndex]
        highestIndex = startingIndex
        startingIndex += 1
    #end while

    #call to displayLists method
    displayLists(sortedNameList, sortedGradeList)
#sortLists method end

#calcAverage method start
def calcAverage(gradeList):
    index = total = 0
    while index < 15:
        total += gradeList[index]
        index += 1
    #end while
    return round(total / 15.0, 2)
#calcAverage method end

#getMean method start
def getMean(nameList, gradeList):
    sortedNameList = nameList
    sortedGradeList = gradeList
    index = highestIndex = 0
    highest = sortedGradeList[index]
    startingIndex = 1
    while startingIndex < 14:
        index = startingIndex
        while index < 15:
            if sortedGradeList[index] > highest:
                highestIndex = index
                highest = sortedGradeList[index]
            #end if
            index += 1
        #end while
        tempName = sortedNameList[startingIndex - 1]
        tempGrade = sortedGradeList[startingIndex - 1]
        sortedNameList[startingIndex - 1] = sortedNameList[highestIndex]
        sortedGradeList[startingIndex - 1] = sortedGradeList[highestIndex]
        sortedNameList[highestIndex] = tempName
        sortedGradeList[highestIndex] = tempGrade
        highest = sortedGradeList[startingIndex]
        highestIndex = startingIndex
        startingIndex += 1
    #end while

    return "%-30s%10d" % (nameList[7], gradeList[7])
#getMean method end

#specificStudent method start
def specificStudent(name, nameList, gradeList):
    match = False
    index = 0
    while index < 15:
        if name == nameList[index]:
            matchIndex = index
            match = True
        #end if
        index += 1
    #end while
    if match == True:
        print("\nSpecific student grade:")
        print("%-30s%10d" % (nameList[matchIndex], gradeList[matchIndex]))
        print("\n")
    #end if
    else:
        print("\nYou did not enter a name in the list.\n")
    #end else
#specificStudent method end
    
#call to main method
main()
