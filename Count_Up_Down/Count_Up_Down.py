val = input("Select Direction (Up/Down):").strip().capitalize()

if val == "Up":
    for i in range (1,11):
        print(i)
elif val == "Down":
    for i in range (10, 0, -1):
        print(i)
else:
    print("SYSTEM ERROR: Invalid Direction Protocol.")