number = [2,3,4,5,6]
def cubic_number(number):
    return number ** 3
cubic_numbers_list = [cubic_number(num) for num in number]
print(cubic_numbers_list)