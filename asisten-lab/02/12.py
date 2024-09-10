umur = input("Umur: ") # Perlu diingat bahwa input() akan memberikan Value dengan Data Type String, dapat kita cek dengan menghover Variable
tinggi = input("Tinggi lu berapa? ") # Hal yang sama berlaku disini

# Akan error, karena kita melakukan operasi matematika pada Variable dengan Data Type String
print(f"Umur anda {umur + 1000} dengan tinggi {tinggi - 100}cm")