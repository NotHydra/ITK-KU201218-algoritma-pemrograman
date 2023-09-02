nilai = int(input("Nilai: "))
print()

if 90 <= nilai <= 100:
    pangkat = "A"

elif 80 <= nilai <= 89:
    pangkat = "B"

elif 70 <= nilai <= 79:
    pangkat = "C"

elif 60 <= nilai <= 69:
    pangkat = "D"

else:
    pangkat = "F"

print(f"Pangkat: {pangkat}")
