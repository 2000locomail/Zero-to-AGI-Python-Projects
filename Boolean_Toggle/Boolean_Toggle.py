# Authenticate user via password check and toggle login state.

def authenticate_user():

    is_logged_in = False
    correct_password = "AGI2026"
    while not is_logged_in:
        user_input = input("Enter Password: ")
        if user_input == correct_password:
            is_logged_in = True
            print("Access Granted!")
            break  # Loop yahan terminate ho jayega
        else:
            print("Incorrect Password. Try again.")

if __name__ == '__main__':
    authenticate_user()
    print("=" * 40)