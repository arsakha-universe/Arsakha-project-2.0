drivers = []

for i in range(3):
    print("driver lambung ", i+1)

    nama = input("nama: ")
    order= int(input("order: "))
    pendapatan= int(input("pendapatan: "))

    driver = {
        "nama": nama,
        "order": order,
        "pendapatan": pendapatan
    }

    drivers.append(driver)

print("\nData Driver:")

for driver in drivers:
    rata_rata = driver["pendapatan"] / driver["order"]
    print(driver["nama"],"-",rata_rata)

total_semua = 0

for driver in drivers:
    pendapatan = driver["pendapatan"]
    total_semua += pendapatan

print("tota; semua:", total_semua)