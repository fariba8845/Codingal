try:
    age = int(input("Enter your age: "))
    if age % 2 == 0:
        print("Your age is an even number.")
    else:
        print("Your age is an odd number.")
except ValueError:
    print("Value Error: Please enter a valid whole number")
except Exception as ex:
    print("Something went wrong:", ex)
