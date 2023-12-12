import re

with open('input_data/1.txt') as f:
    data = f.read().splitlines()

s = 0
for ln in data:
    cld = ln.split(':', 1)[1].strip()
    v_r = cld.split('|', 1)[0].strip()
    v_l = cld.split('|', 1)[1].strip()

    vs_r = re.findall(r'(?:\d+)', v_r)
    vs_l = re.findall(r'(?:\d+)', v_l)

    c = 0
    for i, v in enumerate(vs_r):
        for j, v_2 in enumerate(vs_l):
            if v == v_2:
                c += 1
    if c > 1:
        c = 2**(c-1)
    s += c
    
print(s)
