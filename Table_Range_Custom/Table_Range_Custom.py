def generate_multiplication_table():
    target_number = int(input("Enter the number to generate its table: "))
    for i in range(1,11):
        product = target_number * i 
        print(f"{target_number} x {i} = {product}")
if __name__ == '__main__':
    generate_multiplication_table()
