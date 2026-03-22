drivers = []

while True:
    print("\n=== MENU ===")
    print("1. Tambah Driver")
    print("2. Lihat Data")
    print("3. Keluar")

    pilihan = input ("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama: ")
        order = int(input("Order: "))
        pendapatan = int(input("Pendapatan: "))
        
        driver = {
            "nama": nama,
            "order": order,
            "pendapatan": pendapatan
        }
    
        drivers.append(driver)
        print("Driver berhasil ditambahkan")
    
    elif pilihan == "2":
        print("\nData Driver:")
        for driver in drivers:
            rata_rata = driver["pendapatan"] / driver["order"]
            print(driver["nama"], "=", rata_rata)
    
    elif pilihan == "3":
        print("Program selesai")
        break

    else:
        print("pilihan tidak valid")