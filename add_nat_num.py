def short(max):
    res = 0
    iterations = 0
    fivemaxhit = False
    threemaxhit = False
    for x in range(max):
        if fivemaxhit and threemaxhit: break

        if not fivemaxhit:
            fiver = x * 5
            if fiver < max: 
                res += fiver
            else:
                fivemaxhit = True
        if not threemaxhit:
            threer = x * 3
            if threer < max: 
                res += threer
            else:
                threemaxhit = True
        iterations += 1
    return (res, iterations)

def obvious(max):
    res = 0
    iterations = 0
    for x in range(max):
        if (x % 5 == 0 or x % 3 == 0): res += x
        iterations += 1
    return (res, iterations)

def runtimed(alg, *set):
    from time import clock, time
    algname = alg.__name__
    for n in set:
        start = clock()
        (res,it) = alg(n)
        elapsed = (clock() - start)
        print "Result (%s(%d)): %s, iterations: %d, in %.5f seconds" % (algname, n, res, it, elapsed)

if __name__ == "__main__":
    runtimed(short, 10, 1000)
    runtimed(obvious, 10, 1000)
    
