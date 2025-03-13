import re

def mul(a, b):
    return a * b

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read()

    match = re.findall(r'mul\((\d+)\,(\d+)\)', lines)
    return [(int(a), int(b)) for a, b in match]

def main():
    sum_mem = 0
    data = parse_input('input/1.txt')
    for a, b in data:
        result = mul(a, b)
        sum_mem += result

    print(sum_mem)

if __name__ == '__main__':
    main()