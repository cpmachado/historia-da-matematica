import argparse
import csv
from fractions import Fraction
from math import floor, log, ceil
from functools import partial
from itertools import takewhile

N = 15
en = Fraction(1, 10000)
x = 5
y = 3


class babylonianSqrt(object):
    def __init__(self, N, x, y, en):
        self.x = Fraction(x)
        self.y = Fraction(y)
        self.N = N
        self.en = Fraction(en)
        self.i = 0
        self.stop = False

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.stop:
            raise StopIteration()
        self.stop = self.x - self.y < self.en
        i, x, y, en = self.i, self.x, self.y, self.x - self.y
        self.x, self.y, self.i = (x + y) / 2, 2 * self.N / (x + y), i + 1
        return (i, x, y, en)


for i, xi, yi, eni in babylonianSqrt(N, x, y, en):
    print(i, xi, yi, eni, sep=",")
