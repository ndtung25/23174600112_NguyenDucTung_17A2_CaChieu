def cubesum(n):
    digits = str(n)
    total = sum(int(digit) ** 3 for digit in digits)
    return total

def isArmstrong(n):
    return cubesum(n) == n

n = int(input("Nhập một số: "))
if isArmstrong(n):
    print(f"{n} là số Armstrong")
else:
    print(f"{n} không phải là số Armstrong")
