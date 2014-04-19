#Zack Rosales
#Logic Design COSC 1309-2001
#Simple Restaurant Bill Calculator

#main method start
def main():
    mealPrice = getMealPrice()
    tax = calcTax(mealPrice)
    subtotal = mealPrice + tax
    tip = calcTip(mealPrice, subtotal)
    total = calcTotal(subtotal, tip)
    printReceipt(mealPrice, tax, subtotal, tip, total)
#main method end

#getMealPrice method start
def getMealPrice():
    mealPrice = float(input("Enter the meal price: $"))
    if mealPrice <= 0:
        print("You must enter a positive value. Please try again.")
        mealPrice = float(input("Enter the meal price: $"))
    return mealPrice
#getMealPrice method end

#calcTax method start
def calcTax(mealPrice):
    tax = round(mealPrice * 0.0825, 2)
    return tax
#calcTax method end

#calcTip method start
def calcTip(mealPrice, subtotal):
    if mealPrice < 5.99:
        tip = round(subtotal * 0.1, 2)
    elif mealPrice < 12.00:
        tip = round(subtotal * 0.13, 2)
    elif mealPrice < 17.00:
        tip = round(subtotal * 0.16, 2)
    elif mealPrice < 25.00:
        tip = round(subtotal * 0.19, 2)
    else:
        tip = round(subtotal * 0.22, 2)
    return tip
#calcTip method end

#calcTotal method start
def calcTotal(subtotal, tip):
    total = round(subtotal + tip, 2)
    return total
#calcTotal method end

#printReceipt method start
def printReceipt(mealPrice, tax, subtotal, tip, total):
    print("Meal Price: $", round(mealPrice, 2))
    print("+      Tax: $", round(tax, 2))
    print("--------------------")
    print("  Subtotal: $", round(subtotal, 2))
    print("+      Tip: $", round(tip, 2))
    print("--------------------")
    print("     Total: $", round(total, 2))
#printReceipt method end

#call to main method
main()
#end of program
