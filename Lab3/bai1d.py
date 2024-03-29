n=int(input("Nhập số n:"))
s4=0
if n>0:
    for i in range (1,n+1):
        s4+=((-1)**(i+1))/i
    print("tổng dãy số là:",s4)
else:
    print("Xin mời nhập lại")