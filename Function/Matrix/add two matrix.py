def generate_matrix(noOfRows, x):
    print("Enter the values of matrix -", (x+1))
    matrix = []
    for i in range(noOfRows):
        row = []
        for j in range(noOfRows):
            row.append(int(input()))
        matrix.append(row)
    return matrix


noOfRows = int((input("How many rows = ")))
m1 = generate_matrix(noOfRows, 0)
m2 = generate_matrix(noOfRows, 1)

sum = []

for x in range(noOfRows):
    row = []
    for y in range(noOfRows):
        row.append(m1[x][y] + m2[x][y])
    sum.append(row)
print(sum)

