print("các số chính phương từ 1 đến 1000 là:")
for i in range(1,1001):
    a=i**0.5
    if a==int(a):
        print(i,end=' ')