print("Nhập vào dãy số nguyên của bạn, cách nhau bởi dấu phẩy:")
day_so = list(map(int, input().split(',')))
khoang_cach = day_so[1] - day_so[0]
cap_so_cong = all(day_so[i+1] - day_so[i] == khoang_cach for i in range(len(day_so) - 1))
if cap_so_cong:
    print(f"{day_so} Dãy số này tạo thành cấp số cộng.")
else:
    print(f"{day_so} Dãy số này không tạo thành cấp số cộng.")