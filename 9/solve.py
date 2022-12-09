def main():
    with open("input.txt", "r") as in_file:
        data = map(lambda x: x.rstrip(), in_file.readlines())
        data = list(data)

    with open("test.txt", "r") as in_file:
        test = map(lambda x: x.rstrip(), in_file.readlines())

    head = [0, 0]
    tail = [0, 0]

    track_locations = dict()
    for instruction in data:
        track_locations = move_head(head, tail, instruction, track_locations)

    print(len(track_locations.keys()))

    line = [[0, 0] for _ in range(10)]

    track_locations = dict()
    for instruction in data:
        track_locations = move_line(line, instruction, track_locations)

    from pprint import pprint
    # pprint(track_locations)
    print(len(track_locations.keys()))


def move_line(line: list, instruction: str, track_locations: dict):
    instructions = instruction.split(' ')
    if instructions[0] == "U":
        for move_number in range(int(instructions[1])):
            line[0][0] += 1
            for index in range(9):
                move_tail(line[index], line[index + 1])
            key = str(line[9])
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
            # print(instruction, line)
    if instructions[0] == "R":
        for move_number in range(int(instructions[1])):
            line[0][1] += 1
            for index in range(9):
                move_tail(line[index], line[index + 1])
            key = str(line[9])
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
            # print(instruction, line)
    if instructions[0] == "D":
        for move_number in range(int(instructions[1])):
            line[0][0] -= 1
            for index in range(9):
                move_tail(line[index], line[index + 1])
            key = str(line[9])
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
            # print(instruction, line)
    if instructions[0] == "L":
        for move_number in range(int(instructions[1])):
            line[0][1] -= 1
            for index in range(9):
                move_tail(line[index], line[index + 1])
            key = str(line[9])
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
            # print(instruction, line)
    return track_locations


def move_head(head: list, tail: list, instruction: str, track_locations: dict):
    instructions = instruction.split(' ')
    if instructions[0] == "U":
        for move_number in range(int(instructions[1])):
            head[0] += 1
            move_tail(head, tail)
            key = str(tail)
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
    if instructions[0] == "R":
        for move_number in range(int(instructions[1])):
            head[1] += 1
            move_tail(head, tail)
            key = str(tail)
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
    if instructions[0] == "D":
        for move_number in range(int(instructions[1])):
            head[0] -= 1
            move_tail(head, tail)
            key = str(tail)
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
    if instructions[0] == "L":
        for move_number in range(int(instructions[1])):
            head[1] -= 1
            move_tail(head, tail)
            key = str(tail)
            if track_locations.get(key) is None:
                track_locations[key] = 0
            track_locations[key] += 1
    return track_locations


def move_tail(head: list, tail: list):
    x_dist = head[0] - tail[0]
    y_dist = head[1] - tail[1]
    if abs(x_dist) > 1:
        tail[0] += int(x_dist / abs(x_dist))
        if y_dist != 0:
            tail[1] += y_dist
    elif abs(y_dist) > 1:
        tail[1] += int(y_dist / abs(y_dist))
        if x_dist != 0:
            tail[0] += x_dist
    return tail  # lists are mutable so this isn't necessary but looks nice


if __name__ == "__main__":
    main()
