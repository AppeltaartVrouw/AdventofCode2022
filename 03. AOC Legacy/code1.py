def tellen(regel):
    punt = int(len(regel)/2)
    h1 = set(regel[:punt])
    h2 = set(regel[punt:])
    letter = h1.intersection(h2)
    return letter.pop()


def code():
    prio = {chr(x): j for j, x in enumerate(range(97, 123), start=1)}
    prio.update((chr(x), j) for j, x in enumerate(range(65, 91), start=27))
    prio_tal = 0
    with open('input.txt', 'r') as bestand:
        for regel in bestand:
            prio_tal += prio[tellen(regel.rstrip())]
    return prio_tal


if __name__ == '__main__':
    print(code())
