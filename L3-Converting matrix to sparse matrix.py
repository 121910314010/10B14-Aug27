# Python program to convert a matrix to sparse


def displayMatrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()




def convertToSparseMatrix(matrix):

    sparseMatrix = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] != 0:

                temp = []


                temp.append(i)
                temp.append(j)
                temp.append(matrix[i][j])


                sparseMatrix.append(temp)

            # displaying the sparse matrix
    print("\nSparse Matrix: ")
    displayMatrix(sparseMatrix)


# initializing a normal matrix
normalMatrix = [[1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 3, 0],
                [0, 0, 0, 4],
                [5, 0, 0, 0]]

# displaying the matrix
displayMatrix(normalMatrix)

# converting the matrix to sparse
# displayMatrix
convertToSparseMatrix(normalMatrix)

Output:-
1 0 0 0 
0 2 0 0 
0 0 3 0 
0 0 0 4 
5 0 0 0 

Sparse Matrix: 
0 0 1 
1 1 2 
2 2 3 
3 3 4 
4 0 5 
