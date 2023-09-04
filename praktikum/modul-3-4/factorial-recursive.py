def factorial(number):
    if int(number) != 1:
        return number * factorial(number - 1)

    else:
        return 1


print(factorial(5))
