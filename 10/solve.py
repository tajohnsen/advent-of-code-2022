from itertools import *


INPUT = "input.txt"


def main():
    with open(INPUT, "r") as in_file:
        data = map(lambda x: x.rstrip(), in_file.readlines())

    values = list([1])  # starts with 1

    for instruction in data:
        values.extend(process_op(instruction, values[-1]))

    filtered = (index * values[index - 1] for index in takewhile(lambda x: x < len(values), count(20, 40)))
    print(sum(filtered))

    list(starmap(draw, ((index, values[index]) for index in range(len(values)))))


def process_op(op: str, x: int):
    if op == "noop":
        return [x]
    instr, value = op.split(' ')
    if instr == "addx":
        return [x, x + int(value)]


def draw(index, value):
    adjusted = (value % 40) - 1  # make index 0
    if index % 40 in list(range(adjusted, adjusted+3)):
        print('#', end='')
    else:
        print(".", end='')
    if (index + 1) % 40 == 0:
        print("")


if __name__ == "__main__":
    main()
