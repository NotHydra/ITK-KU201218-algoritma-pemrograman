from random import randint

numbers = []
i = 1
while i <= 100:
    numbers.append(randint(1, 151))

    i = i + 1

minValue = numbers[1 - 1]
i = 1
while i <= 100:
    if minValue > numbers[i - 1]:
        minValue = numbers[i - 1]

    i = i + 1

print(numbers, minValue)
