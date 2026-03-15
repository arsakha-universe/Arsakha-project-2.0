order = int(input("jumlah order hari ini: "))
tarif = int(input("tarif per order: "))

pendapatan = order * tarif

print("pendapatan hari ini:", pendapatan)

if pendapatan >= 500000:
    print("hari ini capai target")
elif pendapatan >= 300000:
    print("sedikit lagi target")
else:
    print("ayo semangat kejar target")