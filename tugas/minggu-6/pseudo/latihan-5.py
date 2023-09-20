from random import randint

numbers = []
i = 1

while i <= 100:
    numbers.append(randint(1, 151))

    i = i + 1

print(numbers, len(numbers))
print()

while True:
    switchCount = 0
    i = 2

    while i <= 100:
        tempPrevious = numbers[i - 1 - 1]
        tempCurrent = numbers[i - 1]

        if tempPrevious > tempCurrent:
            numbers[i - 1] = tempPrevious
            numbers[i - 1 - 1] = tempCurrent

            switchCount += 1

        i += 1

    if switchCount == 0:
        break

print(numbers, len(numbers))
