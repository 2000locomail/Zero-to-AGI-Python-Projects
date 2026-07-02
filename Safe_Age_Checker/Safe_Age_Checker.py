def check_user_age():
    try :
        age = int(input("Enter Your age: "))
        print(f"Vaild age entered: {age}")
    except ValueError:
        print("Error : Invalid input! Please enter number only.")

if __name__ == '__main__':
    check_user_age()