def code():
    eind_res = {('A', 'X'): 0+3,
                ('C', 'X'): 0+2,
                ('B', 'X'): 0+1,
                ('B', 'Y'): 3+2,
                ('A', 'Y'): 3+1,
                ('C', 'Y'): 3+3,
                ('C', 'Z'): 6+1,
                ('B', 'Z'): 6+3,
                ('A', 'Z'): 6+2,}
    with open('input.txt', 'r') as bestand:
        sps_tour = bestand.read().rstrip('\n').split('\n')
    tal = 0
    for sps in sps_tour:
        sps_tup = tuple(sps.split())
        tal += eind_res.get(sps_tup)
    return tal


if __name__ == '__main__':
    print(code())
