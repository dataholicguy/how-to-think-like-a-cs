import sys
import random
import math

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)

def test_suite():
    """ Run suite of tests for this module. """
    test(lotto_match([42,4,7,11,1,13], [2,5,7,11,13,17]) == 3)

    test(lotto_matches([42,4,7,11,1,13], my_tickets) == [1,2,3,1])

    test(primes_in([42, 4, 7, 11, 1, 13]) == 3)

    test(prime_misses(my_tickets) == [3, 29, 47])

def draw_lotto():
    result = []
    for _ in range(6):
        result.append(random.randint(1, 49))
    return result

def lotto_match(ticket, draw):
    """ Return the number of correct pick on a ticket. """
    count = 0
    for pick in ticket:
        if pick in draw:
            count += 1
    return count

def lotto_matches(draw, my_tickets):
    """ Return a list telling how many picks were correct on each ticket """
    result = []
    for ticket in my_tickets:
        result.append(lotto_match(ticket, draw))
    return result

def is_prime(number):
    """ Check if a number is prime or not. """
    if number == 1:
        return False
    count = 0
    square_root = int(math.sqrt(number))
    for i in range(1, square_root +1):
        if number % i == 0:
            count += 1
    return count == 1

def primes_in(li):
    """ Return the number of prime numbers in a list. """
    count = 0
    for num in li:
        if is_prime(num):
            count += 1
    return count

def prime_generate(ub):
    """ Return a list of prime numbers lower than ub. """
    result = [i for i in range(2, ub+1) if is_prime(i)]
    return result

prime_list = prime_generate(49)     # Generate a list of prime number under 49
my_tickets = [ [ 7, 17, 37, 19, 23, 43],
               [ 7,  2, 13, 41, 31, 43],
               [ 2,  5,  7, 11, 13, 17],
               [13, 17, 37, 19, 23, 43] ]

def prime_misses(my_tickets):
    result = []
    all_num = []
    for ticket in my_tickets:
        all_num.extend(ticket)
    for pn in prime_list:
        if pn not in all_num:
            result.append(pn)
    return result

def average_draw(num_correct):
    """ Return the average number of draws are needed until one of
        4 tickets has at least num_correct correct picks """
    global my_tickets
    TIMES = 20              # Number of times for experimenting
    times = []              # count number of times draw lotto
    time = 0
    matches = []
    for _ in range(TIMES):
        while True:
            lotto = draw_lotto()
            time += 1
            matches = lotto_matches(lotto, my_tickets)
            if num_correct in matches:
                times.append(time)
                time = 0
                break
    result = sum(times) / TIMES
    return result

def main():
    print('Average 3: {0} times.'.format(average_draw(3)))
    print('Average 4: {0} times.'.format(average_draw(4)))
    print('Average 5: {0} times.'.format(average_draw(5)))

main()

test_suite()
