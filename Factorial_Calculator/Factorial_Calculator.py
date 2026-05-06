# Calculate the factorial of a given number using iterative loops.

try:
    num = int(input("Enter a number to find its factorial: "))
    if num < 0:
        print("Error: Negative numbers do not have factorials.")
    elif num == 0 or num == 1:
        print(f"The factorial of {num} is 1")
    else:
        fact = 1
        for i in range(1, num + 1):
            fact *= i
        print(f"Result: {num}! = {fact}")
        
except ValueError:
    print("Error: Invalid input!")