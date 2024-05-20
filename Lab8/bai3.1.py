def cubesum(n):
    digits = str(n)
    total = sum(int(digit) ** 3 for digit in digits)
    return total

num=int(input("Nhập vào 1 số: "))
result = cubesum(num)
print(f"Tổng các lập phương của các chữ số của {num} là: {result}")
