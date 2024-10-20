n = int(input("Masukkan jumlah suku deret Fibonacci: "))
a = 0
b = 1

for i in range(0, n + 1):
    if i < n:
        print(a, end=", ")

    else:
        print(a)

    c = a + b
    a = b
    b = c
