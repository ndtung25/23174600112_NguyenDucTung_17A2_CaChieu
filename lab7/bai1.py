n=int(input("Nhập số nguyên n: "))
dictionary={x:x**3 for x in range (1,n+1)}
print("Từ điển dạng như sau:")
for key,value in dictionary.items():
    print(key,":",value)