m=int(input("Nhập số hàng: "))
n=int(input("Nhập số cột: "))
ma_tran = []
for i in range(m):
    row = []
    for j in range(n):
        a = int(input(f"Nhập giá trị ở vị trí [{i}, {j}]: "))
        row.append(a)
    ma_tran.append(row)

tong = 0
for i in range(len(ma_tran)):
    for j in range(len(ma_tran[i])):
        tong += ma_tran[i][j]
print(f"Tổng của các phần tử của ma trận là: {tong}")

ma_tran_chuyen_vi = [[ma_tran[i][j] for i in range(m)] for j in range(n)]
print("Ma trận chuyển vị là:")
for row in ma_tran_chuyen_vi:
    print(row)