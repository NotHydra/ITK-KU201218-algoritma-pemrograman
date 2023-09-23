numbers = []
i = 1
total = 1
while i <= 100:
    numbers.append(int(input()))

    total = total * numbers[i - 1]
    i = i + 1


print(total)
