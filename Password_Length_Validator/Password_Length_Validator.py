# Basic password validation based on character length.

password = input("Enter your Password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "@#$%^&+=!"

if len(password) < 8:
    print("Weak")
else:
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special = True

    if has_upper and has_lower and has_digit and has_special:
        print("Strong")
    else:
        print("Medium (Add Uppercase, Numbers, and Special characters)")
        if not has_upper: print("   - Missing Uppercase")
        if not has_lower: print("   - Missing Lowercase")
        if not has_digit: print("   - Missing Number")
        if not has_special: print("   - Missing Special Character (@#$%^&+=!)")
        