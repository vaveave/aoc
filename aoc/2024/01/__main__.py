import numpy as np
from pathlib import Path


def read_input(input_data):
    return np.fromstring(input_data, sep=' ', dtype=int).reshape(-1, 2).T


def part_1(location_ids):
    list_1, list_2 = -np.sort(-location_ids)
    return np.sum(abs(list_2 - list_1))


def part_2(location_ids):
    list_1, list_2 = location_ids
    return sum(location * np.count_nonzero(list_2 == location) for location in list_1)


test_data = """3   4
4   3
2   5
1   3
3   9
3   3"""


if __name__ == "__main__":
    with (Path(__file__).parent / "input.txt").open("r") as f:
        data = f.read()

    print("Part 1:", part_1(read_input(data)))
    print("Part 2:", part_2(read_input(data)))
