from itertools import *


class Range(object):
    def __init__(self, range_string: str):
        lower, upper = range_string.split('-')
        self.lower = int(lower)
        self.upper = int(upper)


class Ranges(object):
    def __init__(self, ranges_string: str):
        self.range1_str, self.range2_str = ranges_string.split(',')
        self.ranges = tuple((Range(self.range1_str), Range(self.range2_str)))

    def fully_contained(self) -> bool:
        return (self.ranges[0].lower >= self.ranges[1].lower and self.ranges[0].upper <= self.ranges[1].upper) \
            or \
            (self.ranges[1].lower >= self.ranges[0].lower and self.ranges[1].upper <= self.ranges[0].upper)


with open("input.txt") as in_file:
    data = in_file.readlines()


stripped = map(lambda x: x.strip(), data)

filtered = filter(lambda x: Ranges(x).fully_contained(), stripped)

print(len(list(filtered)))
