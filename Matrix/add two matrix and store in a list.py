x = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

y = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
z = []

for i in range(3):
    for j in range(3):
        z.append(x[i][j] + y[i][j])

print(z)