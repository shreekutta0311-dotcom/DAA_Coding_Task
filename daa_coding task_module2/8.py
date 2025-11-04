# Matrix Multiplication (User Input)

# Step 1: Get size of first matrix
r1 = int(input("Enter number of rows for Matrix 1: "))
c1 = int(input("Enter number of columns for Matrix 1: "))

# Step 2: Get size of second matrix
r2 = int(input("Enter number of rows for Matrix 2: "))
c2 = int(input("Enter number of columns for Matrix 2: "))

# Check compatibility
if c1 != r2:
    print("Matrix multiplication not possible! Columns of Matrix 1 must equal rows of Matrix 2.")
    exit()

# Step 3: Input elements for Matrix 1
print("\nEnter elements for Matrix 1:")
A = []
for i in range(r1):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    A.append(row)

# Step 4: Input elements for Matrix 2
print("\nEnter elements for Matrix 2:")
B = []
for i in range(r2):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    B.append(row)

# Step 5: Initialize result matrix with zeros
result = [[0 for _ in range(c2)] for _ in range(r1)]

# Step 6: Multiply matrices
for i in range(r1):
    for j in range(c2):
        for k in range(c1):
            result[i][j] += A[i][k] * B[k][j]

# Step 7: Display the result
print("\nResultant Matrix (A x B):")
for row in result:
    print(row)
