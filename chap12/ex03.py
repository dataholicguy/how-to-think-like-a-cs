import copy

print('1. Investigate the copy.copy() method')
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.copy(old_list)

print('Old list:', old_list)
print('New list:', new_list)

old_list.append([4, 4, 4])
print('Old list:', old_list)
print('New list:', new_list)

old_list[1][1] = 'BB'
print('Old list:', old_list)
print('New list:', new_list)

print('-' * 100)
print('2. Investigate the copy.deepcopy() method')
old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list)

print('Old list:', old_list)
print('New list:', new_list)

old_list.append([4, 4, 4])
print('Old list:', old_list)
print('New list:', new_list)

old_list[1][1] = 'BB'
print('Old list:', old_list)
print('New list:', new_list)
