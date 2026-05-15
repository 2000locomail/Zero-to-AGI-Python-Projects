def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    vowel_count = 0
    consonant_count = 0
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    return vowel_count, consonant_count

if __name__ == "__main__":
    text = input("Enter a string: ")
    v, c = count_vowels_consonants(text)
    print(f"Vowels: {v}, Consonants: {c}") 