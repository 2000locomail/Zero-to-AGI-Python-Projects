def get_stats(num1, num2):
    total_sum = num1 + num2
    difference = num1 - num2
    return total_sum, difference
if __name__ == '__main__':
    a = float(input("Enter first matrix number: "))
    b = float(input("Enter second matrix number: "))
    calculated_sum, calculated_diff = get_stats(a, b)
    print(f"Aggregated Sum: {calculated_sum}")
    print(f"Matrix Difference: {calculated_diff}")
    