def common_letters(string1, string2):
    common_letters = set(
        [letter for letter in string1.lower() if letter in string2.lower()]
    )
    common_letters = ", ".join(common_letters)
    print(f"Common letters: {common_letters}")


common_letters("house", "computers")
