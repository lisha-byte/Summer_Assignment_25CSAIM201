# Program to add 2 matrices
r = int(input("Enter rows: "))
c = int(input("Enter columns: "))

print("Enter first matrix:")
mat1 = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat1.append(row)

print("Enter second matrix:")
mat2 = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(int(input()))
    mat2.append(row)

sum_mat = []
for i in range(r):
    row = []
    for j in range(c):
        row.append(mat1[i][j] + mat2[i][j])
    sum_mat.append(row)

print("Sum of matrices:")
for i in range(r):
    print(sum_mat[i])