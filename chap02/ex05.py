P = 10000
n = 12
r = 0.08

t = int(input('Number of year that the money will be compounded for: '))

amount = P * ((1 + r / n) ** (n * t))

print('Final amount: $' + str(amount))
