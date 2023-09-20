from random import randint

numbers = []
i = 1
total = 0
while i <= 100:
    numbers.append(randint(1, 151))

    total = total + numbers[i - 1]

    i = i + 1

print(total / 100)
