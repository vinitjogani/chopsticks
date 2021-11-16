
def sanitize(i, j, k, l):
    return min(i, j), max(i, j), min(k, l), max(k, l)


def get_transitions(i, j, k, l):
    if (i == 0 and j == 0) or (k == 0 and l == 0):
        return []

    t = []

    if j > 0:
        for i2 in range(i+1, min(i+j+1, 5)):
            t.append((i2, j + i - i2, k, l))
        if k > 0:
            t.append((i, j, (k+j) % 5, l))
        if l > 0:
            t.append((i, j, k, (l+j) % 5))
    if i > 0:
        for j2 in range(j+1, min(i+j+1, 5)):
            t.append((i + j - j2, j2, k, l))
        if k > 0:
            t.append((i, j, (k+i) % 5, l))
        if l > 0:
            t.append((i, j, k, (l+i) % 5))
    sanitized = [sanitize(*x) for x in set(t)]
    return [x for x in sanitized if x != (i, j, k, l)]


def states():
    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    if i > j or k > l:
                        continue
                    yield (i, j, k, l)


def transitions():
    transitions = {}
    for i, j, k, l in states():
        transitions[(i, j, k, l)] = get_transitions(i, j, k, l)
    return transitions
