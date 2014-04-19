# Logic Design COSC 1309-2001
# Written by Zack Rosales

# Output for program description
print ("This program calculates the number of credit hours remaining for your degree.")

# Getting data from user
name = input("\nEnter your name: ")
major = input("Enter your major of study: ")
totalHours = int(input("How many hours is the degree plan? "))
completedHours = int(input("How many hours have you completed? "))

# displaying output
print ("\nName: ", name)
print ("Major: ", major)
print ("remaining hours to complete degree: ", totalHours - completedHours)

# End of program
