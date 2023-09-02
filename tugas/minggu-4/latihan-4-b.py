nilai = int(input("Nilai: "))
print()

if nilai >= 90 and nilai <= 100:
    pangkat = "A"

elif nilai >= 80 and nilai <= 89:
    pangkat = "B"

elif nilai >= 70 and nilai <= 79:
    pangkat = "C"

elif nilai >= 60 and nilai <= 69:
    pangkat = "D"

else:
    pangkat = "F"

print(f"Pangkat: {pangkat}")
