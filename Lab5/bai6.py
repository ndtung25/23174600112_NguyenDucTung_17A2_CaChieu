string=input("Nhập một chuỗi:")
special_characters={}
tong_so_ky_tu = len(string)
for char in string:
    if not char.isalnum():
        if char in special_characters:
            special_characters[char] += 1
        else:
            special_characters[char] = 1
for char in special_characters:
    so_lan_xuat_hien = special_characters[char]
    ty_le_phan_tram = so_lan_xuat_hien / tong_so_ky_tu * 100
    print(f"Ky tu dac biet '{char}' xuat hien {so_lan_xuat_hien} lan ({ty_le_phan_tram:.2f}% trong chuoi)")