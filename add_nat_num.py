def setunion(max):
    return sum(list(set([i for i in range(3,max,3)]).union(set([j for j in range(5,max,5)]))))

def reduced(max):
    val = reduce(lambda x,y: x+y, filter(lambda x: x % 3 == 0 or x % 5 == 0, range(max)))
    return val

def comprehend(max):
    return sum([x for x in range(max) if x%3 == 0 or x%5 == 0])

def rang(max):
    val = sum(range(0,max,3)) + sum(range(0,max,5)) - sum(range(0,1000,15))

# implementation of summation formula (currently fastest impl!
def formulaHelper(max, multiple):
    return (((int((max-1)/multiple)) * ((int((max-1)/multiple))+1)) / 2) * multiple
def formula(max):
    return formulaHelper(max, 3) + formulaHelper(max, 5) - formulaHelper(max, 15)

def short(max):
    res = 0
    fivemaxhit = False
    threemaxhit = False
    nums = {}
    for x in range(max):
        if fivemaxhit and threemaxhit: break
        if not fivemaxhit:
            fiver = x * 5
            if fiver < max:
                if not fiver in nums:
                    res += fiver
                    nums[fiver] = 1
            else:
                fivemaxhit = True
        if not threemaxhit:
            threer = x * 3
            if threer < max:
                if not threer in nums:
                    res += threer
                    nums[threer] = 1
            else:
                threemaxhit = True
    return res

# this can be written concisely as:
#    reduce(add,[x for x in range(max) if x % 3 == 0 or x % 5 == 0])
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
        print "Result (%s(%d)): %s, in %.7f seconds" % (algname, n, res, elapsed)

if __name__ == "__main__":
    runtimed(short, 1000)
    runtimed(obvious, 1000)
    runtimed(reduced, 1000)
    runtimed(rang, 1000)
    runtimed(formula, 1000)
    runtimed(comprehend, 1000)
    runtimed(setunion, 1000)
    
