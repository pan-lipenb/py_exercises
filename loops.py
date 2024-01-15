a = [1, 2, 3, 4, 5]
b = [1, 2, 3]
list(iter(a))
for i, j in zip(a, b):
    if i == 3:
        continue
    print(i)
# print(a+b)