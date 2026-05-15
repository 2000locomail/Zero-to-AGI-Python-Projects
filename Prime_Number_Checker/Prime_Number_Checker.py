# PROJECT: PRIME DETECTOR


num = int(input("Enter Number: "))

is_prime = True 

if num <= 1:
    is_prime = False 
else:
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False 
            break 


if is_prime:
    print(f"{num} is a PRIME Number.")
else:
    print(f"{num} is NOT a Prime Number.")