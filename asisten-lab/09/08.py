# => Fungsi sederhana untuk mencetak segitiga


def cetakSegitiga(ukuran=5):
    for i in range(ukuran):
        for j in range(i + 1):
            print("*", end="")

        print()


cetakSegitiga()

print()  # => Jarak

cetakSegitiga(3)
