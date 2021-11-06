def nod(n):
    for i in range(len(n)):
        pass


def nok(n):
    for i in range(len(n)):
        pass


def dge(mx, mn=None):
    ret = []
    if mn is None:
        for i in range(1, mx + 1):
            if i > 1:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    ret.extend([i])
    elif mn is not None:
        for i in range(mn, mx + 1):
            if i > mn:
                for j in range(2, i):
                    if i % j == 0:
                        break
                else:
                    ret.extend([i])
    return ret
    pass


def raz(did):
    ret = []
    ind = 0
    fid = 2
    while True:
        if did % dge(fid) == 0:
            ret[ind] = fid
            ind += 1
        else:
            fid += 1
    pass


print(dge(20))
