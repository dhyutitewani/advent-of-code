import re

def decrease(data):
    if all(1 <= prev - curr <= 3 for prev, curr in zip(data, data[1:])):
        return True
    for i in range(len(data)):
        temp = data[:i] + data[i+1:]
        if all(1 <= prev - curr <= 3 for prev, curr in zip(temp, temp[1:])):
            return True
    return False

def increase(data):
    if all(1 <= curr - prev <= 3 for prev, curr in zip(data, data[1:])):
        return True
    for i in range(len(data)):
        temp = data[:i] + data[i+1:]
        if all(1 <= curr - prev <= 3 for prev, curr in zip(temp, temp[1:])):
            return True
    return False

def parse_input(file_path):
    with open(file_path, 'r') as f:
        return [list(map(int, re.findall(r'\d+', line))) for line in f]

def main():
    data = parse_input('input/1.txt')

    safe = sum(increase(row) or decrease(row) for row in data)
    print(safe)

if __name__ == '__main__':
    main()
