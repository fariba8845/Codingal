r= float(input("Please enter a radius: "))
def circumference(r):
    return 2*3.14*r
print(circumference(9))

def weather():
    print("weather is pleasant in " ,spring)
    print("the weather is the same in ",autumn)
spring= "auntumn"
autumn="winter"
weather()

def add(P,Q):
    return P+Q
def substract(P,Q):
    return P-Q
def multiply(P,Q):
    return P*Q
def divide(P,Q):
    return P/Q

print("Please select an operation")
print("a. Addition")
print("b. Substraction")
print("c. Multiplication")
print("d. Division")

choice= input("Please enter your choice(a/b/c/d)")
num_1= float(input("Please enter the first number: "))
num_2= float(input("Please enter the second number: "))

if choice== "a":
    print(num_1,"+", num_2, "=", add(num_1, num_2))
elif choice == "b":
    print(num_1,"-",num_2,"=", substract(num_1, num_2))
elif choice == "c":
    print(num_1,"*",num_2,"=", multiply(num_1, num_2))
elif choice == "d":
    print(num_1,"/",num_2,"=", 
    divide(num_1, num_2))
else:
    print("invalid input")





