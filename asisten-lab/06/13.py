# => Perjumlahan matriks 2x2

matriksA = [
    [1, 2], 
    [3, 4]
]

matriksB = [
    [9, 2],
    [3, 5]
]

hasil = [
    [0, 0],
    [0, 0]
]

for indexBaris in range(len(matriksA)):
    for indexKolom in range(len(matriksA[0])):
        hasil[indexBaris][indexKolom] = matriksA[indexBaris][indexKolom] + matriksB[indexBaris][indexKolom]


print(hasil)