import os


class LogInfo(object):
    def __init__(self):
        rows, columns = os.popen('stty size', 'r').read().split()
        self.term_width = int(columns)
        self.stage_separator = "=" * self.term_width

    def std_print(self, string):
        print(string)

    def stage_print(self, string):
        print(self.stage_separator)
        print(string)
        print(self.stage_separator)

    def mark_done(self, string):
        print('\x1b[1A', end='\r')
        print(string + '[DONE]')

    def clear_line(self):
        print('\x1b[2K', end='\r')
