n=int(input("Nhập số n:"))
s2=0
if n>0:
    for i in range (1,n+1):
        s2+=(1/i)
    print("tổng dãy số là:",s2)
else:
    print("Xin mời nhập lại")