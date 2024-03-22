a=float(input("Nhập hệ số a:"))
b=float(input("Nhập hệ số b:"))
if a==0:
    if b==0:
        print("Pt vô số nghiệm")
    else:
        print("Pt vô nghiệm")
else :
    x=-b/a
    print("Nghiệm của pt là:",x)
    