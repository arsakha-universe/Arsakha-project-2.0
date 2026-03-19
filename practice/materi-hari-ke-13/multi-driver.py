drivers = [
    {"nama": "hafizh", "order": 11, "pendapatan": 1300000},
    {"nama": "taufik", "order": 9, "pendapatan": 650000},
    {"nama": "arsakha", "order": 15, "pendapatan":2150000}
]

for driver in drivers:
    rata_rata = driver["pendapatan"] / driver ["order"]
    print(driver["nama"], "=", rata_rata)
