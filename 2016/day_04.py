import re
from collections import Counter, OrderedDict
from pathlib import Path


def part1(input_data):
    rooms_list = input_data.splitlines()
    pattern = r"([a-z\-]+)-(\d+)\[([a-z]+)\]"
    real_rooms_counter = 0
    for room in rooms_list:
        matched_pattern = re.match(pattern, room)
        decoded_room = [matched_pattern.group(1).replace("-", ""), int(matched_pattern.group(2)), matched_pattern.group(3)]
        # Count the occurrences of each character
        char_count = Counter(decoded_room[0])
        # Sort the characters by frequency (descending), then alphabetically for ties
        sorted_string = ''.join(sorted(decoded_room[0], key=lambda x: (-char_count[x], x)))
        if "".join(list(OrderedDict.fromkeys(sorted_string)))[:5] == decoded_room[2]:
            real_rooms_counter += decoded_room[1]
    return str(real_rooms_counter)


def decrypt_room_name(room_name, key):
    decrypted_name = ""
    for ch in room_name:
        if ch != "-":
            decrypted_name += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            decrypted_name += "-"
    return decrypted_name


def part2(input_data):
    rooms_list = input_data.splitlines()
    pattern = r"([a-z\-]+)-(\d+)\[([a-z]+)\]"
    output = []
    for room in rooms_list:
        matched_pattern = re.match(pattern, room)
        decoded_room = [matched_pattern.group(1), int(matched_pattern.group(2)), matched_pattern.group(3)]
        decoded_room[0] = decrypt_room_name(decoded_room[0], decoded_room[1])
        if "north" in decoded_room[0]:
            output += decoded_room
    return output


if __name__ == "__main__":
    # Get the input file path and read the input data
    input_file = Path(__file__).parent / f"day_04_input.txt"
    with open(input_file) as f:
        data = f.read().strip()

    print("Part 1:", part1(data))
    print("Part 2:", part2(data))