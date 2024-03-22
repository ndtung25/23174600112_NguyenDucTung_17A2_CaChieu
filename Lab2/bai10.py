the_loai_phim = ["Hành động", "Kinh dị", "Tình cảm", "Hài hước", "Hoạt hình"]
lua_chon_the_loai = int(input("Nhập số thứ tự thể loại phim bạn muốn xem (1-5): "))
thoi_gian_chieu_phim = input("Nhập thời gian muốn xem phim (sáng, trưa, chiều, tối): ").lower()
if the_loai_phim[lua_chon_the_loai - 1] == "Tình cảm" and thoi_gian_chieu_phim != "tối":
  print("Không có suất chiếu.")
elif the_loai_phim[lua_chon_the_loai - 1] == "Hoạt hình" and thoi_gian_chieu_phim not in ["sáng", "trưa"]:
  print("Không có suất chiếu.")
elif the_loai_phim[lua_chon_the_loai - 1] == "Kinh dị" and thoi_gian_chieu_phim != "tối":
  print("Không có suất chiếu.")
else:
  print(f"Bạn đã chọn xem phim {the_loai_phim[lua_chon_the_loai - 1]} vào lúc {thoi_gian_chieu_phim}.")