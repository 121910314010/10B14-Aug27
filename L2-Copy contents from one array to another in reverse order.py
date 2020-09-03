#Copy the contents from one array to another array in reverse order

#Initialize array
arr1 = [1, 2, 3, 4, 5]

#Create another array arr2 with size of arr1
arr2 = [None] * len(arr1)
length = len(arr1)

#Copying all elements of one array into another
for i in range(0, length) :
    arr2[i] = arr1[length-i-1]

#Displaying elements of array arr1
print("Elements of original array :")
print(arr1)
print()

#Displaying elements of array arr2
print("Elements of new array: ")
for i in range(0, len(arr2)):
    print(arr2[i])
    
Output:-
Elements of original array :
[1, 2, 3, 4, 5]

Elements of new array: 
5
4
3
2
1
