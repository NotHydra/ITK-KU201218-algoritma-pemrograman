def fibbonaci(number):
    if number > 1:
        return fibbonaci(number - 1) + fibbonaci(number - 2)

    return number


print(fibbonaci(11))
