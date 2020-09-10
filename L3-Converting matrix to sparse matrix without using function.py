#Converting matrix to sparse matrix without using function

normalMatrix = [[12, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 29, 3, 0],
                [0, 0, 4, 4],
                [5, 0, 0, 0]]
for row in normalMatrix:
    for element in row:
        print(element, end=" ")
    print()

sparseMatrix=[]
for i in range(len(normalMatrix)):
    for j in range(len(normalMatrix[0])):
        if normalMatrix[i][j] != 0:

            temp = []
            temp.append(i)
            temp.append(j)
            temp.append(normalMatrix[i][j])
            sparseMatrix.append(temp)


print("\nSparse Matrix: ")
for row in sparseMatrix:
    for element in row:
        print(element, end=" ")
    print()
    
 Output:-
12 0 0 0 
0 2 0 0 
0 29 3 0 
0 0 4 4 
5 0 0 0 

Sparse Matrix: 
0 0 12 
1 1 2 
2 1 29 
2 2 3 
3 2 4 
3 3 4 
4 0 5 
