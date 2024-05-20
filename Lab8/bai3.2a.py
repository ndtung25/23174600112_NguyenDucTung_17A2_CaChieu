def cubesum(n):
    digits = str(n)
    total = sum(int(digit) ** 3 for digit in digits)
    return total

def PrintArmstrong():
    for num in range(1, 1000):
        if cubesum(num) == num:
            print(num)

PrintArmstrong()
