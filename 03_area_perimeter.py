


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
                print()
        
        except ValueError:
            print(error)

#main routine goes here

print("===============================")
print("---Area-perimeter-calculator---")
print("===============================")

keep_going = ""
while keep_going == "":


    width = num_check( "Width: ")
    height = num_check("Height: ")
    print()

    #calculator

    area = width * height
    perimeter = 2 * (height+width)
    print("Area: {:.2f} square units".format(area))
    print("Perimeter: {:.2f} units".format(perimeter))

    print()
    keep_going= input("press <enter> to keep going or any key to quit: ")
    print()

print()
print("Thankyou for using area/perimeter calculator (:")






