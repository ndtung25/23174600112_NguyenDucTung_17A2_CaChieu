so_nguyen_to = [so for so in range(2, 100) if all(so % i != 0 for i in range(2, int(so**0.5) + 1))]

print("Danh sách các số nguyên tố nhỏ hơn 100 là:", so_nguyen_to)