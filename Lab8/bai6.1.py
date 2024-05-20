def is_odd(n):
    return n % 2 != 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = list(filter(is_odd, numbers))

print("Các số lẻ trong danh sách là:", odd_numbers)
