def letter_count(word):
    count = {}
    for letter in word:
        count[letter] = count.get(letter, 0) + 1

    # Sort alphabetically
    result = list(count.items())
    result.sort()
    return result

print(letter_count('Mississipi'))
