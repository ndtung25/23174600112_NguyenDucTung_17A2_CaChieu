n=int(input("Nhập số nguyên n(n>10):"))
s1=0
a=1
while n>10:
    if a<=n:
        s1+=6**a
        a+=1
    else:
        break
print("S1=",s1)