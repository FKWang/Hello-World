a = [1, 334, 3123, 43, 31, 5, 11]

b = [[1, 23, 42], [231, 3, 124]]

print(a)

b.sort(key=lambda x: x[1])

print(b)
print(a + b)

a = a + b

a += b