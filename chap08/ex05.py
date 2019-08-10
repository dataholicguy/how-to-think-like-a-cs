import string

def remove_punctuation(strng):
    """ Return a new string from a string which have no punctuation. """
    s = ''
    for char in strng:
        if char not in string.punctuation:
            s += char
    return s


def count_words(strng):
    """ Return number of words in a string which have no punctuation. """
    s = remove_punctuation(strng)
    words = s.split()
    return len(words)


def count_words_e(strng):
    """ Return number of words contain the letter 'e' in a string which have no punctuation.
        And return percentage of occurence of those words.
    """
    s = remove_punctuation(strng)
    count = 0
    words = s.split()
    for word in words:
        if 'e' in word:
            count += 1
    percentage = count / len(words) * 100
    return count, percentage


def print_result(strng):
    """ Print the result for this problem. """
    number_words = count_words(strng)
    number_words_e, percentage = count_words_e(strng)
    print('Your text contains {0} words, of which {1} ({2}%) contain an \'e\'.'.format(number_words, number_words_e, percentage))

s = """
I was born in a thunderstorm
I grew up overnight
I played alone
I played on my own
I survived
Hey
I wanted everything I never had
Like the love that comes with light
I wore envy and I hated that
But I survived
I had a one-way ticket to a place where all the demons go
Where the wind don't change
And nothing in the ground can ever grow
No hope, just lies
And you're taught to cry into your pillow
But I survived
I'm still breathing, I'm still breathing
I'm still breathing, I'm still breathing
I'm alive
I'm alive
I'm alive
I'm alive
I found solace in the strangest place
Way in the back of my mind
I saw my life in a stranger's face
And it was mine
I had a one-way ticket to a place where all the demons go
Where the wind don't change
And nothing in the ground can ever grow
No…
"""

print_result(s)
