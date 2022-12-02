def code():
    eind_res = {('A', 'X'): 3,
                ('B', 'Y'): 3,
                ('C', 'Z'): 3,
                ('A', 'Y'): 6,
                ('B', 'Z'): 6,
                ('C', 'X'): 6,
                ('A', 'Z'): 0,
                ('B', 'X'): 0,
                ('C', 'Y'): 0}
    win = {'X': 1,
           'Y': 2,
           'Z': 3}
    with open('input.txt', 'r') as bestand:
        sps_tour = bestand.read().rstrip('\n').split('\n')
    return sum([eind_res[tuple(x.split())] + \
                win[x[-1]] for x in sps_tour])


if __name__ == '__main__':
    print(code())
