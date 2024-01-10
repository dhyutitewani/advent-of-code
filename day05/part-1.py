import re

with open('input_data/1.txt') as f:
    data = [line.strip() for line in f.read().split('\n\n')]

seeds = [list(map(int, ln.split(':')[1].split())) for ln in data[:1]][0]
maps = [list(map(int, re.findall(r'\d+', ln))) for ln in data[1:]]

for m in maps:
    l = []
    for i in seeds:
        for j in range(0, len(m), 3):
            c = m[j:j+3]
            if c[1] <= i < c[1] + c[2]:
                l.append(i - c[1] + c[0])
                break
        else:
            l.append(i)
    seeds = l

print(min(l))