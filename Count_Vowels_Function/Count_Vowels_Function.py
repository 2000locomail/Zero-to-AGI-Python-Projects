def count_vowels(input_string):
    vowel_count = 0 
    vowels_reference = "aeiou"
    for char in input_string.lower():
        if char in vowels_reference:
            vowel_count += 1
    return vowel_count

if __name__ == '__main__':
    user_text = input("Enter your text string: ")
    total_vowels = count_vowels(user_text)
    print(f"Total Vowels Detected: {total_vowels}")
        