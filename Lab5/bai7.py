string=input("Nhập chuỗi:")
chu_thuong=0
chu_hoa=0
chu_so=0
ky_tu_dac_biet=0
for ky_tu in string:
    if ky_tu.islower():
        chu_thuong+=1
    elif ky_tu.isupper():
        chu_hoa+=1
    elif ky_tu.isdigit():
        chu_so+=1
    else:
        ky_tu_dac_biet+=1
print(f"Số lượng chữ thường là: {chu_thuong}")
print(f"Số lượng chữ hoa là: {chu_hoa}")
print(f"Số lượng chữ số là: {chu_so}")
print(f"Số lượng ký tự đặc biệt là: {ky_tu_dac_biet}")