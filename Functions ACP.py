#functions
def circumference():
    r= float(input("Please enter your radius: "))
    cf= 2*3.14*r
    print(cf)
def perimeter_of_rectangle():
    l= float(input("Enter the length of the rectangle: "))
    b= float(input("Please enter the breadth of the rectangle"))
    pm= 2*b(l+b)
    print("The perimeter of the rectangle is: ", pm)
def perimeter_of_square():
    sl=float(input("Enter the length of one side"))
    prm= sl*4
    print("The Perimeter of the square is: ", prm)
#choices 
print("a. Calculate the circumference of a circle")
print("b. Calculate the perimeter of a rectangle")
print("c. Calculate the perimeter of a square")

choice= input("Please enter your choice: ")
#conditional statements
if choice=="a":
    circumference()
elif choice=="b":
    perimeter_of_rectangle()
elif choice=="c":
    perimeter_of_square()
else:
    print("invalid choice")