import math

value= float(input("Enter a value: "))
radian= math.radians(value)

sv= math.sin(radian)
cv= math.cos(radian)
tv= math.tan(radian)

print("The sine of inputted value is: ", sv)
print("The cosine of inputted value is: ", cv)
print("The tangent of inputted value is: ", tv)