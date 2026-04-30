# HEALTH-TECH ANALYSER (BMI)


try:
    name = input("Enter your name: ")
    weight = float(input(f"Hello! {name} please enter your weight (in kg): "))
    height = float(input(f"Hello! {name} please enter your height (in m): "))
    bmi = weight/(height**2)
    print(f"{name}'s Health Report. Your BMI Score: {bmi:.2f}")

    # Optimized Comparison Logic
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"

    print(f"Status: You are {category}.")

except ZeroDivisionError:
    print("Error: Height cannot be zero!")
except ValueError:
    print("Error: Please enter numbers only for weight and height.")
