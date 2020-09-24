
# binary searching
def Binary_search(mylist,key):
    low = 0
    high =len(mylist)-1
    while low <= high:
        mid=(low+high)//2  # find mid index
        if mylist[mid]==key:
            return mid
        elif key>mylist[mid]:
            low=mid-1
        else:   
            high=mid-1
    return -1  # if no match return -1
mylist=[10,20,30,40,50,60]
print(mylist)
key = (int(input("enter number to search :")))
x = Binary_search(mylist,key)
if (x==-1):
    print("element is not in list")
else:
    print("element is at index",x)

Output:-
[10, 20, 30, 40, 50, 60]
enter number to search :30
element is at index 2
