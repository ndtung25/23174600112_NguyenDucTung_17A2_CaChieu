so = input("Nhap so bat ky: ")
for chu_so in so:
    if chu_so in '0123456789':
        chu_so = int(chu_so)
        if chu_so == 0:
            print("zero", end=' ')
        elif chu_so == 1:
            print("one", end=' ')
        elif chu_so == 2:
            print("two", end=' ')
        elif chu_so == 3:
            print("three", end=' ')
        elif chu_so == 4:
            print("four", end=' ')
        elif chu_so == 5:
            print("five", end=' ')
        elif chu_so == 6:
            print("six", end=' ')
        elif chu_so == 7:
            print("seven", end=' ')
        elif chu_so == 8:
            print("eight", end=' ')
        elif chu_so == 9:
            print("nine", end=' ')
    else:
        print("Khong phai chu so", end=' ')