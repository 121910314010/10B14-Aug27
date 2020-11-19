# creating a function for insertion

def insertion_sort(l1):
    for i in range(1,len(l1)):
        val = l1[i]

        j=i-1

        while j>=0 and val < l1[j]:
            l1[j+1] = l1[j]
            j = j-1

        l1[j+1] = val
    return l1

l1 = [10,5,11,85,96]
print("Unsorted",l1)

print("Sorted is ", insertion_sort(l1))

Output:-
Unsorted [10, 5, 11, 85, 96]
Sorted is  [5, 10, 11, 85, 96]
