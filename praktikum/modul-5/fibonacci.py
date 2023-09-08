n = int(input())

print("1", end="")

firstValue = 1
secondValue = 1
tempValue = 1
for i in range(n - 1):
    tempValue = secondValue
    secondValue = firstValue + secondValue
    firstValue = tempValue

    print(f", {firstValue}", end="")
