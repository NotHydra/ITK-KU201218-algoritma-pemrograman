n = int(input())

count = 0
value = 1
while count < n:
    if value % 2 == 1:
        print(value, end=" ")
        count += 1

    value += 1
