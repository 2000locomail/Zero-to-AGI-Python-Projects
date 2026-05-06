# Generate 'n' terms of the Fibonacci sequence using iterative swapping.

try:


    n_terms = int(input("Enter how many terms you want: "))
    # Starting values for the sequence

    a,b = 0,1
    count = 0
# Validation
    if n_terms <= 0:
        print ("Please enter a positive integer greater than 0.")
    elif n_terms == 1:
        print(f"Fibonacci sequence: {a}")
    else:
        print("Generating Fibonacci sequence: ")
        while count < n_terms:
            print(a, end=", " if count < n_terms - 1 else "\n")

            a, b = b, a+b
            count += 1


except ValueError:
    print("Error")