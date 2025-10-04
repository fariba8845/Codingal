paid_amount= float(input("Please enter paid amount: "))
total_cost= float(input("Please enter the total cost: "))

def calc(x,y):
    if x<y:
        print("total cost was not paid")
    else:
        print("Your change is: ", x-y)
       

calc(paid_amount,total_cost)