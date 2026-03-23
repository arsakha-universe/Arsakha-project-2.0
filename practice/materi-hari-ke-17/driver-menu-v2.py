drivers = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah Driver")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama driver: ")

        orders = []

        while True:
            tarif = int(input("Masukan besaran tarif: "))
            orders.append(tarif)

            lagi = input("Tambah order lagi? (y/n): ")
            if lagi == "n":
                break
        
        driver = {
            "nama": nama,
            "orders": orders
        }

        drivers.append(driver)
        print("Driver berhasil ditambahkan")

    elif pilihan == "2":
        print("\nData Driver:")

        for driver in drivers:
            total = sum(driver["orders"])
            print(driver["nama"], ":", total)

    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak valid")