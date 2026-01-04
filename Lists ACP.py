def rq():
    br = int(input("Enter the beginning of the range: "))
    er = int(input("Enter the end of the range: "))

    lst = []
    while br <= er:
        lst.append(br * br)
        br += 1

    final_list_even = []
    final_list_odd = []

    n = 0
    while n < len(lst):
        if lst[n] % 2 == 0:
            final_list_even.append(lst[n])
        else:
            final_list_odd.append(lst[n])
        n += 1

    print("Even squares:", final_list_even)
    print("Odd squares:", final_list_odd)

rq()



