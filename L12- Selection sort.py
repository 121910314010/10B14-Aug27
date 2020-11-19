#Selection Sort
a = [64,25,55,78,96]
def selection_sort(a):
    for i in range(len(a)):

        min = i
        for j in range(i+1 , len(a)):
            if a[min] > a[j]:
                min = j
# sswap the found element with first element
        a[i],a[min] = a[min],a[i]
print("Unsorted list = ")
print(a)
selection_sort(a)

print("Sorted list =")
print(a)

Output:-
Unsorted list = 
[64, 25, 55, 78, 96]
Sorted list =
[25, 55, 64, 78, 96]
