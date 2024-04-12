str1=input("Nhập chuỗi thứ nhất:")
str2=input("Nhập chuỗi thứ hai:")
chuoi_ngan_nhat=""
min_length=min(len(str1),len(str2))
for i in range(min_length):
    if str1[i]==str2[i]:
        chuoi_ngan_nhat+=str1[i]
    else:
        break
print(f"Chuỗi ký tự con chung có độ dài ngắn nhất là: {chuoi_ngan_nhat}")