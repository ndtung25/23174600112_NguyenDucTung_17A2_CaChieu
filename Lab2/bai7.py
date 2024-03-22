chieu_cao=float(input("Nhập chiều cao của bạn (mét):"))
can_nang=float(input("Nhập cân nặng của bạn (kg):"))
bmi=can_nang / (chieu_cao ** 2)
if bmi < 18.5:
  phan_loai="Gầy"
elif bmi < 25.0:
  phan_loai="Bình thường"
elif bmi < 30.0:
  phan_loai="Hơi béo"
else:
  phan_loai="Béo"
print(f"Chỉ số BMI của bạn là: {bmi:.2f}")
print(f"Phân loại BMI: {phan_loai}")