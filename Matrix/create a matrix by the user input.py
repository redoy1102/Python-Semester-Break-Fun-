matrix1 = []
matrix2 = []
sum = []

row = int(input("Enter the number of rows - "))
print("Give input of first matrix - ")
for i in range(row):
    rows = []
    for j in range(row):
        rows.append(int(input()))
    matrix1.append(rows)

print("Give input of second matrix - ")
for i in range(row):
    rows = []
    for j in range(row):
        rows.append(int(input()))
    matrix2.append(rows)

for i in range(row):
    rows = []
    for j in range(row):
        rows.append((matrix1[i][j] + matrix2[i][j]))
    sum.append(rows)

print(matrix1)
print(matrix2)
print(sum)





