def r_sum(nested_num_list):
    tot = 0
    for element in nested_num_list:
        if type(element) == type([]):
            tot += r_sum(element)
        else:
            tot += element
    return tot

print(r_sum([1, 2, [11, 13], 8, [10, [100]]]))
