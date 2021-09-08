from random import randint as rint


ls = [rint(1, 100) for _ in range(10)]
print(ls)

for i in ls:
    print(i + 1)
