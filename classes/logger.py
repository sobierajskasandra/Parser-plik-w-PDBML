# coding: utf8
import sys

class PDBMLLogger(object):
    def __init__(self, file):
        self.terminal = sys.stdout
        # Remove previous contents
        open(file, 'w').close()
        self.log = open(file, 'a')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass
