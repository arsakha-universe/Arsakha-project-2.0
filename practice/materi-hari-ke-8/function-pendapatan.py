def hitung_pendapatan(order, tarif):
    hasil = order * tarif
    return hasil

order = int(input("jumlah order: "))
tarif = int(input("tarif per order: "))

pendapatan = hitung_pendapatan(order, tarif)

print("pendapatan hari ini:", pendapatan)