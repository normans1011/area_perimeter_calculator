


#checks input is a number more than zero

def num_check (question):

    valid = False
    while not valid:

        error = "Please enter a number that is more than zero"

        try:
            
            # ask user to enter a number
            response = float(input(question))
            
            
            # checks number is more than zero
            if response >0:
                return response

            else:
                print(error)
    
        
        except ValueError:
            print(error)

#main routine goes here

print("===============================")
print("-----Fence-cost-calculator-----")
print("===============================")

keep_going = ""
while keep_going == "":


    width = num_check( "Width (m): ")
    length = num_check("Length(m): ")
    cost_m = num_check("cost per meter: $")

    #calculator

    perimeter = 2 * (length+width)
    cost = perimeter * cost_m
    print()
    print("---------------------------------------")
    print()
    print("Perimeter: {:.2f}m".format(perimeter))
    print("Cost: ${:.2f}".format(cost))
    print()
    print("---------------------------------------")
    print()
    keep_going= input("press <enter> to keep going or any key to quit: ")
    print()

print()
print("Thankyou for using fence cost calculator (:")






