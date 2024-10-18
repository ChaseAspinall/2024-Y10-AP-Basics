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


width = num_check("Width: ")
height = num_check("Height: ")

print(f"Width: {width} | Height {height}")
