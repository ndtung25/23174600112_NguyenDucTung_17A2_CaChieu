import csv
import random

# Khởi tạo thông tin về ngựa
horses = [
    {"ma": 1, "kha_nang": 0.2, "khoang_cach": 0},
    {"ma": 2, "kha_nang": 0.3, "khoang_cach": 0},
    {"ma": 3, "kha_nang": 0.1, "khoang_cach": 0},
    {"ma": 4, "kha_nang": 0.4, "khoang_cach": 0},
    {"ma": 5, "kha_nang": 0.25, "khoang_cach": 0}
]

do_dai = 500
ket_qua = []

# Hàm để mô phỏng một vòng đua
def race():
    for horse in horses:
        if horse["khoang_cach"] < do_dai:
            move = random.random()
            if move < horse["kha_nang"]:
                horse["khoang_cach"] += random.randint(1, 10)

# Mô phỏng cuộc đua cho đến khi một con ngựa về đích
while not any(horse["khoang_cach"] >= do_dai for horse in horses):
    race()

# Sắp xếp kết quả theo thứ tự về đích
horses_sorted = sorted(horses, key=lambda x: x["khoang_cach"], reverse=True)
for i, horse in enumerate(horses_sorted):
    ket_qua.append({"vi_tri": i + 1, "ma_ngua": horse["ma"], "khoang_cach": horse["khoang_cach"]})

# Ghi kết quả vào file CSV
with open("ket_qua_cuoc_dua.csv", mode="w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["vi_tri", "ma_ngua", "khoang_cach"])
    writer.writeheader()
    for result in ket_qua:
        writer.writerow(result)

# Hiển thị kết quả cuộc đua
for result in ket_qua:
    print(f"Vị trí: {result['vi_tri']}, Mã ngựa: {result['ma_ngua']}, Khoảng cách: {result['khoang_cach']}")

