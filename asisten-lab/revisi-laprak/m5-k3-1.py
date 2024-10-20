print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
n = int(input("Masukkan nilai N: "))

a = 0
b = 1
c = 1

for i in range(n + 1):
    print(a, end="")

    if i < n:
        print(", ", end="")

    c = b
    b = a + b
    a = c


print()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
