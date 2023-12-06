from itertools import islice

def sum_nums(ln):
    l = []
    c = 0 

    for i in ln:
        if i.isdigit():
            l.append(i)
            c = c + 1
            
    if c > 1:
        num = int(l[0] + l[-1])
        return(num)
    else:
        num = int(l[0] + l[0])
        return(num)

def main():
    with open('input_data/1.txt','r') as f:
        ls = f.readlines()

    s = 0
    for ln in ls:
        s += sum_nums(ln)

    print(s)

if __name__ == '__main__':
    main()
