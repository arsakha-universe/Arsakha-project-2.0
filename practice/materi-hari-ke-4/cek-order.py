order = int(input("jumlah order hari ini: "))

if order == 0:
    print("belum ada order")
elif order < 4:
    print("order dibawah target")
elif order < 6:
    print("order diatas target")
else:
    print("orderan sangat ramai")