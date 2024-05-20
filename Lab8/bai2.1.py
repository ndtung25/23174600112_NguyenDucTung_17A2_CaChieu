def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def permutation(n, r):
    if r > n:
        return 0
    return factorial(n) // factorial(n - r)
n = int(input("Nhập n: "))
r = int(input("Nhập r: "))
result = permutation(n, r)

print(f"Số hoán vị của phần tử {r} lấy từ phần tử {n} là {result}")