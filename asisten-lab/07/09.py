kalimat = "lampu punya gweh"

kalimatBaru = ""

kataKata = kalimat.split(" ")
for kata in kataKata:
    kalimatBaru += kata.capitalize()

    if kata != kataKata[-1]:
        kalimatBaru += " "

print(kalimat)
print(kalimatBaru)
