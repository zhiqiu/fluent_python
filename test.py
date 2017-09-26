#-*- coding:utf-8 -*-
import sys
import time
import hashlib
import asyncio
import multiprocessing

class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector(x, y)

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

def test():
    vector = Vector(3, 4)
    a = [1, 2, 3]
    for a, b in tuple((1, i) for i in a):
        print(a, b)

    m1 = hashlib.md5()
    m1.update('123456'.encode())
    print(m1.hexdigest())
    print(vector)

DELAY = 0.1
DISPLAY = [ '|', '/', '-', '\\' ]

def spinner_func(before='', after=''):
    write, flush = sys.stdout.write, sys.stdout.flush
    pos = -1
    while True:
        pos = (pos + 1) % len(DISPLAY)
        msg = before + DISPLAY[pos] + after
        write(msg); flush()
        write('\x08' * len(msg))
        time.sleep(DELAY)

def long_computation():
    # emulate a long computation
    time.sleep(10)

def main():
    spinner = multiprocessing.Process(
        None, spinner_func, args=('Please wait ... ', ''))
    spinner.start()
    try:
        long_computation()
        print('Computation done')
    finally:
        spinner.terminate()




if __name__ == '__main__':
    main()