print("Các số hoàn hảo bé hơn 500 là:")
for so in range(2,500):
    tong_uoc=0
    for i in range(1,so):
        if so%i==0:
            tong_uoc+=i
    if tong_uoc==so:
        print(so)