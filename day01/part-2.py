import re
import collections

def calculate_sum_of_distances(data):
    s = 0
    in1, in2 = zip(*data)
    freq = collections.Counter(in2)

    for key, value in freq.items():
        key = int(key)
        if key in in1:
            s += abs(key * value)
    return s

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return [tuple(map(int, re.findall(r'\d+', line))) for line in f]

def main():
    data = parse_input('input/1.txt')
    result = calculate_sum_of_distances(data)
    print(result)

if __name__ == '__main__':
    main()
