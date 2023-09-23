numbers = []
i = 1
total = 0
while i <= 100:
    numbers.append(int(input()))

    total = total + numbers[i - 1]

    i = i + 1

average = total / 100

print(average)
