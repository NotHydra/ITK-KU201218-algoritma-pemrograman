numbers = []
i = 1
while i <= 100:
    numbers.append(int(input()))

    if i == 1:
        minValue = numbers[i - 1]

    else:
        if minValue > numbers[i - 1]:
            minValue = numbers[i - 1]

    i = i + 1

print(minValue)
