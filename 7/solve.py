curr_dir = '/'

d = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k""".split('\n')


def main():
    global curr_dir
    with open("input.txt", "r") as in_file:
        data = in_file.readlines()

    data = map(lambda x: x.strip(), data)

    directories = dict()

    for line in d:
        # print(line)
        if line[:4] == "$ cd":
            change_dir(line)
            if directories.get(curr_dir) is None:
                directories[curr_dir] = 0

        elif line[:4] == "$ ls":
            continue

        elif line[:4] == "dir ":
            continue

        else:
            directories[curr_dir] += get_file_size(line)

    # print(directories)
    # print(find_all_sizes(directories))
    ts = find_all_sizes(directories)

    solution1 = 0
    for value in ts.values():
        if value < 100000:
            solution1 += value

    print(solution1)


def change_dir(cmd: str):
    global curr_dir
    dest = cmd.split(' ')[-1]
    if dest == '..':
        curr_dir = curr_dir[:curr_dir.rfind('/')]
        if len(curr_dir) == 0:
            curr_dir = '/'
    elif dest == "/":
        curr_dir = "/"
    else:
        if len(curr_dir) == 1:
            curr_dir += dest
        else:
            curr_dir += f"/{dest}"


def get_file_size(listing: str):
    return int(listing.split(' ')[0])


def find_all_sizes(dirs: dict):
    total_sizes = dict()
    for dir in dirs.keys():
        if dir == '/':
            if total_sizes.get('') is None:
                total_sizes[''] = 0
            total_sizes[''] += dirs[dir]
            continue
        for key in dir.split('/'):
            if total_sizes.get(key) is None:
                total_sizes[key] = 0
            # print(total_sizes, key, dirs[dir])
            total_sizes[key] += dirs[dir]
    return total_sizes


if __name__ == '__main__':
    main()
