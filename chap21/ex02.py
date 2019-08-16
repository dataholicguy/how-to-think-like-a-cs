class MyTime:

    def __init__(self, hrs=0, mins=0, secs=0):
        """ Create a new MyTime object initialized to hrs, mins, secs.
           The values of mins and secs may be outside the range 0-59,
           but the resulting MyTime object will be normalized.
        """

        # Calculate total seconds to represent
        totalsecs = hrs*3600 + mins*60 + secs
        self.hours = totalsecs // 3600
        leftoversecs = totalsecs % 3600
        self.minutes = leftoversecs // 60
        self.seconds = leftoversecs % 60

    def __str__(self):
        return '{0:02}:{1:02}:{2:02}'.format(self.hours, self.minutes, self.seconds)

    def to_seconds(self):
        """
            Return the number of seconds represented
            by this instance
        """
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def between(self, t1, t2):
        return self.to_seconds() >= t1.to_seconds() and self.to_seconds() < t2.to_seconds()

t1 = MyTime(3, 12, 20)
t2 = MyTime(4, 1, 50)
my_time1 = MyTime(3, 10, 25)
print(my_time1.between(t1, t2))
my_time2 = MyTime(4, 0, 20)
print(my_time2.between(t1, t2))
