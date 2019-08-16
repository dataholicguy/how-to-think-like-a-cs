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

    def increment(self, seconds):
        self.seconds = self.to_seconds() + seconds
        new_time = MyTime(0, 0, self.seconds)
        self.hours = new_time.hours
        self.minutes = new_time.minutes
        self.seconds = new_time.seconds

current_time = MyTime(1, 20, 35)
print('Current Time {0}'.format(current_time))
current_time.increment(100)
print('New Current Time: {0}'.format(current_time))
