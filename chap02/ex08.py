# Write a Python program to solve the general version of ex07.py problem

now = int(input('What time is it? '))
wait = int(input('Number of hours to wait: '))

time = now + wait % 12
print('Time when the alarm go off:', time)
