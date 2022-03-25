
def num_check(question):
    valid = False
    while not valid:

        error = "please enter a number that is more than 0"

        try: 

            response = float(input(question))

            if response > 0:
                return response
            
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
    print("replace me with input statements")

    # Calulate perimeter (width + height) x 2
    
    # Calculate the cost of the fencing (perimeter x price / meter)

    # Output the perimeter and cost of the fencing

    
    keep_going = input("Press <enter> to keep going or any key to quit")
    
print()
print("Thanks for using the Fencing cost calculator")