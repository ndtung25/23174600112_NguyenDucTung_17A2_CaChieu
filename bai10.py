def tinh_xac_suat(tong_so_bi, bi_do, bi_xanh, bi_vang):
    tong_cach_rut_bi = tong_so_bi * (tong_so_bi - 1) * (tong_so_bi - 2)

    tat_ca_bi_do = bi_do * (bi_do - 1) * (bi_do - 2)

    it_nhat_mot_vien_xanh = tong_cach_rut_bi - (tong_so_bi - bi_xanh) * \
                                 (tong_so_bi - bi_xanh - 1) * (tong_so_bi - bi_xanh - 2)

    dung_hai_vien_vang = bi_vang * (bi_vang - 1) * \
                                   (tong_so_bi - bi_vang)

    xac_suat_tat_ca_bi_do = tat_ca_bi_do / tong_cach_rut_bi
    xac_suat_it_nhat_mot_vien_xanh = it_nhat_mot_vien_xanh / tong_cach_rut_bi
    xac_suat_dung_hai_vien_vang = dung_hai_vien_vang / tong_cach_rut_bi

    return xac_suat_tat_ca_bi_do, xac_suat_it_nhat_mot_vien_xanh, xac_suat_dung_hai_vien_vang

def ket_qua():
    tong_so_bi = 50
    bi_do = 20
    bi_xanh = 15
    bi_vang = 15
    print("Nhập số lượng viên bi mà bạn muốn rút ra từ hộp:")
    so = int(input())
    xac_suat_tat_ca_bi_do, xac_suat_dung_mot_vien_xanh, xac_suat_dung_hai_vien_vang = \
        tinh_xac_suat(tong_so_bi, bi_do, bi_xanh, bi_vang)
    print("Xác suất để trong số các viên bi được rút ra:")
    print(f"1. Tất cả là bi đỏ: {xac_suat_tat_ca_bi_do:.4f}")
    print(f"2. Ít nhất một viên là bi xanh: {xac_suat_dung_mot_vien_xanh:.4f}")
    print(f"3. Đúng hai viên là bi vàng: {xac_suat_dung_hai_vien_vang:.4f}")

ket_qua()
