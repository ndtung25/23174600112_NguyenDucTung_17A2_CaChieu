import math

def nhap_toa_do():
    x = float(input("Nhập tọa độ x:"))
    y = float(input("Nhập tọa độ y:"))
    return x, y

def tinh_phep_cong(a, b):
    return (a[0] + b[0],a[1] + b[1])

def tinh_phep_tru(a, b):
    return (a[0] - b[0],a[1] - b[1])

def tinh_do_dai_vector(v):
    return math.sqrt(v[0]**2 + v[1]**2)

def tinh_cosin_goc(a, b):
    dot_product = a[0] * b[0] + a[1] * b[1]
    cd_a = tinh_do_dai_vector(a)
    cd_b = tinh_do_dai_vector(b)
    goc_cos = dot_product / (cd_a * cd_b)
    return round(goc_cos, 2)

def tinh_toan():
    print("Nhập tọa độ của vector a:")
    a = nhap_toa_do()
    print("Nhập tọa độ của vector b:")
    b = nhap_toa_do()
    phep_cong = tinh_phep_cong(a, b)
    phep_tru = tinh_phep_tru(a, b)
    print("Phép cộng a + b:", phep_cong)
    print("Phép trừ a - b:", phep_tru)
    do_dai_a = tinh_do_dai_vector(a)
    do_dai_b = tinh_do_dai_vector(b)
    print("Độ dài của vector a:", round(do_dai_a, 2))
    print("Độ dài của vector b:", round(do_dai_b, 2))
    cosin_goc = tinh_cosin_goc(a, b)
    print("Cosin góc giữa hai vector a và b:", cosin_goc)

tinh_toan()
