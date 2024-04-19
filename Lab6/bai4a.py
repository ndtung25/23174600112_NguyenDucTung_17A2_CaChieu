n=int(input("Nhập số lượng số Fibonacci muốn tạo: "))
a=[0, 1] if n > 1 else [0] if n == 1 else []
[a.append(a[-1] + a[-2]) for _ in range(2, n)]
print(f"Danh sách các số Fibonacci đầu tiên là: {a}")