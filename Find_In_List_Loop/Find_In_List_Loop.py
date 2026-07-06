def search_tech_inventory():
    tech_items = ["neural_link","gpu_h100","quantum_chip","intel"]
    user_input = input("Enter items name: ").strip().lower()
    found = False
    for machine_item in tech_items:
        if machine_item == user_input:
            found = True
            break
    if found:
        print(f"Asset Found: '{user_input.upper()}' is available in the cluster.")
    else:
        print(f"Asset Denied: '{user_input.upper()}' not found in current inventory.")

if __name__ == '__main__':
    search_tech_inventory()