# PROJECT: CHRONOS LEAP CHECKER

year = int(input("Enter Year: "))

if year % 100 == 0:

    if year % 400 == 0:
        print(f"{year} is a leap Year")
    else:
        print(f"{year} is Not a leap year.")
elif year % 4 == 0:
    print(f"{year} is a leap Year")
else:
    print(f"{year} is Not a leap year.")