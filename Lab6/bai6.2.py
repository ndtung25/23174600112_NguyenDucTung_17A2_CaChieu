m=int(input("Nhập số hàng: "))
n=int(input("Nhập số cột: "))
if m != n:
    print("Ma trận vuông phải có cùng số hàng và cột")
else:
    ma_tran = []
    for i in range(m):
        row = []
        for j in range(n):
            a = int(input(f"Nhập giá trị ở vị trí [{i}, {j}]: "))
            row.append(a)
        ma_tran.append(row)
    print("Ma trận đã nhập:")
    for row in ma_tran:
        print(row)

    flag = True
    for i in range(m):
        for j in range(i, n):
            if ma_tran[i][j] != ma_tran[j][i]:
                flag = False
                break
        if not flag:
            break
    if flag:
        print("Ma trận là ma trận đối xứng")
    else:
        print("Ma trận không phải là ma trận đối xứng")