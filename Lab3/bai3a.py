for so in range(100, 1001):
    if so>1:
        so_nguyen_to = True
    for i in range(2, int(so**0.5) + 1):
        if so % i == 0:
            so_nguyen_to = False
            break
    if so_nguyen_to:
        print(so,end=' ')
