def get_vowels(input_string):
    vowel_list = "aeiou"
    vowels = set([letter for letter in input_string.lower() if letter in vowel_list])
    vowels = ", ".join(vowels)

    print(f"Vowels: {vowels}")


get_vowels("Umuzi")
