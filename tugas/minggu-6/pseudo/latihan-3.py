from random import randint

numbers = []
i = 1
while i <= 100:
    numbers.append(randint(1, 151))

    i = i + 1

maxValue = numbers[1 - 1]
i = 1
while i <= 100:
    if maxValue < numbers[i - 1]:
        maxValue = numbers[i - 1]

    i = i + 1

print(maxValue)
