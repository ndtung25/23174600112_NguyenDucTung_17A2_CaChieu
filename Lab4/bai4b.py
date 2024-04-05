n=int(input("Nhập số nguyên n(n>10):"))
s2=0
a=1
while n>10:
    if a<=n:
        s2+=1/(3**a)
        a+=2
    else:
        break
print("S2=",s2)