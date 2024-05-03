kho = {
 "banana": 6,
 "apple": 5,
 "orange": 32,
 "pear": 15
}
gia_tien = {
 "banana": 4,
 "apple": 2,
 "orange": 1.5,
 "pear": 3
}
hoa_don = 0
for mat_hang, so_luong in kho.items():
    don_gia = gia_tien[mat_hang]
    thanh_tien = so_luong * don_gia
    hoa_don += thanh_tien
    print(f"Mặt hàng: {mat_hang}, Số lượng: {so_luong}, Đơn giá: {don_gia}, Thành tiền: {thanh_tien}")

print(f"Tổng hóa đơn: {hoa_don}")