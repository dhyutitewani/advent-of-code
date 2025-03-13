import re

def decrease(data):
    prev = data[0]
    for i in data[1:]:
        if not (prev > i and 1 <= (prev - i) <= 3):
            return False
        prev = i

    return True

def increase(data):
    prev = data[0]
    for i in data[1:]:
        if not (i > prev and 1 <= (i - prev) <= 3):
            return False
        prev = i

    return True

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, re.findall(r'\d+', line))) for line in f]

def main():
    data = parse_input('input/1.txt')

    safe = 0
    for row in data:
        if increase(row) or decrease(row):
            safe += 1

    print(safe)

if __name__ == '__main__':
    main()

"""
alt code
improved version of the redundant code
"""

# import re
#
# def is_valid(seq, cmp):
#     return all(1 <= abs(a - b) <= 3 and cmp(a, b) for a, b in zip(seq, seq[1:]))
#
# def parse_input(file_path):
#     with open(file_path) as f:
#         return [list(map(int, re.findall(r'\d+', line))) for line in f]
#
# def main():
#     data = parse_input('input/1.txt')
#     print(sum(is_valid(row, int.__lt__) or is_valid(row, int.__gt__) for row in data))
#
# if __name__ == '__main__':
#     main()
