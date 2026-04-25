num1 = float(input("Enter Your number 1: "))
num2 = float(input("Enter Your number 2: "))
mo = input("Enter Mathematical Operations +, -, *, /: ").strip()
if mo == "+":
    ans_sum = num1 + num2
    print (f"Answer is {num1} {mo} {num2} = {ans_sum}")
elif mo == "-":
    ans_sub = num1 - num2
    print (f"Answer is {num1} {mo} {num2} = {ans_sub}")
elif mo == "*":
    ans_mul = num1 * num2
    print (f"Answer is {num1} {mo} {num2} = {ans_mul}")
elif mo == "/":
    if num2 != 0:
        ans_div = num1 / num2
        print (f"Answer is {num1} {mo} {num2} = {ans_div}")
    else:
        print(f"Error! {num1} is Not Divisible By 0")
else:
    print("Error")