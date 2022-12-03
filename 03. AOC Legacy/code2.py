def tellen(h1, h2, h3):
    h1, h2, h3 = set(h1), set(h2), set(h3)
    h12 = h1.intersection(h2)
    h23 = h2.intersection(h3)
    h123 = h12.intersection(h23)
    return h123.pop()


def code():
    prio = {chr(x): j for j, x in enumerate(range(97, 123), start=1)}
    prio.update((chr(x), j) for j, x in enumerate(range(65, 91), start=27))
    prio_tal = 0
    with open('input.txt', 'r') as bestand:
        inp = bestand.read().rstrip('\n').split('\n')
    for reg in range(2, len(inp), 3):
        prio_tal += prio[tellen(inp[reg-2], inp[reg-1], inp[reg])]
    return prio_tal


if __name__ == '__main__':
    print(code())
