order = int(input("jumlah order hari ini: "))
tarif = int(input("tarif per order: "))

pendapatan = order * tarif

print("pendapatan hari ini sebesar:", pendapatan)

stock = int(input("berapa banyak stock hari ini: "))
laku = int(input("berapa banyak yang terjual: "))
harga = int(input("berapa harga per pcs: "))

selisih = stock - laku
target_jual = selisih * harga 

print("pendapatan yang belum laku sebesar:", target_jual)