def count_letters(strng, letter):
    """ return the number of a character in a string. """
    count = 0
    start = 0
    while start < len(strng):
        if strng.find(letter, start) != -1:
            count += 1
            start = strng.find(letter, start) + 1
        else:
            start += 1
    return count

print(count_letters("banana", "a"))
print(count_letters("banana", "b"))
print(count_letters("banana", "na"))
