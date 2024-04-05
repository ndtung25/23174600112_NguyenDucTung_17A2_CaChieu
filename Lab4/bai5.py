while True:
    a,b=map(float,input("Nhập 2 số từ bàn phím:").split())
    tong=a+b
    hieu=a-b
    tich=a*b
    thuong=a/b
    luy_thua=a**b
    can_bac_hai_a=a**0.5
    can_bac_hai_b=b**0.5
    print(f"Tong = {tong} \nHieu = {hieu} \nTich = {tich} \nThuong = {thuong} \nLuy thua = {luy_thua} \nCan bac hai cua a = {can_bac_hai_a} \nCan bac hai cua b = {can_bac_hai_b}")

    chuong_trinh=input("Bạn có muốn tiếp tục chương trình không(y/n):")
    if chuong_trinh=='n':
        print("Kết thúc chương trình")
        break