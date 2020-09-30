#Implement binary search with user function and dynamic inputs.
pos=-1

def search(list,n):

    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False



list=[]
k=int(input("Enter number of elements: "))

for i in range(0,k):
    ele=int(input("Enter the numbers in list: "))
    list.append((ele))
n=int(input("Enter the number to search: "))

if search(list,n):
    print("found at",pos+1)
else:
    print("not found")

Output:-
Enter number of elements: 5
Enter the numbers in list: 1
Enter the numbers in list: 2
Enter the numbers in list: 3
Enter the numbers in list: 4
Enter the numbers in list: 5
Enter the number to search: 5
found at 5
