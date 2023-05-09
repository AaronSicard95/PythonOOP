"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

class SerialGenerator:

    def __init__(self,start):
        self.start = start
        self.inc = start-1

    def generate(self):
        self.inc = self.inc+1
        return self.inc
    
    def reset(self):
        self.inc = self.start-1
