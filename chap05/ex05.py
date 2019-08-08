def get_truth(p, q, r):
    return (not(p and q)) or r

print('(not (p and q)) or r\n')
print('F F F:', get_truth(False, False, False))
print('F F T:', get_truth(False, False, True))
print('F T F:', get_truth(False, True, False))
print('F T T:', get_truth(False, True, True))
print('T F F:', get_truth(True, False, False))
print('T F T:', get_truth(True, False, True))
print('T T F:', get_truth(True, True, False))
print('T T T:', get_truth(True, True, True))
