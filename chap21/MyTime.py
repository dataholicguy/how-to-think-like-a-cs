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

    def add_time(self, t):
        secs = self.to_seconds() + t.to_seconds()
        return MyTime(0, 0, secs)

    # Operator overloading
    def __add__(self, other):
        return MyTime(0, 0, self.to_seconds()+other.to_seconds())

    def after(self, time2):
        """ Return True if I am strictly greater than time2 """
        return self.to_seconds() > time2.to_seconds()

t1 = MyTime(1, 30, 52)
t2 = MyTime(3, 45, 10)
print(t1.add_time(t2))

t3 = MyTime(2, 10, 50)
t4 = MyTime(3, 20, 30)
print(t3 + t4)
