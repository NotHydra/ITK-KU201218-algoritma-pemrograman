# => Faktorial


def faktorialDenganPerulangan(angka):
    hasil = 1
    for i in range(1, angka + 1):
        hasil *= i

    return hasil


def faktorialDenganRekusif(angka):
    if angka <= 0:
        return 1

    else:
        return angka * faktorialDenganRekusif(angka - 1)


print(faktorialDenganPerulangan(3))
print(faktorialDenganRekusif(3))
