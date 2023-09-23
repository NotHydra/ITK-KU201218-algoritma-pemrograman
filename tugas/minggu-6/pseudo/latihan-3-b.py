numbers = []
i = 1
while i <= 100:
    numbers.append(int(input()))

    if i == 1:
        maxValue = numbers[i - 1]

    else:
        if maxValue < numbers[i - 1]:
            maxValue = numbers[i - 1]

    i = i + 1

print(maxValue)
