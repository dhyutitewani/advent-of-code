import re

with open('input_data/1.txt') as f:
    data = f.readlines()

vs = [list(map(int, re.findall(r'\d+', ln))) for ln in data]

r = 1
for i, v in enumerate(vs[0]): 
    c = 0
    for j in range(1, v):
        dist = j * (v - j)
        if (dist > vs[1][i]): c += 1

    r *= c

print(n)
