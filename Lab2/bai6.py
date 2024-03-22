a=int(input("Nhập số thứ nhất:"))
b=int(input("Nhập số thứ hai:"))
c=int(input("Nhập số thứ ba:"))
if a>b and a<c :
    print(f"{a} là số lớn thứ hai")
elif b>a and b<c:
    print(f"{b} là số lớn thứ hai")
else:
    print(f"{c} là số lớn thứ hai")