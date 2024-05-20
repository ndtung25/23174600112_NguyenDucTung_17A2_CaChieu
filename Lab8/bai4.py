def sumPdivisors():
    a = []
    number = int(input("Nhập số bất kì: "))
    for i in range(1, number):
        if number % i == 0:
            a.append(i)
    print(a)
sumPdivisors()
