def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def combination(n, r):
    if r > n:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
result = combination(n, r)

print(f"Số tổ hợp của {n} phần tử lấy {r} phần tử mỗi lần là: {result}")