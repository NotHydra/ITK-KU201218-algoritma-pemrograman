# => if statement bersarang

umur = 18
batasUmur = 18

if umur >= batasUmur and umur > 40 and umur <= 100:
    print("Umur lu udah aman, karena sudah tua")

elif umur >= batasUmur and umur > 30 and umur <= 100:
    print("Umur lu udah aman, karena sudah 30an")

elif umur >= batasUmur:
    print("Umur lu udah aman, pokoknya udah aman")

elif umur < 0 or umur > 100:
    print("Umur lu gak jelas")

else:
    print("Umur lu belum aman")
