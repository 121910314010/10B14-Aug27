#Accept input of matrix from user and change to sparse matrix

a= int(input("Enter Number of rows"))
b= int(input("Enter columns"))
matrix=[]
for i in range (a):
    c=[]
    for j in range(b):
        j=int(input("Enter Number in matrix"+str(i)+" "+str(j)+" "))
        c.append(j)
    print()
    matrix.append(c)
for i in range (a):
    for j in range (b):
        print (matrix [i][j],end="")
        print()

thres=1
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] <thres+1:
            matrix[i][j]=0
sparseMatrix = []
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] != 0:
            temp = [i, j, matrix[i][j]]
            sparseMatrix.append(temp)
print(sparseMatrix)

Output:-
Enter Number of rows3
Enter columns3
Enter Number in matrix0 0 1
Enter Number in matrix0 1 2
Enter Number in matrix0 2 3

Enter Number in matrix1 0 4
Enter Number in matrix1 1 5
Enter Number in matrix1 2 6

Enter Number in matrix2 0 7
Enter Number in matrix2 1 8
Enter Number in matrix2 2 9

1
2
3
4
5
6
7
8
9
[[0, 1, 2], [0, 2, 3], [1, 0, 4], [1, 1, 5], [1, 2, 6], [2, 0, 7], [2, 1, 8], [2, 2, 9]]
