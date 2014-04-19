'''
Written by Zack Rosales
Logic Desgin COSC 1309-2001
Paint Job Estimator

----Psuedocode----
Module main()
    Real sqft,
         pricePerGal
         totalGallons
         hours
         paintCost
         labor
         totalCost

    sqft = getSqft()
    pricePerGal = getPricePerGal()
    totalGallons = calcGallons(sqft)
    hours = calcHours(totalGallons)
    paintCost = calcPaintCost(totalGallons, pricePerGal)
    labor = calcLabor(hours)
    totalCost = calcTotal(paintCost, labor)
    displayTotal(totalGallons, hours, paintCost, labor, totalCost)
End main module

Function getSqft()
    Real sqft
    
    Display "Enter the total square feet to paint: "
    Input sqft
    return sqft
End getSqft function

Function Real getPricePerGal()
    Real price

    Display "Enter the price per gallon: "
    Input price
    return price
End getPricePerGal function

Function Real calcGallons(Real sqft)
    return (sqft / 115)
End calcGallons function

Function Real calcHours(Real totalGallons)
    return (totalGallons * 8)
End calcHours function

Function Real calcPaintCost(Real totalGallons, Real pricePerGal)
    return (totalGallons * pricePerGal)
End calcPaintCost function

Function Real calcLabor(Real hours)
    return (hours * 20.00)
End calcLabor function

Function Real calcTotal(Real paintCost, Real labor)
    return (paintCost + labor)
End calcTotal function

Module displayTotal(Real totalGal, Real hours, Real paint, Real labor, Real total)
    Print "Total Gallons: ", totalGal
    Print "Total hours: ", hours
    Print "Paint Cost: $", paint
    Print "Labor Cost: $", labor
    Print "Total Cost: $", total
End displayTotal module

----End Psuedocode----
----Start Python----'''
#main method start
def main():
    sqft = getSqft()
    pricePerGal = getPricePerGal()
    totalGallons = calcGallons(sqft)
    hours = calcHours(totalGallons)
    paint = calcPaintCost(totalGallons, pricePerGal)
    labor = calcLabor(hours)
    total = calcTotal(paint, labor)
    displayTotal(totalGallons, hours, paint, labor, total)
#main method end

#getSqft method start
def getSqft():
    sqft = float(input("Enter the total square feet to be painted: "))
    return sqft
#getSqft method end

#getPricePerGal method start
def getPricePerGal():
    price = float(input("Enter the price per gallon: $"))
    return price
#getPricePerGal method end

#calcGallons method start
def calcGallons(sqft):
    return (sqft / 115)
#calcGallons method end

#calcHours method start
def calcHours(totalGallons):
    return (totalGallons * 8)
#calcHours method end

#calcPaintCost method start
def calcPaintCost(totalGallons, pricePerGal):
    return (totalGallons * pricePerGal)
#calcPaintCost method end

#calcLabor method start
def calcLabor(hours):
    return (hours * 20.00)
#calcLabor method end

#calcTotal method start
def calcTotal(paint, labor):
    return (paint + labor)
#calcTotal method end

#displayTotal method start
def displayTotal(totalGallons, hours, paint, labor, total):
    print("Total Gallons: ", round(totalGallons, 2))
    print("Total Hours: ", round(hours, 2))
    print("Paint Cost: $", round(paint, 2))
    print("Labor Cost: $", round(labor, 2))
    print("Total Cost: $", round(total, 2))
#displayTotal method end

#call to main method
main()
