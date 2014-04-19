#Written by Zack Rosales
#Logic Design COSC 1309-2001
#Multiplication Tables (Nested loops)

#main method start
def main():
    for x in range (1, 13):
        print("   ", x)
        print("---------")
        for y in range (1, 13):
            print(x, " x ", y, " = ", x * y)
        #end for
        print("\n")
    #end for
#main method end

#call to main method
main()        
