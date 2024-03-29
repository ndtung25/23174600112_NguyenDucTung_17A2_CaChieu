a,b=0,1
print("Chuỗi Fibonacci sao cho số cuối cùng nhỏ hơn 100 là:")
for i in range(100):
    if b >= 100:
        break
    print(b,end=' ')
    a,b=b,a+b