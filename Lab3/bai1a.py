n=int(input("Nhập số n:"))
s1=0
if n>0:
    for i in range (1,n+1):
        s1+=i
    print("tổng dãy số là:",s1)
else:
    print("Xin mời nhập lại")
