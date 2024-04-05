a=2
while a<100:
    so_nguyen_to=True
    b=2
    while b<a:
        if a%b==0:
            so_nguyen_to=False
            break
        b+=1
    if so_nguyen_to:
        print(a,end=' ')
    a+=1