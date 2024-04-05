so_le=[]
so_chan=[]
sum=0
so_luong=0
while sum<=1000:
    n=int(input("Nhập số nguyên dương:"))
    if n%2!=0:
        so_le.append(n)
    if n%2==0:
        so_chan.append(n)
    sum+=n
    so_luong+=1
print("Các số lẻ đã nhập là:",so_le)
print("Các số chẵn đã nhập là:",so_chan)
print("Số lượng số nguyên đã nhập là:",so_luong)
