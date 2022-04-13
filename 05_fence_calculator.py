# functions go here

# checks input is a number more than zero
from re import M
from tkinter.tix import Meter


def num_check(question):
    valid = False
    while not valid:
        
        error = "Please enter a number that is more than zero"
        
        try:
        
            # ask user to enter a number
            response = float(input(question))
            
            # checks number is more than zero
            if response > 0:
                return response
            
            # outputs error if input is invalid
            else:
                print(error)
                print()
                
        except ValueError:
            print(error)    
    


# Main Routine goes here

# Introduction / Heading print statements
print()
print("**** Fence Cost Calculator *****")
print()

# Start of calculator loop
keep_going = ""
while keep_going == "":

    # call your number checker function three times to get the 
    # width, length and cost_per_m of the fencing
    width = num_check ("width: ")
    height = num_check("height: ")
    cost_per_m = num_check("cost / m: ")

    # Calulate perimeter (width + height) x 2
    perimeter = width + height * 2
    # Calculate the cost of the fencing (perimeter x price / meter)
    fencing = perimeter * cost_per_m / cost_per_m

    # Output the perimeter and cost of the fencing
    print("perimeter:  {:.2f} units".format(perimeter))
    print("cost:  {:.2f} square units".format(cost_per_m))
    print()

    
    keep_going = input("Press <enter> to keep going or any key to quit")
    
print()
print("Thanks for using the Fencing cost calculator")

        
    
    