n=int(input("Nhập số n:"))
s3=0
if n>0:
    for i in range (2,n+1,2):
        s3+=1/(i**0.5)
    print("tổng dãy số là:",s3)
else:
    print("Xin mời nhập lại")