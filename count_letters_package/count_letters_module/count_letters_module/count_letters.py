def count_letters(text, letters):
    result = {}
    for letter in letters:
        result[letter] = text.count(letter)

    return result