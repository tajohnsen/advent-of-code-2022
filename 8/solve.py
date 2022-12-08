def main():
    with open("input.txt", "r") as in_file:
        data = in_file.readlines()
        data = list(map(lambda x: x.rstrip(), data))

    with open("test.txt", "r") as in_file:
        test = in_file.readlines()
        test = list(map(lambda x: x.rstrip(), test))

    test = data  # remove this to use the small test input

    total_visible = 0
    for row_index in range(len(test)):
        for column_index in range(len(test[row_index])):
            if visible(row_index, column_index, test):
                total_visible += 1

    print(total_visible)

    sight_scores = dict()
    for row_index in range(len(test)):
        for column_index in range(len(test[row_index])):
            sight_score = total_score(row_index, column_index, test)
            if sight_scores.get(sight_score) is None:
                sight_scores[sight_score] = list()
            sight_scores[sight_score].append((row_index, column_index))

    highest_score = max(sight_scores.keys())
    print(f"Highest score was {highest_score} at position(s): {sight_scores.get(highest_score)}")


def column_visible(index: int, column: list):
    before = True
    after = True
    if index == 0 or index == (len(column) - 1):
        return True
    for row in column[:index]:
        if row >= column[index]:
            before = False
            break
    for row in column[index+1:]:
        if row >= column[index]:
            after = False
            break

    return before or after


row_visible = column_visible  # same functionality but this makes things easier to understand


def visible(row_index: int, column_index: int, grid: list) -> bool:
    if row_index == 0 or column_index == 0:
        return True
    if column_index == (len(grid[row_index]) - 1):
        return True
    if row_index == (len(grid) - 1):
        return True

    return row_visible(column_index, list(grid[row_index])) \
        or \
        column_visible(row_index, [value[column_index] for value in grid])


def row_score(column_index, row):
    index = column_index  # hack for the edges
    for index in range(column_index - 1, -1, -1):
        if row[index] >= row[column_index]:
            break
    left_score = column_index - index
    index = column_index  # hack for the edges
    for index in range(column_index + 1, len(row)):
        if row[index] >= row[column_index]:
            break
    right_score = index - column_index
    return right_score * left_score


def column_score(row_index, column):
    return row_score(row_index, column)


def total_score(row_index, column_index, grid):
    return row_score(column_index, grid[row_index]) * column_score(row_index, [value[column_index] for value in grid])


if __name__ == "__main__":
    main()
