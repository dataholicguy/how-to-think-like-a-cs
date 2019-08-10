def count_letters(strng, letter):
    """ Return the number of a character in a string. """
    count = 0
    for char in strng:
        if char == letter:
            count += 1
    return count

print(count_letters("banana", "a"))
