def hitung_pendapatan(order, tarif):
    print("function sedang berjalan")
    return order * tarif

while True:

    order=int(input("jumlah order: "))
    tarif=int(input("tarif per order: "))

    pendapatan = hitung_pendapatan(order, tarif)

    print("pendapatan hari ini:", pendapatan)

    lagi = input("hitung lagi? (y/n): ")

    if lagi == "n":
        break