def make_random_list():
    """ Return a new sorted list with random size and random integer elements. """
    import random
    sz = random.randint(10, 20)     # random size of list in range [10, 20]
    result = []
    for _ in range(sz):
        new_item = random.randint(0, 100)
        result.append(new_item)
    result.sort()
    return result

l1 = make_random_list()
l2 = make_random_list()

# a, Return only those items that are present in both lists.
def find_both_list_words(list1, list2):
    """ Both the vocab and wds must be sorted.  Return a new
        list of words that are present in both lists.
    """
    result = []
    xi = 0
    yi = 0

    while True:
        if xi >= len(list1):
            result.extend(list2[yi:])
            return result

        if yi >= len(list2):
            result.extend(list1[xi:])
            return result

        if list1[xi] <= list2[yi]:
            result.append(list1[xi])
            xi += 1
        else:
            result.append(list2[yi])
            yi += 1

both = find_both_list_words(l1, l2)
print('List1:', l1)
print('List2:', l2)
print('Both:', both)
print('-' * 100)
