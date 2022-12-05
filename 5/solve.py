from itertools import *
from string import ascii_uppercase


class Stacks(object):
    def __init__(self, initial_state: list):
        column_row = initial_state[-1]
        indexes = list()
        counter = count(1)  # count starting at 1
        while True:
            found = column_row.find(str(next(counter)))
            if found == -1:
                break
            indexes.append(found)
        self.columns = list([[] for _ in range(len(indexes))])

        for row in initial_state[:-1]:
            for column in range(len(indexes)):
                try:
                    if row[indexes[column]] in ascii_uppercase:
                        self.columns[column].append(row[indexes[column]])
                except IndexError:
                    break  # no more left most likely

        self.columns.insert(0, None)  # start at 1 to make string processing easier

    @staticmethod
    def get_count_source_dest(action_str: str):
        count_label = "move "
        source_label = "from "
        dest_label = "to "
        count_slice = action_str[action_str.find(count_label) + len(count_label):]
        count = int(count_slice[:count_slice.find(' ')])
        source_slice = action_str[action_str.find(source_label) + len(source_label):]
        source = int(source_slice[:source_slice.find(' ')])
        dest_slice = action_str[action_str.find(dest_label) + len(dest_label):]
        dest = int(dest_slice)
        return count, source, dest

    def move(self, action_str: str):
        cnt, source, dest = self.get_count_source_dest(action_str)
        for c in range(cnt):
            value = self.columns[source].pop(0)
            self.columns[dest].insert(0, value)

    def move9001(self, action_str: str):
        cnt, source, dest = self.get_count_source_dest(action_str)
        slc = self.columns[source][:cnt]
        for _ in range(cnt):
            self.columns[source].pop(0)
        self.columns[dest] = slc + self.columns[dest]

    def print_solution(self):
        for column in self.columns[1:]:
            print(column[0], end='')
        print("")

    def print(self):
        for column in self.columns[1:]:
            print(column)


def main():
    with open("input.txt") as in_file:
        data = in_file.readlines()

    end_of_initial_state = data.index("\n")  # first lone newline is the separator

    stripped = map(lambda x: x.rstrip(), data)

    initial_state = list(islice(stripped, 0, end_of_initial_state))
    stacks = Stacks(initial_state)
    next(stripped)  # just to consume the blank
    actions1 = list(stripped)
    actions2 = actions1[::]  # copy
    for action in actions1:
        stacks.move(action)
    stacks.print_solution()

    stacks = Stacks(list(initial_state))

    for action in actions2:
        stacks.move9001(action)

    stacks.print_solution()


if __name__ == '__main__':
    main()
