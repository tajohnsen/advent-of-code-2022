def main():
    with open("input.txt", "r") as in_file:
        data = in_file.read()

    print("Part 1:\t", find_marker_offset(data, 4))
    print("Part 2:\t", find_marker_offset(data, 14))


def all_unique(data: str):
    for index in range(len(data) - 1):
        key = data[index]
        if key in data[index+1:]:
            return False
    return True


def find_marker_offset(data: str, length: int) -> int:
    for index in range(len(data) - length):
        key = data[index:index+length]
        if all_unique(key):
            return index + length


if __name__ == '__main__':
    main()
