val = float(input("Enter Value: "))
unit = input("Choose F/C: ").capitalize().strip()
if unit == "C":
    fahr = (val * 1.8) + 32
    print(f"{val} °C is equal to {fahr}°F")
elif unit == "F":
    celsius = (val - 32) / 1.8
    print(f"{val} °F is equal to {celsius}°C")
else:
    print("Invalid choice! Please enter 'C' or 'F'.")
