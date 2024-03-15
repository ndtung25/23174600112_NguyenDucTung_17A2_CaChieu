def nhap_toa_do_dinh():
    print("Nhập tọa độ của đỉnh M:")
    x_m = float(input("x_M = "))
    y_m = float(input("y_M = "))
    print("Nhập tọa độ của đỉnh N:")
    x_n = float(input("x_N = "))
    y_n = float(input("y_N = "))
    print("Nhập tọa độ của đỉnh P:")
    x_p = float(input("x_P = "))
    y_p = float(input("y_P = "))
    print("Nhập tọa độ của đỉnh Q:")
    x_q = float(input("x_Q = "))
    y_q = float(input("y_Q = "))
    return (x_m, y_m), (x_n, y_n), (x_p, y_p), (x_q, y_q)

def tinh_trung_diem(a, b):
    x_tđ = (a[0] + b[0]) / 2
    y_tđ = (a[1] + b[1]) / 2
    return x_tđ, y_tđ

def tinh_toan():
    M, N, P, Q = nhap_toa_do_dinh()
    trung_diem_MN = tinh_trung_diem(M, N)
    trung_diem_NP = tinh_trung_diem(N, P)
    trung_diem_MP = tinh_trung_diem(M, P)
    trung_diem_PQ = tinh_trung_diem(P, Q)
    print("Tọa độ trung điểm của cạnh MN là:", trung_diem_MN)
    print("Tọa độ trung điểm của cạnh NP là:", trung_diem_NP)
    print("Tọa độ trung điểm của cạnh MP là:", trung_diem_MP)
    print("Tọa độ trung điểm của cạnh PQ là:", trung_diem_PQ)

tinh_toan()
