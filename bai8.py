def calculate_probabilities(total_balls, red_balls, blue_balls, yellow_balls):
    # Tính tổng số cách có thể rút bóng
    total_outcomes = total_balls * (total_balls - 1) * (total_balls - 2)

    # Tính số cách rút tất cả là bi đỏ
    red_only_outcomes = red_balls * (red_balls - 1) * (red_balls - 2)

    # Tính số cách rút ít nhất một viên bi xanh
    at_least_one_blue_outcomes = total_outcomes - (total_balls - blue_balls) * \
                                 (total_balls - blue_balls - 1) * (total_balls - blue_balls - 2)

    # Tính số cách rút đúng hai viên là bi vàng
    exactly_two_yellow_outcomes = yellow_balls * (yellow_balls - 1) * \
                                   (total_balls - yellow_balls)

    # Tính xác suất cho từng trường hợp
    red_only_probability = red_only_outcomes / total_outcomes
    at_least_one_blue_probability = at_least_one_blue_outcomes / total_outcomes
    exactly_two_yellow_probability = exactly_two_yellow_outcomes / total_outcomes

    return red_only_probability, at_least_one_blue_probability, exactly_two_yellow_probability

def main():
    total_balls = 50
    red_balls = 20
    blue_balls = 15
    yellow_balls = 15

    print("Nhập số lượng viên bi mà bạn muốn rút ra từ hộp:")
    num_draws = int(input())

    red_only_probability, at_least_one_blue_probability, exactly_two_yellow_probability = \
        calculate_probabilities(total_balls, red_balls, blue_balls, yellow_balls)

    print("Xác suất để trong số các viên bi được rút ra:")
    print(f"1. Tất cả là bi đỏ: {red_only_probability:.4f}")
    print(f"2. Ít nhất một viên là bi xanh: {at_least_one_blue_probability:.4f}")
    print(f"3. Đúng hai viên là bi vàng: {exactly_two_yellow_probability:.4f}")

if __name__ == "__main__":
    main()
