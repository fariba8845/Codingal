def multiply(tuple1,tuple2):
    result1= 1
    result2= 1
    for i in range(len(tuple1)):
        result1 *= tuple1[i]

    for i in range(len(tuple2)):
        result2 *= tuple2[i]

    print("Product of the first tuple: ", result1)
    print("Product of the second tuple: ", result2)

multiply((4,3,2,2,-1,18),(2,4,8,8,3,2,9))

    