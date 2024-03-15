def tinh_toan():
    so_tien_ban_dau=10000
    lai_suat=0.06
    amount_after_5_years=so_tien_ban_dau*(1+lai_suat)**5
    amount_after_10_years=so_tien_ban_dau*(1+lai_suat)**10
    growth_rate=amount_after_10_years/amount_after_5_years
    print("Số tiền có sau 5 năm là:",round(amount_after_5_years, 2))
    print("Số tiền có sau 10 năm là:",round(amount_after_10_years, 2))
    print("Tỷ lệ tăng trưởng sau 10 năm so với sau 5 năm là:",round(growth_rate, 2))
tinh_toan()