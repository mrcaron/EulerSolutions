def reduced(max):
    res = reduce( lambda x, y: x + ( (y % 5 == 0 or y % 3 == 0) and y or 0 ), range(0,max))
    return res

def short(max):
    res = 0
    fivemaxhit = False
    threemaxhit = False
    nums = {}
    for x in range(max):
        if fivemaxhit and threemaxhit: break
        if not fivemaxhit:
            fiver = x * 5
            if not fiver in nums and fiver < max: 
                res += fiver
                nums[fiver] = 1
            else:
                fivemaxhit = True
        if not threemaxhit:
            threer = x * 3
            if not threer in nums and threer < max: 
                res += threer
                nums[threer] = 1
            else:
                threemaxhit = True
    return res

def obvious(max):
    res = 0
    for x in range(max):
        if (x % 5 == 0 or x % 3 == 0): res += x
    return res

def runtimed(alg, *set):
    from time import clock, time
    algname = alg.__name__
    for n in set:
        start = clock()
        res = alg(n)
        elapsed = (clock() - start)
        print "Result (%s(%d)): %s, in %.5f seconds" % (algname, n, res, elapsed)

if __name__ == "__main__":
    runtimed(short, 10, 1000)
    runtimed(obvious, 10, 1000)
    runtimed(reduced, 10, 1000)
    
