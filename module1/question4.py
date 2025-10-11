#create a n* n matrix, Get i and J from user, fetch the vaue corresponding to 'i'th row and 'j'th columnn = int(input("Enter the size of the matrix (n): "))
n = int(input("enter the size of the matrix : "))
matrix_M = []
for i in range(n):
    row=[]
    for j in range(n):
        index = int(input(f"enter value of index [{i}][{j}]: "))
        row.append(index)
    matrix_M.append(row)
print("Matrix:")
for row in matrix_M:
    print(row)
i = int(input("Enter row index (starting from 0): "))
j = int(input("Enter column index (starting from 0): "))
print("Value at position [", i, "][", j, "] is:", matrix_M[i][j])
