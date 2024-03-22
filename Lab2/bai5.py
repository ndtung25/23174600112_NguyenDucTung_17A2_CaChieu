n=int(input("Nhập số lượng người mua vé xem phim:"))
gia_ve=120000
if 2<=n<4:
    gia_ve=n*gia_ve-(n*gia_ve*0.05)
    print(f"Số tiền phải trả là:{gia_ve}")
elif 4<=n<10:
    gia_ve=n*gia_ve-(n*gia_ve*0.1)
    print(f"Số tiền phải trả là:{gia_ve}")
else:
    gia_ve=n*gia_ve-(n*gia_ve*0.2)
    print(f"Số tiền phải trả là:{gia_ve}")