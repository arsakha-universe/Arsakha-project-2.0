drivers = []

while True:
    nama = input("nama driver: ")
    order = int(input("jumlah order: "))
    pendapatan = int(input("jumlah pendapatan: "))
    tip = int(input("jumlah tip: "))

    driver = {
        "nama": nama,
        "order": order,
        "pendapatan": pendapatan,
        "tip": tip
    }

    drivers.append(driver)

    lanjut = input("tambah driver lagi? (y/n): ")

    if lanjut == "n":
        break

print("\nData driver:")

for driver in drivers:
    rata_rata = driver["pendapatan"] / driver["order"]
    print(driver["nama"], ":", rata_rata)

total_semua = 0

for driver in drivers:
    gabungan = driver["pendapatan"]
    total_semua += gabungan

print("Total semua:", total_semua)