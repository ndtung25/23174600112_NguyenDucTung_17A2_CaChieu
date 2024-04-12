a=int(input("Nhập số nguyên dương:"))
nhi_phan=""
while a>0:
    phan_du=a % 2
    nhi_phan=str(phan_du) + nhi_phan
    a //= 2
print(f"Số nhị phân của {a} là: {nhi_phan}")