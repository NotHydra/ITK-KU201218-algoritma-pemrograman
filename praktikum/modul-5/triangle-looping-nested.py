n = int(input())

print()
for i in range(n, 0, -1):
    for j in range(i):
        print("x", end="")

    print()

print()
for i in range(n, 0, -1):
    if i % 2 == 1:
        for j in range(i):
            print("x", end="")

    else:
        for j in range(i):
            print("-", end="")

    print()

print()
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")

    print()

print()
for i in range(1, n + 1):
    for j in range(i):
        print("x", end="")

    print()

for i in range(n - 1, 0, -1):
    for j in range(i):
        print("x", end="")

    print()

print()
for i in range(n, 0, -1):
    for j in range(i - 1):
        print(". ", end="")

    print(i)
