def num_check(question):
    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


keep_going = ""
while keep_going == "":

    # get width and height and check they are more than zero
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost / m: ")

    # calculate cost and perimeter...
    perimeter = 2 * (width + length)
    price = (perimeter * cost)
    # output results to user
    print()
    print(f"Perimeter: {perimeter:.2f} units")
    print(f"Price: ${price:.2f}")

    # ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

print("Thank you for using the area / perimeter calculator")
