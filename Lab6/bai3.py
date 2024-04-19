print("Nhập vào dãy số của bạn, cách nhau bởi dấu phẩy: ")
day_so=list(map(float,input().split(',')))
sln=day_so[0]
snn=day_so[0]
for i in day_so:
    if sln<i:
        sln=i
    if i<snn:
        snn=i
print(f"Số lớn nhất trong dãy số là:{sln}")
print(f"Số nhỏ nhất trong dãy số là:{snn}")