n=int(input("Nhập số nguyên n(n>10):"))
s3=0
a=1
while n>10:
    if a<=n:
        s3=((-1)**a)*(a**2)
        a+=1
    else:
        break
print("S3=",s3)