def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """
    my_substitutions = the_text.maketrans(
        # If you find any of these
        "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
        # Replace them by these
        "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, 'r')
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds


book_words = get_words_in_book("alice.txt")
book_words.sort()
book_words = [word.lower() for word in book_words]

def word_count(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1

    result = list(count.items())
    result.sort()
    return result

result = word_count(book_words)
layout = '{0:20}{1:5}'
print(layout.format('Word', 'Count'))
print('=' * 25)

for i in range(60):
    print(layout.format(result[i][0], result[i][1]))

print('=' * 25)

def count_alice(words):
    count = {}
    for word in words:
        count[word] = count.get(word, 0) + 1
    return count['alice']

print('The word \'alice\' occurs {0} times in the book.'.format(count_alice(book_words)))

print('=' * 25)
def find_longest(words):
    longest = len(words[0])
    long_word = words[0]
    for word in words:
        if longest < len(word):
            longest = len(word)
            long_word = word
    return (long_word, longest)

longest_word = find_longest(book_words)
print('The word \'{0}\' is the longest word in Alice in Wonderland with {1} characters.'
        .format(longest_word[0], longest_word[1]))
