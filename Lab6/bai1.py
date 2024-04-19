n=int(input("Nhập số lượng phẩn tử của mảng:"))
so_nguyen_duong=[]
print("Nhập các phần tử của mảng:")
for i in  range (n):
    so=int(input(f"Nhập phần tử thứ {i+1}: "))
    if so > 0:
        so_nguyen_duong.append(so)
    else:
        print("Đây không phải số nguyên dương. Xin mời nhập lại")

tong_chan=0
tong_le=0
for so in so_nguyen_duong:
    if so % 2 == 0:
        tong_chan+=so
    else:
        tong_le+=so
print(f"Tổng số chẵn có trong mảng là:{tong_chan}")
print(f"Tổng lẻ có trong mảng là:{tong_le}")