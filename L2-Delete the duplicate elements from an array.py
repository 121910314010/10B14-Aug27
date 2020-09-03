#Delete the duplicate elements from an array

#Defining the user function

list = [2, 4, 10, 20, 5, 2, 20, 4]
print("The original list is : " +str(list))

res = []
for i in list:
    if i not in res:
        res.append(i)

#printing list after removal
print("The list after removing duplicates : " + str(res))

Output:-
The original list is : [2, 4, 10, 20, 5, 2, 20, 4]
The list after removing duplicates : [2, 4, 10, 20, 5]
