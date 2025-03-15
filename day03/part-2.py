"""
    use a dictionary to solve this
    kays will be do() and dont()
"""

import re

def mul(a, b):
    return a * b

def parse_input(file_path):
    with open(file_path, 'r') as f:
        lines = f.read()

    instructions = True
    instruction_set = []
    match = re.findall(r'mul\((\d+)\,(\d+)\)|(do\(\))|(don\'t\(\))', lines)

    for i in match:
        if i[3] == "don't()":
            instructions = False
        elif i[2] == "do()":
            instructions = True
        if i[0] and i[1] and instructions:
            instruction_set.append([int(i[0]), int(i[1])])

    return instruction_set

def main():
    sum_mem = 0
    data = parse_input('input/1.txt')

    for a, b in data:
        result = mul(a, b)
        sum_mem += result

    print(sum_mem)

if __name__ == '__main__':
    main()