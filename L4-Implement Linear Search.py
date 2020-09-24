#Implement Linear Search

def Linear_search(my_list, key):
    for i in range(len(my_list)):
        if (my_list[i] == key):
            print(key, "is found at index", i)
            return i
            break
    return -1


my_list = [12, 22, 45, 67, 89]
print(my_list)
key = (int(input("enter the number to be searched:")))
L1 = Linear_search(my_list, key)
if (L1 != -1):
    print(key, "is found at position", L1 + 1)
else:
    print(key, "is not present")
print("searching completed")

Output:-
[12, 22, 45, 67, 89]
enter the number to be searched:22
22 is found at index 1
22 is found at position 2
searching completed
