n=int(input("Nhập số lượng phần tử của mảng:"))
so_nguyen_duong=[]
print("Nhập các phần tử của mảng:")
for i in range (n):
    so=int(input(f"Nhập phần tử thứ {i+1}: "))
    if so > 0 :
        so_nguyen_duong.append(so)
    else:
        print("Đây không phải số nguyên dương. Xin mời nhập lại")

print("Các số nguyên tố trong mảng này là:")
for so in so_nguyen_duong:
    if so>1:
        so_nguyen_to = True
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                so_nguyen_to = False
                break
        if so_nguyen_to:
            print(so,end=' ')

print("\nCác số hoàn hảo trong mảng này là:")
for so in so_nguyen_duong:
    tong_uoc_so=0
    for i in range(1,so):
        if so % i == 0:
            tong_uoc_so += i
    if tong_uoc_so == so:
        print(so,end=' ')