#Zack Rosales
#Logic Desgin COSC 1309-2001
#BMI Calculator

#main method start
def main():
    #getting user input
    height = int(input("Please enter your height in inches: "))
    weight = int(input("Please enter your weight in pounds: "))
    #call to calcBMI method
    calcBMI(height, weight)
    #main method end

#calcBMI method start    
def calcBMI(height, weight):
    #outputting results
    print("Your BMI is ", (weight * 703) / (height * 2))
    #calcBMI method end

#call to main method
main()
#end program
