def tinh_tien_dien(gio_su_dung, hieu_dien_the, cuong_do_dien):
    cong_suat = hieu_dien_the * cuong_do_dien / 1000
    nang_luong = cong_suat * gio_su_dung
    gia_dien = 5000  
    tien_dien = nang_luong * gia_dien
    return tien_dien

def tinh_toan():
    gio_su_dung = float(input("Nhập số giờ sử dụng máy lọc không khí: "))
    hieu_dien_the = 220
    cuong_do_dien = 1.5
    tien_dien = tinh_tien_dien(gio_su_dung, hieu_dien_the, cuong_do_dien)
    print("Tổng số tiền điện phải trả cho việc sử dụng máy lọc không khí là:", round(tien_dien, 2),"VND")

tinh_toan()
