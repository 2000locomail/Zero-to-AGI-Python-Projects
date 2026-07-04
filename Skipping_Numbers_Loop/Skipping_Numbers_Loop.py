def filter_number():
    for num in range(1, 21):
        if num == 5 or num == 10:
            continue
        else:
            print(num)
if __name__ == '__main__':
    filter_number()

