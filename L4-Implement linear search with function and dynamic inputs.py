#Implement linear search with function and dynamic inputs.
my_list = []
for i in range(0,4) :
    x=input("enter elements to add in list :")
    x = int(x)
    my_list.append(x)
    print("elements")
    print(my_list) # all elements are added
def Linear_search(my_list,key):
    for i in range(len(my_list)):
        if(my_list[i]==key):
            print(key,"is found at index",i)
            return i
            break
    return -1
#my_list = int(input("enter a list",))
#print(my_list)
key=(int(input("enter the number to be searched:")))
L1=Linear_search(my_list,key)
if(L1!=-1):
    print(key, "is found at position",L1+1)
else :
    print(key, "is not present")
print("searching completed")

Output:-
enter elements to add in list :10
elements
[10]
enter elements to add in list :20
elements
[10, 20]
enter elements to add in list :30
elements
[10, 20, 30]
enter elements to add in list :25
elements
[10, 20, 30, 25]
enter the number to be searched:10
10 is found at index 0
10 is found at position 1
searching completed
