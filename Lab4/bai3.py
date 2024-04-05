n=int(input("Nhập số nguyên:"))
so_chu_so=0
while n>0:
    n//=10
    so_chu_so+=1
print(f"Số chữ số của số nguyên là:{so_chu_so}")    