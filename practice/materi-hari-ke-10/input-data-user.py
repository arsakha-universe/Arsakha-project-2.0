orders = []

for i in range(7):
    order = int(input("berapa order hari ini "))
    orders.append(order)

total = 0

for order in orders:
    total = total + order
    
print("data order:", total)