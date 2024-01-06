import re 

def sum_calc(vs):
    total = 0

    for r, row in enumerate(vs):
        for c, char in enumerate(row):
            if char != '*':
                continue

            cs = set()

            for sr in [r-1, r, r+1]:
                for sc in [c-1, c, c+1]:
                    if sr < 0 or sr >= len(vs) or sc < 0 or sc >= len(vs[sr]) or not vs[sr][sc].isdigit():
                        continue
                    while sc > 0 and vs[sr][sc-1].isdigit():
                        sc -= 1
                    cs.add((sr, sc))

            if len(cs) != 2:
                continue

            l = []

            for a, b in cs:
                n = ''
                while b < len(vs[a]) and vs[a][b].isdigit():
                    n += vs[a][b]
                    b += 1
                l.append(int(n))

            total += l[0] * l[1]

    print(total)

def main():
    with open(r'input_data/1.txt','r') as f:
        ls = f.read().splitlines()

    sum_calc(ls)

if __name__ == '__main__':
    main()
    