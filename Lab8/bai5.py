def sumPdivisors(n):
    total = 0
    for i in range(1, n):
        if n % i == 0:
            total += i
    return total

def areAmicable(a, b):
    if a == b:
        return False  # Hai số phải khác nhau
    return sumPdivisors(a) == b and sumPdivisors(b) == a

a = int(input("Nhập số thứ nhất: "))
b = int(input("Nhập số thứ hai: "))
if areAmicable(a, b):
    print(f"{a} và {b} là cặp số amicable")
else:
    print(f"{a} và {b} không phải là cặp số amicable")
