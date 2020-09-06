#Concatenate multiple arrays

from numpy import*
from array import*
arr = array('i',[])
num = int(input("Enter the length of first array:"))
for i in range(num):
    l = int(input("Enter the next value:"))
    arr.append(l)
print(arr)

arr2 = array('i',[])
num2 = int(input("Enter the length of second array:"))
for i in range(num2):
    k = int(input("Enter the next value:"))
    arr.append(k)
print(arr2)

print("Concatenated array is:")
print(concatenate([arr, arr2]))

Output:-
Enter the length of first array:3
Enter the next value:5
Enter the next value:3
Enter the next value:5
array('i', [5, 3, 5])
Enter the length of second array:2
Enter the next value:5
Enter the next value:5
array('i')
Concatenated array is:
[5 3 5 5 5]
