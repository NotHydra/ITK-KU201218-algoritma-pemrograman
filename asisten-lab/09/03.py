# => Fungsi juga dapat memanggil fungsi lain di dalamnya


def cetakAsep():
    print("Asep")


def helloWorld():
    print("Hello World!")
    cetakAsep()
    cetakAsep()
    cetakAsep()


helloWorld()
helloWorld()
helloWorld()
