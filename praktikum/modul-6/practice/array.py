myArray = ["Rizky", "Irswanda", "Ramadhana"]

print(myArray[0])

myArray[1] = "Alfonso"
print(myArray)

myArray.append("Fernande")
print(myArray)

myArray.insert(1, "Wantonio")
print(myArray)

myArrayAnother = ["1", "1", "5"]
myArray.extend(myArrayAnother)
print(myArray, myArrayAnother)

myArray.remove("Rizky")
print(myArray)

myArray.pop(2)
print(myArray)

del myArray
# print(myArray)

myArrayOther = ["Balikpapan", "Utara"]
# print(myArrayOther)
# myArrayOther.clear()
print(myArrayOther)

print(len(myArrayOther))
print(myArrayOther)
myArrayOther.sort()
print(myArrayOther)

myArrayOther.reverse()
print(myArrayOther)

myArrayNew = myArrayOther.copy()
print(myArrayNew)