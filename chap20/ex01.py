def letter_count(s):
    count = {}
    split = [char for char in s]
    new_str = ''.join(split)
    split = new_str.split(' ')      # remove space ' '
    new_str = ''.join(split)
    new_str = new_str.lower()

    for letter in new_str:
        count[letter] = count.get(letter, 0) + 1

    result = list(count.items())
    result.sort()

    for t in result:
        print('{0}\t{1}'.format(t[0], t[1]))

s = 'ThiS is String with Upper and lower case Letters'
letter_count(s)
