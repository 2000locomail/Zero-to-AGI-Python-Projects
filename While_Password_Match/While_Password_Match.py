def verify_master_gate ():
    master_password = "AGI2026"
    user_input = input("Enter Master Password: ").strip()
    while user_input != master_password:
        print("Access Denied. Invalid Token.")
        user_input = input("Try Again: ").strip()
    print("Access Granted")
if __name__ == '__main__':
    verify_master_gate()