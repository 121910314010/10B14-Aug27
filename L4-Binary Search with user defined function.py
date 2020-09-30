#Binary Search with user defined function.

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


list=[1,7,8,4,12,45,99,702,10987,54866]
n=99

if search(list,n):
    print("found at",pos+1)
else:
    print("not found")
    
    Output:-
    found at 7
