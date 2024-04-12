chuoi = input("Nhập một chuỗi ký tự: ")
chuoi_ky_tu = ''.join(filter(str.isdigit, chuoi))

if chuoi_ky_tu:
    so = int(chuoi_ky_tu)
    if so < 2:
        so_nguyen_to = False
    else:
        so_nguyen_to = True
        for i in range(2, int(so**0.5) + 1):
            if so % i == 0:
                so_nguyen_to = False
                break
else:
    so_nguyen_to = False

if so_nguyen_to:
    print(f"Chuỗi ký tự '{chuoi_ky_tu}' là số nguyên tố.")
else:
    print(f"Chuỗi ký tự '{chuoi_ky_tu}' không phải là số nguyên tố hoặc không chứa số.")

