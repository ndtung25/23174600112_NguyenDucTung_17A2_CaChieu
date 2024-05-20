def is_odd(n):
    return n % 2 != 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_numbers = filter(is_odd, numbers)

squares = map(lambda x: x ** 2, odd_numbers)

squares_list = list(squares)

print("Danh sách bình phương của các số lẻ:", squares_list)
