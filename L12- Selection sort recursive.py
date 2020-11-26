def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp


# Function to perform selection sort on list
def selectionSort(A):
    for i in range(len(A) - 1):

        # find the minimum element in the unsorted sublist[i..n-1]
        # and swap it with A[i]
        min = i

        for j in range(i + 1, len(A)):
            # if A[j] element is less, then it is the minimum
            if A[j] < A[min]:
                min = j  # update index of min element

        # swap the minimum element in sublist[i..n-1] with A[i]
        swap(A, min, i)


if _name_ == '_main_':
    A = []
    n = int(input("Enter number of elements : "))

    for i in range(0, n):
        ele = int(input())

        A.append(ele)

        selectionSort(A)

        # print the sorted list
        print(A)
