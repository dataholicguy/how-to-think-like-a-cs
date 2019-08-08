# You look at the clock and it is exactly 2pm. You set an alarm to go off in 51 hours.
# At what time does the alarm go off?

now = 2

time = now + 51 % 12

print('Time the alarm go off:', time)
