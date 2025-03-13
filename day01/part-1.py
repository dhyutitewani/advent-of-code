import re

def calculate_sum_of_distances(data):
    in1, in2 = zip(*sorted(data))
    in2 = tuple(sorted(in2))
    return sum(abs(i - j) for i, j in zip(in1, in2))

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return [tuple(map(int, re.findall(r'\d+', line))) for line in f]

def main():
    data = parse_input('input/1.txt')
    result = calculate_sum_of_distances(data)
    print(result)

if __name__ == '__main__':
    main()
