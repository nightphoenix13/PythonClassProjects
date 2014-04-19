# Logic Design COSC 1309-2001
# Written by Zack Rosales

# Output for program description
print ("This program accepts a number of seconds from the user and returns the time in days, hours, minutes, and seconds.\n")

# Getting data from user
seconds = int(input("How many seconds would you like to break down? "))

# breaking seconds down
days = int(seconds / 86400) # forcing integer division
remaining = seconds % 86400
hours = int(remaining / 3600) # forcing integer division
remaining = remaining % 3600
minutes = int(remaining / 60) # forcing integer division
remaining = remaining % 60

# Displaying output
print ("Here is the breakdown for ", seconds, " seconds:\n")
print (days, " day(s), ", hours, " hour(s), ", minutes, " minute(s), ", remaining, " second(s)")

# End of program
