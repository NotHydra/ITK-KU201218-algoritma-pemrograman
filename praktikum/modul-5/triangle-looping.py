n = int(input())

print()
for i in range(n, 0, -1):
    print("x" * i)

print()
for i in range(n, 0, -1):
    if i % 2 == 1:
        print("x" * i)

    else:
        print("-" * i)

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
    print("x" * i)

for i in range(n - 1, 0, -1):
    print("x" * i)

print()
for i in range(n, 0, -1):
    print(". " * (i - 1), end="")
    print(i)