n=int(input("Nhập số nguyên n(n>10):"))
s4=0
a=1
while n>10:
    if a<=n:
        s4=a*(a+1)*(a+2)
        a+=1
    else:
        break
print("S4=",s4)