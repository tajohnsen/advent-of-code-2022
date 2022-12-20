from itertools import *
from math import lcm

INPUT = "input.txt"
# INPUT = "test.txt"


class Monkey(object):
    def __init__(self, lines: list):
        id_line = lines[0]
        id_ = id_line.split(' ')[1]
        self.id = int(id_.replace(":", ''))
        items_line = lines[1]
        items = items_line.split(': ')[1].split(', ')
        self.items = list(map(int, items))
        operation_line = lines[2]
        operation = operation_line.split(': ')[1]
        action = operation.split('old ')[1]
        self.action = tuple(action.split(' '))
        test_line = lines[3]
        self.test = int(test_line.split('divisible by ')[1])
        result_lines = lines[4:6]
        self.destination = tuple(map(lambda x: int(x.split("throw to monkey ")[1]), result_lines))
        self.inspecting = None  # what the monkey is currently acting on

    def print(self):
        print(self.id, self.items, self.action, self.test, self.destination)

    def decide(self, lcm_=1):
        self.inspecting = self.items.pop(0)
        worry_level = self.operate()
        # worry_level = int(worry_level / 3)  # uncomment for part 1
        worry_level %= lcm_  # remove for part 1
        destination = self.test_worry_level(worry_level)
        item = self.inspecting
        self.inspecting = None
        return worry_level, destination

    def operate(self):
        number = self.action[1]
        if number == 'old':
            number = self.inspecting
        else:
            number = int(number)
        if self.action[0] == '*':
            result = self.inspecting * number
        else:  # only two actions
            result = self.inspecting + number
        return result

    def test_worry_level(self, worry_level):
        if worry_level % self.test == 0:
            return self.destination[0]
        else:
            return self.destination[1]


def main():
    with open(INPUT, "r") as in_file:
        data = map(lambda x: x.rstrip(), in_file.readlines())

    monkeys = list()
    monkey_data = list(takewhile(lambda x: x != '', data))

    while monkey_data:
        monkeys.append(Monkey(monkey_data))
        monkey_data = list(takewhile(lambda x: x != '', data))

    monkey_count = [0 for monkey in monkeys]
    print(monkey_count)

    divs = (x.test for x in monkeys)
    lcm_ = lcm(*divs)  # shouldn't break part 1 but i didn't test

    for round_number in range(10000):  # make 20 for part 1
        for monkey in monkeys:
            monkey_index = monkeys.index(monkey)
            # monkey.print()
            while monkey.items:
                monkey_count[monkey_index] += 1
                worry, destination = monkey.decide(lcm_)
                monkeys[destination].items.append(worry)
        # for monkey in monkeys:
        #     monkey.print()
        if (round_number + 1) % 1000 == 0:
            print("round number", round_number + 1)
            print(monkey_count)

    print(monkey_count)

    total = 1
    print(sorted(monkey_count, reverse=True))
    for num in sorted(monkey_count, reverse=True)[:2]:
        total *= num

    print(total)


if __name__ == "__main__":
    main()
