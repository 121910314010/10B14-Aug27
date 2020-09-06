#Search for an element in an array by calling function

from numpy import*
from array import*
def find_array(n):

    k = 0
    for e in arr:
        if e == n:
            print("Index of the value you searched for:")
            print(k)
            break
        k += 1
    else:
        print("Enter correct element:")

arr = array('i',[])
num = int(input("Enter the length of array:"))
for i in range(num):
    l = int(input("Enter next value:"))
    arr. append(l)
print(arr)
n = int(input("Enter the number to search:"))
find_array(n)

Output:-
Enter the length of array:5
Enter next value:2
Enter next value:8
Enter next value:9
Enter next value:7
Enter next value:4
array('i', [2, 8, 9, 7, 4])
Enter the number to search:9
Index of the value you searched for:
2
