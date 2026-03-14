user = ""

while user != "hapis":
    user = input("masukan user id anda: ")

password = ""

while password != 123:
    password = int(input("masukan password anda: "))
print("selamat datang hapis")

total = 0

for i in range (10):
    order = int(input("masukan jumlah order hari ini: "))
    total = total + order

    print("total orderan masuk sebanyak:", total)