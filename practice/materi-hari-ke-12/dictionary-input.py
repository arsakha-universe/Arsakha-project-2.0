nama = input("nama driver: ")
order = int(input("jumlah order: "))
pendapatan = int(input("total pendapatan: "))

driver = {
    "nama": nama,
    "order": order,
    "pendapatan": pendapatan
}

rata_rata = driver["order"] / driver["pendapatan"]

print("nama", driver["nama"])
print("pendapatan:", rata_rata)

bonus = 0 

if driver["order"] >= 15:
    bonus = 100000

total = pendapatan + bonus

print("total pendapatan", total)