def small(list1):
    lowest = list1[0]
    lowest2 = None
    for i in list1[1:] :
        if i < lowest:
            lowest2 = lowest
            lowest = i
        elif lowest2 == None or lowest2 > i:
            lowest2 = i
    print("smallest element is",lowest)
    print("second smallest ",lowest2)

list1 = [12,2,65,31,10,8,6,4]
small(list1)

Output:-
smallest element is 2
second smallest  4
