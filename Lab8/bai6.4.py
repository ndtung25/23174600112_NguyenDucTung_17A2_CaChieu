def is_even(n):
    return n % 2 == 0
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = filter(is_even, numbers)

cubes = map(lambda x: x ** 3, even_numbers)

cubes_list = list(cubes)

print("Danh sách lập phương của các số chẵn:", cubes_list)
