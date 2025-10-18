try:
 age= int(input("Enter your age: "))
except ValueError:
 print("Please enter a whole number")
except NameError:
  print("The exception is: ", ex)
except:
 print("Something went wrong")
if age%2==0:
 print("Your age is an even number")
else:
 print("your age is an odd number")