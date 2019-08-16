import sys

def test(did_pass):
    """ Print the result of a test """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)

def test_suite():
    """ Run the suite of tests for this module """
    current_time = MyTime(1, 20, 35)
    current_time.increment(10)
    test(current_time == MyTime(1, 20, 45))
    current_time.increment(-100)
    test(current_time == MyTime(1, 19, 5))

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

    def __eq__(self, other):
        return self.to_seconds() == other.to_seconds()

test_suite()
