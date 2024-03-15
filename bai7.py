def solve_linear_equations(a1, b1, c1, a2, b2, c2):
    determinant = a1 * b2 - a2 * b1
    if determinant == 0:
        return "Hệ phương trình không có nghiệm hoặc có vô số nghiệm"
    else:
        x = (c1 * b2 - c2 * b1) / determinant
        y = (a1 * c2 - a2 * c1) / determinant
        return x, y

def main():
    print("Nhập các hệ số của hệ phương trình ax + by = c:")
    a1 = float(input("Nhập a1: "))
    b1 = float(input("Nhập b1: "))
    c1 = float(input("Nhập c1: "))
    a2 = float(input("Nhập a2: "))
    b2 = float(input("Nhập b2: "))
    c2 = float(input("Nhập c2: "))

    result = solve_linear_equations(a1, b1, c1, a2, b2, c2)
    if type(result) == tuple:
        x, y = result
        print(f"Giải hệ phương trình:\nx = {round(x, 2)}\ny = {round(y, 2)}")
    else:
        print(result)

if __name__ == "__main__":
    main()
