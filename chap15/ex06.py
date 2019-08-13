import sys

def test(did_pass):
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = 'Test at line {0} ok.'.format(linenum)
    else:
        msg = 'Test at line {0} FAILED.'.format(linenum)
    print(msg)

def test_suite():
    """ Run suite of tests for this module """
    pass

class SMS_store:
    def __init__(self):
        self.inbox = []

    def add_new_arrival(self, from_number, text_of_sms,read_status = False):
        number = str(from_number)
        time_received = time.strftime("%D %T")
        self.inbox.append([time_received, number, text_of_sms, read_status])

    def message_count(self):
        return "There are {0} messages in your Inbox".format(len(self.inbox))

    def get_unread_indexes(self):
        unread = []
        for index, message in enumerate(self.inbox):
            if False in message:
                unread.append(index)
        return "Unread Messages in:", unread

    def get_message(self, index):
        message = self.inbox[index]
        message[3] = "Read"
        return message[ : 3]

    def delete(self, index):
        del self.inbox[index]
        return "Deleted Message", index

    def clear(self):
        self.inbox = []
        return "Empty Inbox"
