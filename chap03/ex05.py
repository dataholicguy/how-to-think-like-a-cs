xs = [12, 10, 32, 3, 66, 17, 42, 99, 20]

# a, Write a loop that prints each of the numbers on a new line.
print('Print each of the numbers on a new line')
for num in xs:
    print(num)

# b, Write a loop that prints each number and its square on a new line.
print('\nPrint each number and its square on a new line')
for num in xs:
    print(num, num * num)

# c, Write a loop that adds all the numbers from the list into a variable called total.
print('\nWrite a loop that adds all the numbers from the list into a variable called total')
total = 0
for num in xs:
    total += num
print('Total:', total)

# d, Print the product of all the numbers in the list. (product means all multiplied together)
print('\nPrint the product of all the numbers in the list')
product = 1
for num in xs:
    product *= num
print('Product:', product)
