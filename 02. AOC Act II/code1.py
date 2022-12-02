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
    tal = 0
    for sps in sps_tour:
        sps = tuple(sps.split())
        print(sps)
        tal += eind_res.get(sps) + win.get(sps[-1])
    return tal


if __name__ == '__main__':
    print(code())
