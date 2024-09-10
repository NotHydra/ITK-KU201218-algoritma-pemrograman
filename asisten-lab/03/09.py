# => if statement bersarang

umur = 9
batasUmur = 18

if umur >= batasUmur:
    print("Umur lu udah aman", end="")

    if umur > 40:
        print(", karena sudah 40an")

    elif umur > 30:
        print(", karena sudah 30an")

    else:
        print(", pokoknya udah aman")

elif umur < batasUmur:
    print("Umur lu belum aman", end="")

    if umur < 10:
        print(", karena masih dibawah 10 tahun")

    elif umur < 15:
        print(", karena masih dibawah 15 tahun")

    else:
        print(", pokoknya belum aman")
