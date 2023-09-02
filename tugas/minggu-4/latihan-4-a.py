nilai = int(input("Nilai: "))
print()

if nilai < 60:
    pangkat = "F"

elif nilai < 69:
    pangkat = "D"

elif nilai < 79:
    pangkat = "C"

elif nilai < 89:
    pangkat = "B"

elif nilai < 100:
    pangkat = "A"


print(f"Pangkat: {pangkat}")
