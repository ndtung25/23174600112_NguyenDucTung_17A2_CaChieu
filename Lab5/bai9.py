str1 = input("Nhap chuoi 1: ")
str2 = input("Nhap chuoi 2: ")
len1 = len(str1)
len2 = len(str2)
khoang_cach = abs(len1 - len2)
if len1 == len2:
    for i in range(len1):
        if str1[i] != str2[i]:
            khoang_cach += 1
print(f"Co the thay doi chuoi 1 thanh chuoi 2 bang cach them, xoa, hoac thay doi {khoang_cach} ky tu.")