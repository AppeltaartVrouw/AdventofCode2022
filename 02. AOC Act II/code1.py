def code():
    eind_res = {('A', 'X'): 3 + 1,
                ('B', 'Y'): 3 + 2,
                ('C', 'Z'): 3 + 3,
                ('A', 'Y'): 6 + 2,
                ('B', 'Z'): 6 + 3,
                ('C', 'X'): 6 + 1,
                ('A', 'Z'): 0 + 3,
                ('B', 'X'): 0 + 1,
                ('C', 'Y'): 0 + 2}
    win = {'X': 1,
           'Y': 2,
           'Z': 3}
    with open('input.txt', 'r') as bestand:
        sps_tour = bestand.read().rstrip('\n').split('\n')
    return sum([eind_res[tuple(x.split())] for x in sps_tour])


if __name__ == '__main__':
    print(code())
