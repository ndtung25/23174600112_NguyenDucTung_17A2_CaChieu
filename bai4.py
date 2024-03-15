import math
def tinh_dien_tich_xung_quanh(a, h):
    l = math.sqrt(a**2 + h**2)  
    S = 0.5*a*l
    return round(S, 2)

def tinh_dien_tich_toan_phan(a, h):
    S = tinh_dien_tich_xung_quanh(a, h) 
    S_toan_phan = S+a**2 
    return round(S_toan_phan, 2)

def tinh_the_tich(a, h):
    V = (1/3)*a**2*h
    return round(V, 2)

def main():
    a = float(input("Nhập độ dài cạnh đáy của hình chóp: "))
    h = float(input("Nhập chiều cao của hình chóp: "))
    dien_tich_xung_quanh = tinh_dien_tich_xung_quanh(a, h)
    dien_tich_toan_phan = tinh_dien_tich_toan_phan(a, h)
    the_tich = tinh_the_tich(a, h)
    print("Diện tích xung quanh của hình chóp là:", dien_tich_xung_quanh)
    print("Diện tích toàn phần của hình chóp là:", dien_tich_toan_phan)
    print("Thể tích của hình chóp là:", the_tich)

main()
